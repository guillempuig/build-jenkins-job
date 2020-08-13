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
echo "$url"
echo "${protocol%$'\r'}"
protocol+=$url
echo "$protocol"



# output=$(curl -i -X  POST "${url}" | grep Location | tail -1 | sed 's/[^ ]* //')

echo "This is my output ${output}"

time=$(date)
echo "::set-output name=time::$time"