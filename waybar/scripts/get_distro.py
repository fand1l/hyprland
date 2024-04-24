#!/usr/bin/env python3

import requests
import json


url = "http://127.0.0.1:1530/get_distro_icon"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data['text'])
else:
    print("err")

