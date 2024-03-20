****Flask API Deployment with Azure and Docker****

**Overview**

This project aims to create a Flask API that displays a cricketer's team when their name is input. The project utilizes Docker for containerization and Azure services for deployment, specifically Azure Container Registry and Azure Container Instances.

**Project Components**

Flask API

> Developed a Flask API (app.py) capable of displaying cricketer teams based on input.
> Utilized Flask's lightweight and flexible framework for rapid development

Docker Containerization

> Dockerized the Flask API using a Dockerfile, ensuring consistency across different environments
> Built and tested the Docker image locally to ensure functionality (sudo docker build -t cricketerapi-image .)

**Azure Deployment**

1. Azure Container Registry Setup:

   > Created an Azure Container Registry named cricketaustralia in the East US region.
   > Logged into the Azure Container Registry using Docker login.

2. Docker Image Push:

   > Tagged the Docker image (cricketapi-image) with the Azure Container Registry address.
   > Pushed the tagged Docker image to Azure Container Registry (sudo docker push cricketaustralia.azurecr.io/cricketapi-image:latest)

3. Azure Container Instance Creation:

   > Created an Azure Container Instance named icc within the resource group RG-Crick.
   > Specified the Docker image from Azure Container Registry for deployment.
   > Configured ports (5000) for external access

**Project Execution**

1. Local Testing

   > Successfully tested the Flask API functionality locally using Docker (sudo docker run -p 5000:5000 -it cricketapi-image).
   > Verified functionality by accessing endpoints through browser and curl

2. Azure Deployment:

   > Deployed the Docker image to Azure Container Instance, ensuring seamless integration with Azure Container Registry.
   > Accessed the deployed Flask API using the provided Fully Qualified Domain Name (FQDN) and tested functionality.

