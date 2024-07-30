from kafka import KafkaProducer
import json
from app.config import Config

producer = None

def get_kafka_producer():
    global producer
    if producer is None:
        try:
            producer = KafkaProducer(
                bootstrap_servers=Config.KAFKA_BOOTSTRAP_SERVERS,
                value_serializer=lambda v: json.dumps(v).encode('utf-8')
            )
        except Exception as e:
            print(f"Failed to create Kafka producer: {e}")
    return producer

def produce_flight_status_update(flight_data):
    producer = get_kafka_producer()
    if producer:
        try:
            producer.send('flight_status_updates', flight_data)
        except Exception as e:
            print(f"Failed to send message to Kafka: {e}")
    else:
        print("Kafka producer is not available. Message not sent.")

def consume_flight_status_updates():
    pass