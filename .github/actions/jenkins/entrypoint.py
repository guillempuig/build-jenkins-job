#!/usr/bin/python
import sys

print("inside script")


def greed():
    print("hello")


greed()
print(f"This is the name of the script: {sys.argv[0]}")
print(f"Number of arguments: {len(sys.argv)}")
print(f"The arguments are:  {str(sys.argv)}")
