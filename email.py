import json
import config

from kafka import KafkaConsumer

consumer = KafkaConsumer(
    config.ORDER_CONFIRMED_KAFKA_TOPIC,
    bootstrap_servers=config.BOOTSTRAP_SERVERS
)

email_send_so_far = set()
print("Email is listening..")

while True:
    for message in consumer:
        consumed_message = json.loads(message.value.decode())
        customer_email = consumed_message["customer_email"]

        print(f"Sending email to {customer_email}")

        email_send_so_far.add(customer_email)
        print(f"So far emails sent to {len(email_send_so_far)} unique emails.")
