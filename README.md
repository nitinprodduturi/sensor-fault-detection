# Sensor-Fault-Detection

### Problem Statement
The Air Pressure System (APS) is a critical component of a heavy-duty vehicle that uses compressed air to force a piston to provide pressure to the brake pads, slowing the vehicle down. The benefits of using an APS instead of a hydraulic system are the easy availability and long-term sustainability of natural air.

This is a Binary Classification problem, in which the affirmative class indicates that the failure was caused by a certain component of the APS, while the negative class
indicates that the failure was caused by something else.

### Solution Proposed 
In this project, the system in focus is the Air Pressure system (APS) which generates pressurized air that are utilized in various functions in a truck, such as braking and gear changes. The datasets positive class corresponds to component failures for a specific component of the APS system. The negative class corresponds to trucks with failures for components not related to the APS system.

The problem is to reduce the cost due to unnecessary repairs. So it is required to minimize the false predictions.
## Tech Stack Used
1. Python 
2. FastAPI 
3. Machine learning algorithms
4. Docker
5. MongoDB

## Infrastructure Required.

1. AWS S3
2. AWS EC2
3. AWS ECR
4. Git Actions
5. Terraform

## How to run?
Before we run the project, make sure that you are having MongoDB in your local system, with Compass since we are using MongoDB for data storage. You also need AWS account to access the service like S3, ECR and EC2 instances.

## Data Collections
![image]()


## Project Archietecture
![image]()


## Deployment Archietecture
![image]()


### Step 1: Clone the repository
```bash
git clone https://github.com/nitinprodduturi/sensor-fault-detection.git
```

### Step 2- Create a conda environment after opening the repository

```bash
conda create -n sensor-venv python=3.8 -y
```

```bash
conda activate sensor-venv
```

### Step 3 - Install the requirements
```bash
pip install -r requirements.txt
```

### Step 4 - Export the environment variable
```bash
export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>

export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>

export AWS_DEFAULT_REGION=<AWS_DEFAULT_REGION>

export MONGODB_URL="mongodb+srv://nitinprodduturi15:s9kWaVkxY4viAP0E@cluster0.uodlfhv.mongodb.net/?retryWrites=true&w=majority"

```

### Step 5 - Run the application server
```bash
python app.py
```

### Step 6. Train application
```bash
http://localhost:8080/train

```

### Step 7. Prediction application
```bash
http://localhost:8080/predict

```

## Run locally

1. Check if the Dockerfile is available in the project directory

2. Build the Docker image
```
docker build --build-arg AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID> --build-arg AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY> --build-arg AWS_DEFAULT_REGION=<AWS_DEFAULT_REGION> --build-arg MONGODB_URL=<MONGODB_URL> . 

```

3. Run the Docker image
```
docker run -d -p 8080:8080 <IMAGE_NAME>
```

To run the project  first execute the below commmand.
MONGO DB URL: 
```
mongodb+srv://nitinprodduturi15:s9kWaVkxY4viAP0E@cluster0.uodlfhv.mongodb.net/?retryWrites=true&w=majority
```
windows user

```
MONGO_DB_URL= mongodb+srv://nitinprodduturi15:s9kWaVkxY4viAP0E@cluster0.uodlfhv.mongodb.net/?retryWrites=true&w=majority
```

Linux user

```
export MONGO_DB_URL= mongodb+srv://nitinprodduturi15:s9kWaVkxY4viAP0E@cluster0.uodlfhv.mongodb.net/?retryWrites=true&w=majority
```

then run 
```
python main.py
```