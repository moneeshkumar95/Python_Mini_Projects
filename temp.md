# FastAPI Project

This is a FastAPI project that provides a basic setup for getting started with your application. Follow the steps below to set up and run the project.

## Prerequisites

Make sure you have the following prerequisites installed on your system:

- Python >=3.10

## Installation
### Move into projectAPIv1 directory

1. Update the package lists and upgrade the installed packages by running the following commands:

   ```shell
   sudo apt update
   sudo apt upgrade
   ```

2. Install the necessary dependencies for Python and MySQL development:

   ```shell
   sudo apt install python3-dev default-libmysqlclient-dev build-essential
   ```

3. Install the Python virtual environment package:

   ```shell
   sudo apt install python3-venv
   ```

4. Create a virtual environment for the project:

   ```shell
   python3 -m venv venv
   ```

5. Activate the virtual environment:

   ```shell
   source venv/bin/activate
   ```

6. Install the project dependencies by running the following command:

   ```shell
   pip3 install -r requirements/dev.txt
   ```
   Note: Install dependencies according on the environment

## Database Configuration

1. Open the `config/db_config.ini` file 
2. Update the configuration values for the multiple database connections:

   ```ini
   [tenant_name]  ### allcat, prestige
   host = <host>
   username = <username>
   password = <password>
   database = <database>
   port = <port>
   tenant = <tenant> ### tenant name or ID or UUID
   is_main = true

   [tenant_name]
   host = <host>
   username = <username>
   password = <password>
   database = <database>
   port = <port>
   tenant = <tenant>
   is_main = false

   ```

   Note: The `[db]` section can be name or Generated ID or UUID. Only include multiple DB sections If your using the multiple DB. Otherwise keep one DB section.
   

## Table Check

Ensure that all the required tables are present in their respective databases.

## Running the Application

To run the application, use the following command:

```shell
uvicorn main:app --reload
```

This command starts the application with auto-reload enabled. You can access the application at the provided URL.

```shell
http://127.0.0.1:8000
```

For swagger UI.

```shell
http://127.0.0.1:8000/docs
```

### Note: Pass the tenant & token in header for every endpoints ( login and register endpoints doesn't require token )


