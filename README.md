# M101P: MongoDB for Developers

Tested on python version 3.6

### init db
```commandline
$ docker run --name mongo-cont --expose 27017 -v /home/user/mongodatadb:/data/db -d mongo
$ docker exec -it mongo-cont bash
$ echo "172.17.0.2      mongo.localhost         mongo.loc" >> /etc/hosts 
```

### init project
```commandline
$ virtualenv M101P
$ source M101P/bin/activate
$ pip install bottle pymongo
```
	
