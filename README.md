#        ****Flask API Deployment with _Azure and Docker_****



##    **Overview**

This project aims to create a Flask API that displays a cricketer's team when their name is input. The project utilizes Docker for containerization and Azure services for deployment, specifically Azure Container Registry and Azure Container Instances.

### **Project Components**

Flask API

- Developed a Flask API (app.py) capable of displaying cricketer teams based on input.
- Utilized Flask's lightweight and flexible framework for rapid development

Docker Containerization

- Dockerized the Flask API using a Dockerfile, ensuring consistency across different environments
- Built and tested the Docker image locally to ensure functionality (sudo docker build -t cricketerapi-image .)

**Azure Deployment**

1. Azure Container Registry Setup:

   - Created an Azure Container Registry named cricketaustralia in the East US region.

![container registry](https://github.com/Shahanaz-M-Meera/Flask-api-cricketteam/assets/163439731/7827f883-1629-4ee6-9dcd-0da43f4aa8eb)


   - Logged into the Azure Container Registry using Docker login.

1. Docker Image Push:

   - Tagged the Docker image (cricketapi-image) with the Azure Container Registry address.

             `sudo docker tag cricketapi-image cricketaustralia.azurecr.io/cricketapi-image:latest`

   - Pushed the tagged Docker image to Azure Container Registry

             `sudo docker push cricketaustralia.azurecr.io/cricketapi-image:latest`

             ``The push refers to repository [cricketaustralia.azurecr.io/cricketapi-image]
                fb346f227eb2: Pushed 
                22106a1af9fe: Pushed 
                da7662160602: Pushed 
                0dbb6d5260db: Pushed 
                4a7ac3585b06: Pushed 
                6be461d39d4d: Pushed 
                d91aa0e727e2: Pushed 
                c8f253aef560: Pushed 
                a483da8ab3e9: Pushed 
             latest: digest: sha256:0125d42da055fa8978ae1bbc06c626ae23f037f2cf402e6bef6dce2ace6cf999 size: 2202`
`
1. Azure Container Instance Creation:

   - Created an Azure Container Instance named icc within the resource group RG-Crick.

![container instance today](https://github.com/Shahanaz-M-Meera/Flask-api-cricketteam/assets/163439731/35c7c926-4cb9-4133-9175-752c90f815a0)


   - Specified the Docker image from Azure Container Registry for deployment.
   - Configured ports (5000) for external access

**Project Execution**

1. Local Testing

   - Successfully tested the Flask API functionality locally using Docker (sudo docker run -p 5000:5000 -it cricketapi-image).

            `Serving Flask app 'app'
                   Debug mode: on
                   WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
                   Running on all addresses (0.0.0.0)
                   Running on http://127.0.0.1:5000
                   Running on http://172.17.0.2:5000
                   Press CTRL+C to quit`

   - Verified functionality by accessing endpoints through browser and curl

`     ``:~# curl http://localhost:5000/cricketer-team?name=Shane%20Bond`

        {
          "name": "Shane Bond",
          "team": "New Zealand"
        }``

![testing locally](https://github.com/Shahanaz-M-Meera/Flask-api-cricketteam/assets/163439731/7824d91b-69a5-482d-b685-44ec36b897b3)



2. Azure Deployment:

   - Deployed the Docker image to Azure Container Instance, ensuring seamless integration with Azure Container Registry.

  ![repo](https://github.com/Shahanaz-M-Meera/Flask-api-cricketteam/assets/163439731/272616e1-25e7-452b-aed1-eec79b23f790)

![repo 1](https://github.com/Shahanaz-M-Meera/Flask-api-cricketteam/assets/163439731/2f38d25d-6f07-466c-96e5-45a2dc5d15b3)

   - Accessed the deployed Flask API using the provided Fully Qualified Domain Name (FQDN) and tested functionality.

![container instance today](https://github.com/Shahanaz-M-Meera/Flask-api-cricketteam/assets/163439731/6076397c-27bb-4628-bd3d-f9b79e0ff375)

![container instance testing](https://github.com/Shahanaz-M-Meera/Flask-api-cricketteam/assets/163439731/36413514-9c93-44c2-acfe-9b74d5e119b5)

![testing 2](https://github.com/Shahanaz-M-Meera/Flask-api-cricketteam/assets/163439731/d3d5edde-e032-404d-892d-fb9ec5afec8d)

## How To Use

1. Clone Repository:

   `git clone https://github.com/Shahanaz-M-Meera/Flask-api-cricketteam.git`

2. Setup Docker Environment
3. Run Docker Container Locally:

   `sudo docker run -p 5000:5000 -it cricketapi-image`
   
5. Access API Endpoints:

   -  Open a browser and visit http://localhost:5000/cricketer-team?name=Ricky%20Ponting

## Conclusion

Through the effective utilization of Docker and Azure services, the project achieved successful deployment of a Flask API for displaying cricketer teams. The integration of Docker for containerization and Azure for deployment provided scalability, reliability, and ease of management.
