#!/usr/bin/env python3

import requests
import csv
import json
import os

conf_path = ("/data/config.json" if os.path.exists("/data/config.json") else ("/code/config.json" if os.path.exists("/code/config.json") else "config.json"))


if (not os.path.exists(conf_path)):
	print("Cannot run without configuration")
	sys.exit(0)

with open("/data/config.json","r") as conf_file:
    conf = json.load(conf_file)["parameters"]

print(conf.keys())

endpoint = "https://{0}.talon.one/v1/applications/{1}/campaigns/{2}/import_coupons".format(conf["project"], conf["application-id"], conf["campaign-id"])
headers = {"authorization":"Bearer {0}".format(conf["#bearer"])}

if not os.path.exists("/data/in/tables/input.csv"):
    raise Exception("Input table must be named \"input.csv\"")

files = {'file': open("/data/in/tables/input.csv", "rb")}

r1 = requests.post(endpoint,headers=headers,files=files)

if r1.status_code != 200:
    raise Exception("ERROR:",r1.status_code, r1.text)

