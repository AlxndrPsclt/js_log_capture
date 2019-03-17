
from bson.objectid import ObjectId

import pprint


from pymongo import MongoClient

client = MongoClient('mongo', 27017,username="root", password="example")
db = client.test_database
raw_logs = db.raw_logs

def find_by_id(id):
    document = raw_logs.find_one({'_id': ObjectId(id)})
    pprint.pprint(document)
    #document = client.db.collection.find_one({'_id': ObjectId(post_id)})

all_logs = raw_logs.find()

print('\n All logs from raw_logs Database \n')
for log_elt in all_logs:
    pprint.pprint(log_elt['log_text'])

#with open(RECIEVED_LOGS_FILE, 'a') as f:
#    f.write(request.data)
#return "Captured"

