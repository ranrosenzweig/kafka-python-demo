import configparser

config = configparser.ConfigParser()
config.read('config.ini')  # path of your .ini file

BOOTSTRAP_SERVERS = config.get("kafka-configurations", "bootstrap_servers")

ORDER_KAFKA_TOPIC = config.get("kafka-settings", "order_topic")
ORDER_CONFIRMED_KAFKA_TOPIC = config.get("kafka-settings", "order_confirmed_topic")

ORDER_LIMIT = config.get("app-settings", "order_limit")
