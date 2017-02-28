use test;
db.stuff.drop();

db.stuff.createIndex({'a': 1, 'b': 1}, {name: 'a_1_b_1'});
db.stuff.createIndex({'a': 1, 'c': 1}, {name: 'a_1_c_1'});
db.stuff.createIndex({'c': 1}, {name: 'c_1'});
db.stuff.createIndex({'a': 1, 'b': 1, 'c': -1}, {name: 'a_1_b_1_c_-1'});

for (i = 0; i < 10000; i++) {
    record = {
        'a': NumberInt(i),
        'b': NumberInt(i),
        'c': NumberInt(i)
    }

    db.stuff.insert(record);
}

planner = db.stuff.find({'a':{'$lt':10000}, 'b':{'$gt': 5000}}, {'a':1, 'c':1}).sort({'c':-1}).explain()['queryPlanner']


//c_1
//a_1_b_1_c_-1
//a_1_c_1
//a_1_b_1

print(planner['winningPlan']['inputStage']['inputStage']['indexName'])
for (var i = 0; i < 3; i++) {
    print(planner['rejectedPlans'][i]['inputStage']['inputStage']['inputStage']['inputStage']['indexName'])
}

