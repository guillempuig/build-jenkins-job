#!/bin/sh -l

url=$1
token=$2
user=$3
job_path=$4
echo "jenkins url $1"
echo "jenkins url ${url}"
echo "jenkins token $2"
echo "user $3"
echo "job path $4"

echo "http://$3:$4@"
echo "http://$3:$2@"
echo "http://$1:$2@"
jenkins_url="http://${user/$'\r'/}:${token/$'\r'/}@${url/$'\r'/}${job_path/$'\r'/}"
echo "$jenkins_url"
jenkins_url="${jenkins_url}/buildWithParameters?token=$2"
echo "$jenkins_url"

# output=$(curl -i -X  POST "$jenkins_url" | grep Location | tail -1 | sed 's/[^ ]* //')

echo "This is my output ${output}"

time=$(date)
echo "::set-output name=time::$time"