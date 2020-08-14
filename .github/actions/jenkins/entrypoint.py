#!/usr/bin/env python3

import sys
import requests
import jenkins

JENKINS_URL = sys.argv[1]
JENKINS_TOKEN = sys.argv[2]
JENKINS_USER = sys.argv[3]
JOB_PATH = sys.argv[4]

print(JENKINS_URL)
print(JENKINS_USER)
print(JENKINS_TOKEN)
print(JOB_PATH)

server = jenkins.Jenkins(JENKINS_USER, username=JENKINS_USER, password=JENKINS_TOKEN)
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))

url = "http://"+JENKINS_USER+":"+JENKINS_TOKEN+"@"+JENKINS_URL+JOB_PATH+"/buildWithParameters?token="+JENKINS_TOKEN
print(url)

x = requests.post(url, data={"QUEUE_TIMEOUT": "2"})
print(x)
print(x.status_code)
print(x.json())

