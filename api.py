from flask import Flask, request
from random import random
from model import Model
import json

app = Flask(__name__)
model = Model()


@app.route("/", methods=["POST"])
def main():
    domain = request.get_json(force=True)["domain"]
    return {"sus": model.predict(domain)}
