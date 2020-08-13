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

BRANCH_NAME=""

queue_url=$(curl -i -X  POST "$protocol" \
   --data "BRANCH_NAME=${BRANCH_NAME}" \
     | grep Location | tail -1 | sed 's/[^ ]* //')
#
echo "Queue location: ${queue_url}"

queue_item=$(echo "${queue_url}" | grep -Po '[\/](\d{4})[\/]')
queue_number=${queue_item///}
echo "Job in queue with number: $queue_number"

build_number=$(curl --silent --output -X GET $JENKINS_URL/queue/item/$queue_number/api/json?pretty=true | jq '.executable.number')

requests=0
echo "build_number is: "$build_number
while [ "$build_number" == "" ] &&  [ $requests -lt 5 ]; do
  sleep 2
  build_number=$(curl --silent --output -X GET $JENKINS_URL/queue/item/$queue_number/api/json?pretty=true | jq '.executable.number')
  requests=$((requests+1))
  echo "Job still in queue..."
done


status=$(curl --silent --output -X GET $JENKINS_URL/job/Fluid/job/fluid-controller-deploy/${build_number}/api/json?petty=true | jq '.result')
echo $status

if [ $status == "" ]
then
  echo "void"
fi
#while [ "$status" == "" ]; do
#    sleep 1
#    echo "Job running..."
#    status=$(curl --silent --output -X GET $JENKINS_URL/job/Fluid/job/fluid-controller-deploy/${build_number}/api/json?petty=true | jq '.result')
#done
#echo "Job finished. Build status: ${status}"

#
#time=$(date)
#echo "::set-output name=time::$time"

