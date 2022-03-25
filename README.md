# DRF-Inventory

DRF_Inventory is an implementation of imaginary store inventory that accepts orders. This project is a microservice-based web application that is implemented via Django Rest Framework.

How to setup:
1. Make sure you have Docker on your machine and all the necessary [requirements](https://github.com/Verdiyev/DRF-Inventory/blob/master/inventory/requirements.txt).
2. Clone the repo
3. Run the following command in the root directory (same as docker-compose.yaml):
  ```shell
  docker-compose build
  ```
  and then 
  ```shell
  docker-compose up
  ```
4. Go to your browser and check API in /api/ with port 8001 for inventory microservice and 8002 for reporting
