#!/usr/bin/env python3

import os
import json

env = {}

for env_key, env_value in os.environ.items():
    env[env_key] = env_value

#print("Content-Type: application/json")
#print()

#print(json.dumps(env))
print("Content-Type: text/html\r\n")
print(env["QUERY_STRING"] + env["HTTP_USER_AGENT"])