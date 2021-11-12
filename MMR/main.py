#!/usr/bin/env python3
import json
import sys
from classes.database import Database
from classes.azur import AzurClient
from classes.handler import RequestHandler

from flask import Flask, request


if len(sys.argv) != 4:
    sys.exit("Usage: python main.py [database] [subscription_key] [environment]")
with open(sys.argv[1]) as f:
    database_info = json.load(f)

client = AzurClient(
    subscription_key = sys.argv[2],
    environment = sys.argv[3].upper()
)
database = Database(
    host = database_info["host"],
    database = database_info["database"],
    user = database_info["user"],
    password = database_info["password"]
)

app = Flask(__name__)
@app.route('/', methods = ["POST"])

def result():
    global client
    global database
    handler = RequestHandler(client, database)
    result = handler.handle_request(request)

    if result < 0:
        if result == -1:
            return "Number not found in image"
        elif result == -2:
            return "Invalid image"
        else:
            return "Negative delta value found with user id " + str(result / -3) 
    else:
        return "Image received"
        

app.run(host = "0.0.0.0", port = 5000)