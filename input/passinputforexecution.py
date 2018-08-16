from kafka import KafkaConsumer,KafkaProducer
import configurations.config as config
import json
import time

producer = KafkaProducer(bootstrap_servers=config.kafka_bootstrap_servers, retries=5)


if __name__=="__main__":

    """
       In this main function we get the data from the given json file and send this data as messages to the kafka topic which will be 
       consumed on the other side and the data will will be verified wether it violates the given set of rules or not.

    """
    inputjson = json.loads(open('executerules.json').read())

    for iterator in inputjson:
        message={}
        message["signal"]=iterator["signal"]
        message["value"]=iterator["value"]
        message["value_type"]=iterator["value_type"]
        message=json.dumps(message)
        response=producer.send(config.testdatastream_topic,b'{0}'.format(message))
        print response

    time.sleep(5)
    print "[INFO] Messages have been successfully sent"
    message={}
    message["signal"]="END"
    message["value"]="END"
    message["value_type"]="END"
    message=json.dumps(message)
    response=producer.send(config.testdatastream_topic,b'{0}'.format(message))
    print response