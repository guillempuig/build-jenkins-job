#!/bin/sh


JENKINS_TOKEN=$2
JENKINS_USER=$3
JENKINS_URL=$1
JOB_PATH=$4

echo "jenkins url $JENKINS_URL"
echo "jenkins token $JENKINS_TOKEN"
echo "user $JENKINS_USER"
echo "job path $JOB_PATH"

url="$JENKINS_USER:$JENKINS_TOKEN@$JENKINS_URL$JOB_PATH/buildWithParameters?token=$JENKINS_TOKEN"
protocol="http://"
#protocol="http://"
echo "$protocol$url"
echo "${protocol%$'\r'}$url"
#jenkins_url="http://${user}:${token}@${url}${job_path}"
#echo "$jenkins_url"
#jenkins_url="${jenkins_url}/buildWithParameters?token=$2"
#echo "$jenkins_url"

# output=$(curl -i -X  POST "$jenkins_url" | grep Location | tail -1 | sed 's/[^ ]* //')

echo "This is my output ${output}"

time=$(date)
echo "::set-output name=time::$time"