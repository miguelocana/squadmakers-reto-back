# Squadmasters API test
Hello! This is a Django project that implements a web API for generate jokes and calculate math operations.

The service generate automatically a view to [Swagger UI](https://swagger.io/), where you can test the API.

## Setup 
To set up this project, follow these steps:

1. Install Python 3.6 or higher.
2. Clone this repository to your local machine and go to the project directory.
```bash
git clone https://github.com/miguelocana/squadmakers-reto-back.git
cd squadmakers-reto-back
```

From here, you can either set up the project manually or using Docker.

### OPTION 1 - Manual setup
To run this project manually, follow these steps:

1. Install the required Python packages using pip:
```bash
pip install -r requirements.txt
```
2. Set up the database:
```bash
python manage.py migrate
```
3. Start the development server:
```bash
python manage.py runserver
```

### OPTION 2 - Docker setup
To run this project using Docker, follow these steps:

1. Install Docker and Docker Compose.

2. Build the Docker image and start the containers::
```bash
docker compose up --build
```

The Docker container will automatically set up the environment and dependencies for the project. Any changes to the code will be reflected in the running container immediately.

## Swagger UI
You're all set up to access to the API documentation by visiting http://localhost:8000/swagger/ in your web browser. Additionally, you'll find a `swagger.yaml` file in the root directory of the project.
## Tests
Tests are implemented using [pytest](https://docs.pytest.org/en/stable/). Run this command:
```bash
docker compose run test
```
You'll see the results in the terminal.

