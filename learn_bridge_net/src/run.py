from pymongo import MongoClient

from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    conn = MongoClient("mongo", 27017)
    conn["learn_docker"]["test"].insert_one({
        "name": "docker test",
        "pw": "123456789"
    })
    return "Hello World!"


@app.route("/home")
def home():
    return "weblcome to docker"


if __name__ == "__main__":
    app.run()