from kafka import KafkaConsumer,KafkaProducer
import configurations.config as config
import json

producer = KafkaProducer(bootstrap_servers=config.kafka_bootstrap_servers, retries=5)


if __name__=="__main__":

    """
    In this main function we get the data from the given json file and send this data as messages to the kafka topic which will be 
    consumed on the other side and is used to generate rules which are stored in cassandra tables.
    
    """

    inputjson = json.loads(open('rules.json').read())

    for iterator in inputjson:
        message={}
        message["signal"]=iterator["signal"]
        message["value"]=iterator["value"]
        message["value_type"]=iterator["value_type"]
        message=json.dumps(message)
        response=producer.send(config.inputstream_topic,b'{0}'.format(message))
        print response
    print "[INFO] Messages have been successfully sent"