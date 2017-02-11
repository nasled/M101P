use blog;

db.posts.dropIndex('date_-1');
db.posts.dropIndex('permalink_1');
db.posts.dropIndex('tags_1_data_-1');

db.posts.createIndex({'date': -1}, {name: 'date_-1'});
db.posts.createIndex({'permalink': 1}, {name: 'permalink_1', unique: true});
db.posts.createIndex({'tags': 1, 'date': -1}, {name: 'tags_1_data_-1'});
