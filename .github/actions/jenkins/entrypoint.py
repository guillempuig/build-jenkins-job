#!/usr/bin/env python3

import sys
import requests
import jenkins
import time

JENKINS_URL = sys.argv[1]
JENKINS_TOKEN = sys.argv[2]
JENKINS_USER = sys.argv[3]
JOB_PATH = sys.argv[4]

print(JENKINS_URL)
print(JENKINS_USER)
print(JENKINS_TOKEN)
print(JOB_PATH)

server = jenkins.Jenkins("http://209.133.201.194:8080", username=JENKINS_USER, password=JENKINS_TOKEN)
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))

# jobs = server.get_jobs()
# print(jobs)
server.build_job('Fluid/fluid-controller-deploy', parameters={"QUEUE_TIMEOUT": "2"}, token=JENKINS_TOKEN)
queue_info = server.get_queue_info()
id = queue_info[0].get('id')

print(queue_info)
print(id)

url = f"http://{JENKINS_USER}:{JENKINS_TOKEN}@{JENKINS_URL}/queue/item/{id}/api/json?pretty=true"
print(url)
#
x = requests.get(url)
print(x)
print(x.status_code)

if "executable" not in x.json():
    time.sleep(10)
    x = requests.get(url)
    print(x.json())


# print()

