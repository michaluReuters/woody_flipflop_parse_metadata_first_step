# woody_flipflop_parse_metadata_first_step

This repository represents first step in gathering, extracting and
updating metadata in sonyhive api platform. Inputs might be coming 
from many sources so the key to the overhaul flow is to be adaptive.

## Installation
This repository i just a representation of Lambda function stored in
company AWS account. Every test shoudl be run in AWS and be verified
in CloudWatch. Main function and a starting point of this step starts
with lambda.py, and it's handler() 

## Usage

### High level overview
Below we present high level overview of the algorithm for the first
step.

<div align="center">
  <img src="./images/first_step.png" alt="First step flow">
</div>

First step is really simple, it's purpose is to gather file name
and id from incoming SNS message

### Important configuration and environment variables

For this step there are no important config and variables