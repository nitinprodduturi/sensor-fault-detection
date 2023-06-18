import os,sys
from sensor.exception import SensorException
from sensor.logger import logging
from sensor.utils.main_utils import read_yaml_file
from sensor.pipeline.training_pipeline import TrainPipeline

env_file_path=os.path.join(os.getcwd(),'env.yaml')

def set_env_variable(env_file_path):

    if os.getenv('MONGO_DB_URL',None) is None:
        env_config=read_yaml_file(env_file_path)
        os.environ['MONGO_DB_URL']=env_config['MONGO_DB_URL']

def main():
    try:
        training_pipeline=TrainPipeline()
        training_pipeline.run_pipeline()
    except Exception as e:
        raise SensorException(e,sys)

if __name__ == '__main__':
    set_env_variable(env_file_path)
    main()