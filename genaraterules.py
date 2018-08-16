#!/usr/bin/python
"""
__email__ sgosman_chem@yahoo.com
__author__ Usman Shaik
"""


import configurations.config as config
import connections.connections as connections
import utils.tools as tools
import query.db as db
import traceback
import json

LOGGER=tools.getlogger()

def generate_rule(message):

    """
    Function generate_rule generates rules with the given input signal and stores
    it into the rules table in the rule_engine keyspace of cassandra.
    """
    key=message["signal"]
    value=message["value"]
    value_type=message["value_type"]
    insert_success=db.insert_rule(key,value,value_type)
    if insert_success==1:
        LOGGER.info("[INFO] Rule insertion has been successful.")
    else:
        LOGGER.info("[INFO] Rule insertion has been unsuccessful.")


if __name__=="__main__":
    """
       In the main function we connect to the consumer with the input datastream topic where the input set of rules will be sent by the producer. 
    """
    rule_consumer = connections.kafka_connect(config.inputstream_topic)
    running = True
    try:
        while running:
            kafka_msg = rule_consumer.poll()
            if kafka_msg != None:
                if not kafka_msg.error():
                    try:
                        jsonobject = json.loads(kafka_msg.value().decode('utf-8'))
                        print jsonobject["signal"], jsonobject["value"], jsonobject["value_type"]
                        generate_rule(jsonobject)
                    except:
                        LOGGER.info(traceback.print_exc())
    except:
        LOGGER.info(traceback.print_exc())

