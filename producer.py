from confluent_kafka import Producer  # , KafkaError
import json

producer = Producer({
    'bootstrap.servers': 'localhost:9092',
})


def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        # partitions are created when a topic is set
        print('Message delivered to {} - partition [{}]'.format(
            msg.topic(), msg.partition()))


# data to be sent
for i in range(3):
    record_key = "javier"
    print("number", i)
    # dictionary
    data = ({'sent from producer': i})
    # convert list to object (required)
    data = json.dumps(data)
    producer.poll(0)
    producer.produce('topic_1', key=record_key,
                     value=data, callback=delivery_report)

producer.flush()
