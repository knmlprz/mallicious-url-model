from flask import Flask, request
from random import random

app = Flask(__name__)


@app.route("/", methods=["POST"])
def main():

    return {"sus": "good" if round(random()) == 1 else "bad"}
