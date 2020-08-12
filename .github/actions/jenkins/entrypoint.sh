#!/bin/sh -l

echo "jenkins url $1"
echo "jenkins token $2"
echo "job path $3"
time=$(date)
echo "::set-output name=time::$time"