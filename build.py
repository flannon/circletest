#!/usr/bin/env python
from __future__ import print_function

import boto3
import os
import sys

def main():
    print("test")
    access = os.environ['AWS_ACCESS_KEY_ID']
    print("access: " + access)
    ami_instance_profile = os.environ['AMI_INSTANCE_PROFILE']
    print("ami_instance_profile: " + ami_instance_profile)

if __name__ == "__main__":
    main()
