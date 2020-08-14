#!/usr/bin/python
import sys

print("inside script")


def greed():
    print("hello")


greed()
print(sys.argv[0])
print(len(sys.argv))
print(str(sys.argv))
