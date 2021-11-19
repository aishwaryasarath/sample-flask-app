# Dockerfile

# inherit from this "empty base image", see https://hub.docker.com/_/python/
FROM python:3.9-alpine

RUN addgroup -g 9000 -S appgroup && adduser -u 9000 -S appuser -G appgroup

# take some responsibility for this container
LABEL Sujith Shajee <sujith.shajee@gmail.com>

# directory to install the app inside the container
WORKDIR /usr/src/app

# install python dependencies, this will be cached if the requirements.txt file does not change
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# copy application source code into container
COPY app.py .

# drop root privileges when running the application
USER appuser

# run this command at run-time
CMD [ "python", "app.py" ]

# expose this TCP-port
EXPOSE 8080