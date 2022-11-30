import json
import config

from kafka import KafkaProducer
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    config.ORDER_KAFKA_TOPIC,
    bootstrap_servers=config.BOOTSTRAP_SERVERS
)
producer = KafkaProducer(
    bootstrap_servers=config.BOOTSTRAP_SERVERS
)
print("Transaction start listening...")
while True:
    for message in consumer:
        print("Ongoing transaction..")
        consumer_message = json.loads(message.value.decode())
        print(consumer_message)

        user_id = consumer_message["user_id"]
        total_cost = consumer_message["total_cost"]

        data = {
            "customer_id": user_id,
            "customer_email": f"{user_id}@gmail.com",
            "total_cost": total_cost
        }
        print("Successful transaction...")
        producer.send(
            config.ORDER_CONFIRMED_KAFKA_TOPIC,
            json.dumps(data).encode("utf-8")
        )
