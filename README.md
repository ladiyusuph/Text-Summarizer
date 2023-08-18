# End to end Text-Summarizer Project

## Workflow

1. Update config.yaml
2. Update params.yaml
3. Update entity
4. Update the configuration manager in src config
5. update the conponents
6. update the pipeline
7. update the main.py
8. update the app.py


# How to run the app ?
### STEPS:

### Clone the repository

```bash
https://github.com/ladiyusuph/Text-Summarizer
```
### STEP 1- Create a conda environment after opening the repository

```bash
conda create -n txt_sum python=3.8 -y
```

```bash
conda activate txt_sum
```


### STEP 2- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Run the app with the following command
python app.py
```

Now,
```bash
open up you local host and port
```


```bash
Author: Ladi Yusuph

```
# AWS-CICD-Deployment-with-Github-Actions

### Step 1: Login to AWS console.

### Step 2: Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
### Step 3: Create ECR repo to store/save docker image
    - Save the URI: 379434898136.dkr.ecr.us-east-1.amazonaws.com/text_summarizer

	
## Step 4: Create EC2 machine (Ubuntu) 

## Step 5: Open EC2 and Install docker in EC2 Machine
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# Step 6: Configure EC2 as self-hosted runner


# Step 7: Setup github secrets

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION =

    AWS_ECR_LOGIN_URL = 

    ECR_REPOSITORY_NAME = 