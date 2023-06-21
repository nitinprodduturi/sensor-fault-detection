import os,sys
from sensor.exception import SensorException
from sensor.logger import logging
from sensor.utils.main_utils import read_yaml_file
from sensor.pipeline.training_pipeline import TrainPipeline
import pandas as pd
import numpy as np

from fastapi import FastAPI,File,UploadFile,Request
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from uvicorn import run as app_run
from sensor.constant.application import APP_HOST,APP_PORT
from fastapi.responses import StreamingResponse

from sensor.ml.model.estimator import ModelResolver,TargetValueMapping
from sensor.constant.training_pipeline import SAVED_MODEL_DIR
from sensor.utils.main_utils import load_object
from sensor.constant.training_pipeline import SCHEMA_FILE_PATH
import io

env_file_path=os.path.join(os.getcwd(),'env.yaml')

def set_env_variable(env_file_path):

    if os.getenv('MONGO_DB_URL',None) is None:
        env_config=read_yaml_file(env_file_path)
        os.environ['MONGO_DB_URL']=env_config['MONGO_DB_URL']

app=FastAPI()
origins=["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/",tags=["authetication"])
async def index():
    return RedirectResponse(url="docs")

@app.get("/train")
async def train_routes():
    try:
        train_pipeline=TrainPipeline()
        if train_pipeline.is_pipeline_running:
            return Response("Training pipeline is already running.")
        train_pipeline.run_pipeline()
        return Response("Training successfully !!")
    except Exception as e:
        return Response(f"Error Occured! {e}")

@app.post("/predict")
async def predict_route(request:Request,file:UploadFile=File(...)):
    try:
        df=pd.read_csv(file.file)
        schema_file=read_yaml_file(SCHEMA_FILE_PATH)
        df=df.drop(schema_file['drop_columns'],axis=1)
        for i in df.columns:
            df[i].replace({'na':np.nan},inplace=True)
            df[i]=df[i].astype(float)
            df[i].fillna(df[i].mean(),inplace=True)
        model_resolver=ModelResolver(model_dir=SAVED_MODEL_DIR)
        if not model_resolver.is_model_exists():
            return Response("Model not available")
        
        best_model_path=model_resolver.get_best_model_path()
        model=load_object(file_path=best_model_path)
        y_pred=model.predict(df)
        df['predicted_column']=y_pred
        df['predicted_column'].replace(TargetValueMapping().reverse_mapping(),inplace=True)
        #return df[['predicted_column']].to_html()
        stream = io.StringIO()
        df.to_csv(stream, index=False)
        response = StreamingResponse(
        iter([stream.getvalue()]), media_type="text/csv")
        response.headers["Content-Disposition"] = "attachment; filename=export.csv"
        return response
    except Exception as e:
        raise Response(f"Error Occured! {e}")

# def main():
#     try:
#         training_pipeline=TrainPipeline()
#         training_pipeline.run_pipeline()
#     except Exception as e:
#         raise SensorException(e,sys)

if __name__ == '__main__':
    #set_env_variable(env_file_path)
    # main()
    app_run(app,host=APP_HOST,port=APP_PORT)