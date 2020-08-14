#!/usr/bin/env python3

# use of https://python-jenkins.readthedocs.io/en/latest/index.html

import sys
import requests
import jenkins
import time

JENKINS_URL = sys.argv[1]
JENKINS_TOKEN = sys.argv[2]
JENKINS_USER = sys.argv[3]
JOB_PATH = sys.argv[4]

# create/connect jenkins server
server = jenkins.Jenkins(f"http://{JENKINS_URL}", username=JENKINS_USER, password=JENKINS_TOKEN)
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))

# build job
server.build_job('Fluid/fluid-controller-deploy', parameters={"QUEUE_TIMEOUT": "2"}, token=JENKINS_TOKEN)
queue_info = server.get_queue_info()
queue_id = queue_info[0].get('id')

# define url to request build_number
url = f"http://{JENKINS_USER}:{JENKINS_TOKEN}@{JENKINS_URL}/queue/item/{queue_id}/api/json?pretty=true"


def get_trigger_info(url: str):
    trigger_info = requests.get(url).json()
    return trigger_info


while "executable" not in (info := get_trigger_info(url)):
    time.sleep(3)

build_number = info["executable"]["number"]
print(build_number)


def get_status(job_name: str, build_number: int) -> str:
    build_info = server.get_build_info(name=job_name, number=build_number)
    job_status = build_info["result"]
    return job_status


while not (status := get_status('Fluid/fluid-controller-deploy', build_number)):
    time.sleep(1)

print(f"Job status is : {status}")
print(f"::set-output name=myOutput::{status}")
