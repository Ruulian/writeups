#!/usr/bin/python

import requests

if requests.get('http://localhost:2156').status_code == 200:
  exit(0)
else:
  exit(1)
