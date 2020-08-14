# Container image that runs your code
FROM python:3.7

#install pre-requisites
RUN apt-get update && apt-get install -y curl && apt-get -y install jq

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY entrypoint.py /entrypoint.py

RUN chmod +x /entrypoint.py
# Code file to execute when the docker container starts up (`entrypoint.sh`)
CMD ["/entrypoint.py"]
ENTRYPOINT ["python"]
