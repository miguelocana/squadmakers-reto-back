# Squadmasters API test

## Setup 
To set up this project, follow these steps:

1. Install Python 3.6 or higher.
2. Clone this repository to your local machine and go to the project directory.
```bash
git clone https://github.com/miguelocana/squadmasters-test.git
cd squadmasters-test
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
4. Access the web API by visiting http://localhost:8000/swagger/ in your web browser.


### OPTION 2 - Docker setup
To run this project using Docker, follow these steps:

1. Install Docker and Docker Compose.

2. Build the Docker image and start the containers::
```bash
docker-compose up --build
```
3. Access the web application by visiting http://localhost:8000/swagger/ in your web browser.

The Docker container will automatically set up the environment and dependencies for the project. Any changes to the code will be reflected in the running container immediately.

# Conclusion
That's it! You now know how to set up and run this Django project manually or using Docker. Enjoy!