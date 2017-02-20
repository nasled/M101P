db=db.getSiblingDB("school");
db.students.remove({});

// insert test data
types = ['exam', 'quiz', 'homework', 'homework'];
for (i = 0; i < 10000; i++) {

    // take 10 classes
    for (class_counter = 0; class_counter < 10; class_counter ++) {
	    scores = []

	    // and each class has 4 grades
	    for (j = 0; j < 4; j++) {
		    scores.push({'type':types[j],'score':Math.random()*100});
	    }

        // there are 500 different classes that they can take
        class_id = Math.floor(Math.random()*501); // get a class id between 0 and 500

        record = {'student_id':i, 'scores':scores, 'class_id':class_id};
        db.students.insert(record);
    }
}

//{ "student_id" : { "$minKey" : 1 } } -->> { "student_id" : 1 } on : s1 Timestamp(2, 0)
//{ "student_id" : 1 } -->> { "student_id" : 13 } on : s2 Timestamp(3, 0)
//{ "student_id" : 13 } -->> { "student_id" : 3613 } on : s1 Timestamp(4, 0)
//{ "student_id" : 3613 } -->> { "student_id" : 7789 } on : s0 Timestamp(4, 1)
//{ "student_id" : 7789 } -->> { "student_id" : { "$maxKey" : 1 } } on : s0 Timestamp(3, 4)
sh.status();

explain = db.students.find({'student_id':2000}).explain();

// s1
print(explain.queryPlanner['winningPlan']['shards'][0].shardName)
