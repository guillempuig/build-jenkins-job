#!/bin/sh -l

echo "jenkins url $1"
echo "jenkins token $2"
echo "user $3"
echo "job path $4"
# shellcheck disable=SC2027
jenkins_url="$3:$2@$1$4/buildWithParameters?token=$2"
echo "$jenkins_url"
time=$(date)
echo "::set-output name=time::$time"