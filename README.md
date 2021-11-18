# coding-challenge
```
Requirements
```
python3
flask

```
Run Tests
```
python -m pytest

```
Run Tests with Coverage and Generate Report
```
python -m coverage run --source app -m pytest
python -m coverage report

```
Build and run using docker
```
docker build -t flask-app .
docker run -p 8080:8080 flask-app

```
Build and run using docker-compose
```
docker-compose up

```
Application can be accessed at URL http://<hostname>:8080/
```