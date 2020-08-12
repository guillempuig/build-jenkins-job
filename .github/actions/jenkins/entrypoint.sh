#!/bin/sh -l

echo "jenkins url $1"
echo "jenkins token $2"
echo "user $3"
echo "job path $4"

IFS=$'\n'
# shellcheck disable=SC2027
protocol="http://$3:$2"
echo $protocol
jenkins_url="$protocol@$1$4"
echo "$jenkins_url"
jenkins_url="${jenkins_url}/buildWithParameters?token=$2"

echo "$jenkins_url"

output=$(curl -i -X  POST "$jenkins_url" | grep Location | tail -1 | sed 's/[^ ]* //')

echo "This is my output ${output}"

time=$(date)
echo "::set-output name=time::$time"