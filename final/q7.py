#!/usr/bin/env python
import pymongo

connection = pymongo.MongoClient("mongodb://mongo.loc")
db = connection.photo

try:

    images = db.images.find();
    for image in images:
        album = db.albums.find_one({"images": {'$in': [image['_id']]}})
        if (album == None):
            db.images.delete_one({'_id': image['_id']})

    count = db.images.find({ "tags": { '$in': ['kittens'] } }).count()

except Exception as e:
    print("Unexpected error:", type(e), e)

# 44822
print(count)