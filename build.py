#!/usr/bin/env python
from __future__ import print_function

import boto3
import os
import sys

def main():
    print("test")
    access = os.environ['AWS_ACCESS_KEY_ID']
    print("access: " + access)

if __name__ == "__main__":
    main()
