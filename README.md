# Coding-Challenge
## Requirements


```bash
pip install flask
pip install pytest
pip install coverage
```

## Run Tests

```python
python -m pytest
```

## Run Tests with Coverage and Generate Report
```python
python -m coverage run --source app -m pytest
python -m coverage report
```

## Build and run using docker
```
docker build -t flask-app .
docker run -p 8080:8080 flask-app
```

## Build and run using docker-compose
```
docker-compose up
```