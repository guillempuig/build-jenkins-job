# Container image that runs your code
FROM python:3.7

#install pre-requisites
RUN apt-get update

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY entrypoint.py /entrypoint.py
COPY requirements.txt /requirements.txt

RUN chmod +x /entrypoint.py

WORKDIR /

RUN pip install -r requirements.txt

RUN echo $(ls -1)
# Code file to execute when the docker container starts up (`entrypoint.py`)
ENTRYPOINT ["/entrypoint.py"]
# ENTRYPOINT ["python", "entrypoint.py"]
