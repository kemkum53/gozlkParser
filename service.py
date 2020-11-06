from flask import Flask, request, jsonify
from gzlkParser import get_meanings

app = Flask(__name__)

@app.route("/search/<data>", methods = ["POST"])
def search(data):
    if request.method == "POST":
        return jsonify(get_meanings(data))
if __name__ == "__main__":
    app.run(debug = False)