from flask import Flask, render_template
from flask import request
from pymongo import MongoClient

RECIEVED_LOGS_FILE='/var/recieved_logs/'

app = Flask(__name__)

client = MongoClient('mongo', 27017,username="root", password="example")
db = client.test_database
raw_logs = db.raw_logs

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_log', methods=["POST"])
def capture_log():
    print("Recieved log...")
    raw_log = {"log_text": request.data }
    raw_log_id = raw_logs.insert_one(raw_log).inserted_id
    #with open(RECIEVED_LOGS_FILE, 'a') as f:
    #    f.write(request.data)
    #return "Captured"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)


