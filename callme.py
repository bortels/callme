#!/usr/bin/env python
from flask import Flask, request, json, jsonify
import redis
import os
import re

# Get redis connect info from docker, if any
m = re.match(r"tcp://(.*):(\d+)$", os.getenv('REDIS_PORT', 'tcp://localhost:6379'))
red = redis.StrictRedis(host=m.group(1), port=m.group(2), db=0)

app = Flask(__name__)

@app.route("/")
def hello():
    return "Callme API v0.1"

@app.route("/event", methods=['POST'])
def post_event():
  data = request.get_json(force=True)
  return jsonify(status="OK")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
