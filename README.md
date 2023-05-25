# python and confluent kafka - docker
https://pypi.org/project/confluent-kafka/

$ docker network create kafka-networks
$ docker-compose up
$ docker image prune -f -a
$ docker rm $(docker ps -a -q) -f

# run python
## virtual environment
$ virtualenv entorno_virtual -p python3.11
$ source entorno_virtual/bin/activate
$ pip install confluent-kafka

$ python3 producer.py
$ python3 consumer.py
