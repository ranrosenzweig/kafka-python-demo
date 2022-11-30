import json
import time
import config

from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=config.BOOTSTRAP_SERVERS
)
#print("Going to be generating order after 5 seconds")
#print("Will generate one unique order every 5 seconds")

for i in range (1, int(config.ORDER_LIMIT)):
    data = {
        "order_id": i,
        "user_id": f"ran_{i}",
        "total_cost": i * 2,
        "items":  "burger, sandwich"
    }

    producer.send(
        config.ORDER_KAFKA_TOPIC,
        json.dumps(data).encode("utf-8")
    )
    print(f"Done sending...{i}")
    #time.sleep(5)