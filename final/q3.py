#!/usr/bin/env python
import pymongo

connection = pymongo.MongoClient("mongodb://mongo.loc")
collection = connection.enron.messages

try:
    collection.update_one(
        {'headers.Message-ID': '<8147308.1075851042335.JavaMail.evans@thyme>'},
        {'$push': {'headers.To': 'mrpotatohead@mongodb.com'}}
    )

except Exception as e:
    print("Unexpected error:", type(e), e)
