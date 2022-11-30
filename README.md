# Scalable & Event Driven Food Ordering App with Kafka & Python | System Design

This demo is a simple backend app for ordering food, implemented on python and using kafka as event driven platform.<br/>
<br/>

![! kafka-python-demo](https://github.com/ranrosenzweig/kafka-python-demo/blob/main/doc/img/diagram.png)

#### 0.pre-requisites:
```sh
pip install kafka-python
```

#### 1. Start the Kafka broker
From a directory containing the docker-compose.yml file, start all services in the correct order.
```sh
docker-compose up -d
```