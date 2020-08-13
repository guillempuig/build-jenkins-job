#!/bin/bash


JENKINS_URL=$1
JENKINS_TOKEN=$2
JENKINS_USER=$3
JOB_PATH=$4

echo "jenkins url $JENKINS_URL"
echo "jenkins token $JENKINS_TOKEN"
echo "user $JENKINS_USER"
echo "job path $JOB_PATH"

url="$JENKINS_USER:$JENKINS_TOKEN@$JENKINS_URL$JOB_PATH/buildWithParameters?token=$JENKINS_TOKEN"
protocol="http://"

protocol+="$url"
echo "${protocol}"

BRANCH_NAME="ASAJDA"

output=$(curl -i -X  POST "$protocol" \
   --data "BRANCH_NAME=${BRANCH_NAME}" \
     | grep Location | tail -1 | sed 's/[^ ]* //')
#
echo "This is my output ${output}"

build_number=$(curl -X GET http://${JENKINS_USER}:${JENKINS_TOKEN}@209.133.201.194:8080/queue/item/1225/api/json?pretty=true | jq '.executable.number')
echo "This is my build number ${build_number}"

status=$(curl -X GET http://${JENKINS_USER}:${JENKINS_TOKEN}@209.133.201.194:8080/job/Fluid/job/fluid-deploy-service/${build_number}/api/json?petty=true | jq '.result')
echo "This is my build status ${status}"

#
#time=$(date)
#echo "::set-output name=time::$time"

