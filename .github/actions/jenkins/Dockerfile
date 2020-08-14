# Container image that runs your code
FROM python:3.7

#install pre-requisites
RUN apt-get update # && apt-get install -y curl && apt-get -y install jq

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY entrypoint.py /entrypoint.py
COPY init.sh /init.sh

RUN chmod +x /init.sh
# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/init.sh"]
