#!/usr/bin/env python
import pymongo

connection = pymongo.MongoClient("mongodb://mongo.loc")
db = connection.store
products = db.products


def _finditem(obj, key):
    if key in obj:
        return obj[key]

    for k, v in obj.items():
        if isinstance(v,dict):
            item = _finditem(v, key)

            if item is not None:
                return item

try:
    doc1 = products.find({'brand': 'GE'}).explain()
    doc2 = products.find({'brand': 'GE'}).sort('price', pymongo.ASCENDING).explain()
    doc3 = products.find({'$and': [{'price': {'$gt': 30}}, {'price': {'$lt': 50}}]}).sort('brand', pymongo.ASCENDING).explain()
    doc4 = products.find({'brand': 'GE'}).sort([('category', pymongo.ASCENDING), ('brand', pymongo.DESCENDING)]).explain()

except Exception as e:
    print("Unexpected error:", type(e), e)

# Find utilizing index in queries...
# 1st query index:  None
# 2nd query index:  price_1
# 3rd query index:  price_1
# 4th query index:  None

print("Find utilizing index in queries...")
print('1st query index: ', _finditem(doc1, 'indexName'))
print('2nd query index: ', _finditem(doc2, 'indexName'))
print('3rd query index: ', _finditem(doc2, 'indexName'))
print('4th query index: ', _finditem(doc4, 'indexName'))

