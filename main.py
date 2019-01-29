#!/usr/bin/env python3

import requests
import csv
import json
import os

with open("/data/config.json","r") as conf_file:
    conf = json.load(conf_file)["parameters"]

endpoint = "https://{0}.talon.one/v1/applications/{1}/campaigns/{2}/import_coupons".format(conf["project"], conf["application-id"], conf["campaign-id"])
headers = {"authorization":"Bearer {0}".format(conf["#bearer"])}

if not os.path.exists("/data/config.json"):
    raise Exception ("Missed configuration parametrs: project, application-id, campaign-id, bearer")

if not os.path.exists("/data/in/tables/input.csv"):
    raise Exception("Input table must be named \"input.csv\"")

files = {'file': open("/data/in/tables/input.csv", "rb")}

r1 = requests.post(endpoint,headers=headers,files=files)

if r1.status_code != 200:
    raise Exception("ERROR:",r2.status_code, r2.text)

