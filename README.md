# Coding-Challenge
![Workflow](https://github.com/sujithshajee/coding-challenge/actions/workflows/flask.yml/badge.svg)
![Docker Image CI](https://github.com/sujithshajee/coding-challenge/workflows/Docker%20Image%20CI/badge.svg)
![Publish Docker image](https://github.com/sujithshajee/coding-challenge/workflows/Publish%20Docker%20image/badge.svg)

## Requirements
```python
pip install flask
```


## Requirements for Test, Coverage and Lint
```python
pip install pytest
pip install coverage
pip install pylint
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
docker build -t coding-challenge .
docker run -p 8080:8080 coding-challenge
```

## Build and run using docker-compose
```
docker-compose up
```

## Deploy the application in Kubernetes
```
helm install coding-challenge ./chart/coding-challenge
```

## Validate application with port-forward
```
kubectl port-forward <pod-name> 8081:8080
Once port forward is successful, browse http://localhost:8080

```

## Uninstall application in Kubernetes
```
helm uninstall coding-challenge 
```

## Configuration

The following table lists the configurable parameters of the Keycloak chart and their default values.

Parameter | Description | Default
--- | --- | ---
`image.repository` | image repository | `sujithshajee/coding-challenge`
`image.pullPolicy` | image pull policy | `IfNotPresent`
`image.tag` | image tag | `1.0`
`replicaCount` | replicaCount | `1`
`service.type` | service type | `ClusterIP`
`service.port` | service port | `8080`

Specify each parameter using the `--set key=value[,key=value]` argument to `helm install`.