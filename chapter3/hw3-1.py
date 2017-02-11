#!/usr/bin/env python
import pymongo

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://mongo.loc")

# get a handle to the school database
db = connection.school
students = db.students

# find lowest score from collection of scores
# maximum score can be 999
def find_lowest_score(scores):
    lowest_score = {'score': 999}

    for score in scores:
        if (score['type'] == 'homework' and score['score'] < lowest_score['score']):
            lowest_score = score

    return lowest_score

try:
    cursor = students.find()
    for student in cursor:
        student_scores = student['scores']
        lowest_score = find_lowest_score(student_scores)
        student_scores.remove(lowest_score)

        students.update_one(
            {'_id': student['_id']},
            {'$set': {'scores': student_scores}}
        )

    doc = students.aggregate([
        {'$unwind': '$scores'},
        {'$group': {'_id': '$_id', 'average': {'$avg': '$scores.score'}}},
        {'$sort': {'average': -1}},
        {'$limit': 1}
    ])

except Exception as e:
    print("Unexpected error:", type(e), e)


# 13
print(list(doc)[0]['_id'])

