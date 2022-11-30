import json
import config

from kafka import KafkaConsumer

consumer = KafkaConsumer(
    config.ORDER_CONFIRMED_KAFKA_TOPIC,
    bootstrap_servers=config.BOOTSTRAP_SERVERS
)

total_orders_count = 0
total_revenue = 0
average_cost = 0

print("Analytics listening..")

while True:
    for message in consumer:
        print("Updating analytics...")
        consumed_message = json.loads(message.value.decode())

        total_cost = float(consumed_message["total_cost"])

        total_orders_count += 1
        total_revenue += total_cost
        average_cost = total_revenue / total_orders_count

        print(f"Orders so far today: {total_orders_count}")
        print(f"Revenue so far today: {total_revenue}")
        print(f"Average Cost so far today: {average_cost}")
