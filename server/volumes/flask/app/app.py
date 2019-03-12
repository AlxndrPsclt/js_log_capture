from flask import Flask, render_template
from flask import request
from pymongo import MongoClient


app = Flask(__name__)

client = MongoClient('mongo', 27017,username="root", password="example")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_log', methods=["POST"])
def capture_log():
    print(request.data)
    return "Captured"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)


