#!/usr/bin/env bash

mkdir /data/{rs1,rs2,rs3}

echo "Start mongo intances"
mongod --replSet m101 --logpath "1.log" --dbpath /data/rs1 --port 37017 --smallfiles --oplogSize 64 --fork
mongod --replSet m101 --logpath "2.log" --dbpath /data/rs2 --port 37018 --smallfiles --oplogSize 64 --fork
mongod --replSet m101 --logpath "3.log" --dbpath /data/rs3 --port 37019 --smallfiles --oplogSize 64 --fork

echo "Create the replica set"
mongo --port 37017 << 'EOF'
config = { _id: "m101", members:[
    { _id : 0, host : "localhost:37017"},
    { _id : 1, host : "localhost:37018"},
    { _id : 2, host : "localhost:37019"} ]
};
rs.initiate(config);
EOF

mongo --port 37017 --eval "rs.status()"
