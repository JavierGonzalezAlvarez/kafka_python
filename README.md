# python and confluent kafka - docker
https://pypi.org/project/confluent-kafka/

$ pip install confluent-kafka
$ docker network create kafka-networks
$ docker-compose up
$ docker image prune -f -a
$ docker rm $(docker ps -a -q) -f

# run python
$ python3 producer.py
$ python3 consumer.py
