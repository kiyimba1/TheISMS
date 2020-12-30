#!/usr/bin/env python

import json
import os
import pipes


# file = open("env.json", "r")
# with open("env.json", "r") as f:
#     file = f.read()

# def setup(file="env.json"):
#
#
#     file = open(file, "r")
#     print("========================================================")
#     print("Reading environment variables from " + file.name)
#     for key, value in json.load(file).items():
#         key = pipes.quote(key)
#         value = pipes.quote(value)
#         os.environ[str(key)] = str(value)
#         print(key + " : " + value)
# setup()

import nexmo

client = nexmo.Client(key='95c59113', secret='CQn3Af37lHxnTnU3')

client.send_message({
    'from': 'ISMS',
    'to': '256753389506',
    'text': 'Hello from ISMS SMS FEATURE',
})
