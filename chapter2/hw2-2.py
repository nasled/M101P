#!/usr/bin/env python
import pymongo

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://mongo.loc")

# get a handle to the school database
db = connection.students
grades = db.grades


try:
    cursor = grades.aggregate([
        {'$match': {'type': 'homework'}},
        {'$group': {'_id': '$student_id', 'score': {'$min': '$score'}}}
        #,{'$count': 'passing_scores'}
    ])

    for doc in cursor:
        grades.remove({'student_id': doc['_id'], 'type': 'homework', 'score': doc['score']})

    doc = grades.aggregate([
        {'$group': {'_id': '$student_id', 'average': { '$avg': '$score'}}},
        {'$sort': {'average': -1}},
        {'$limit': 1}
    ])

except Exception as e:
    print("Unexpected error:", type(e), e)

# 54
print(list(doc)[0]['_id'])

