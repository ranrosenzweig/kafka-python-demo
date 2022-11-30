# Scalable & Event Driven Food Ordering App with Kafka & Python | System Design

This demo is a simple backend app for ordering food, implemented on python and using kafka as event driven platform.<br/>
<br/>
**Services included**:
1. **Food Ordering Client** - responsible to generate food orders by the user (not implemented)
2. **Orders** - responsible to get the orders from the clients, create event and send to the system.
3. **Transaction** - responsible to get orders, provide a confirmation and send new event back to the system.
4. **Analytics** - responsible to get insights from the orders like total orders that been sent and total revenue status.
5. **Email** - responsible to send emails to the users once the order has been confirmed.

#### HL diagram:
![! kafka-python-demo](https://github.com/ranrosenzweig/kafka-python-demo/blob/main/doc/img/diagram.png)

#### pre-requisites, install kafka-python package:
```sh
pip install kafka-python
```

#### 1. Start the Kafka broker:
From a directory containing the docker-compose.yml file, start all services in the correct order.
```sh
docker-compose up -d
```

#### 2. Start the app components:
```sh
python3 transaction.py 
python3 analytics.py 
python3 email.py 
python3 orders.py 
```


**Note**: Check config.ini for configure some values.

</br>

#### Reference project
https://github.com/irtiza07/python-kafka-demo