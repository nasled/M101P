# M101P: MongoDB for Developers

## Warning! Contains spoilers.

Tested on
- Mongo 4.3.2
- Python 3.6.0
- Docker 1.12.6

### init mongos and hosts
```commandline
$ docker run --name mongo-cont --expose 27017 -v /home/user/mongo/datadb:/data/db -d mongo
$ docker run --name mongos-cont --expose 27000-61000 -v /home/user/mongo/sdatadb:/data/db -d mongo
$ docker run --name mongor-cont --expose 27000-61000 -v /home/user/mongo/rdatadb:/data/db -d mongo

$ echo "172.17.0.2      mongo.localhost         mongo.loc" >> /etc/hosts
$ echo "172.17.0.3      mongo.localhost         mongos.loc" >> /etc/hosts
$ echo "172.17.0.4      mongo.localhost         mongor.loc" >> /etc/hosts
```

### get shell in container
```
$ docker exec -it <container-name> bash
```

### init project
```commandline
$ virtualenv M101P
$ source M101P/bin/activate
$ pip install bottle pymongo
```
	
