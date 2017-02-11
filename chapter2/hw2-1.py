#!/usr/bin/env python
import pymongo

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://mongo.loc")

# get a handle to the school database
db = connection.students
grades = db.grades


query = {'type': 'exam', 'score': {'$gte': 65}}

try:
    doc = grades.find(query)
    doc.sort('score', pymongo.ASCENDING)
    doc.limit(1)

except Exception as e:
    print("Unexpected error:", type(e), e)

# 22
print(doc[0]['student_id'])

