use store;
db.products.drop();

db.products.createIndex({'sku': 1}, {name: 'sku_1', unique: true});
db.products.createIndex({'price': -1}, {name: 'price_1'});
db.products.createIndex({'description': 1}, {name: 'description_1'});
db.products.createIndex({'category': 1, 'brand': 1}, {name: 'category_1_brand_1'});
db.products.createIndex({'reviews.author': 1}, {name: 'reviews.author_1'});


for (i = 0; i < 100000; i++) {
    brands = ['AE','BE','CE','GE'];
    categories = ['category 1', 'category 2', 'category 3', 'category 4'];
    descriptions = ['description 1', 'description 2', 'description 3', 'description 4'];
    rand = Math.floor(Math.random() * 4);

    record = {
        'sku': NumberInt(i),
        'price': Math.floor(Math.random() * 1000),
        'description': descriptions[rand],
        'category': categories[rand],
        'brand': brands[rand]
    }

    db.products.insert(record);
}
