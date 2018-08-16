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
import datetime
import json


LOGGER=tools.getlogger()


def verify_rules(message):
    """
    Function verify_rules is used to verify whether the given data violates the existing rules or not.
    If the given signal violates the rule then the data will be captured into a text file
    """

    print message
    if message["signal"] == "END":
        print "End of File."

    else:
        key=message["signal"]
        value_type=message["value_type"]
        value=message["value"]
        rule_value=db.get_value(key,value_type)
        if rule_value==0:
            print "[INFO] No Rule of this particular type."
        else:
            if value_type == "Integer":
                if float(rule_value)<=float(value):
                    print "[INFO] Satisfies the Rule."
                else:
                    tools.writetofile(message)
                    print "[INFO] Violates the Rule."
            elif value_type == "String":
                if rule_value==value:
                    print "[INFO] Satisfies the Rule."
                else:
                    tools.writetofile(message)
                    print "[INFO] Violates the Rule."
            elif value_type == "Datetime":
                print "[CHECK] {0},{1}".format(rule_value,value)
                if tools.get_epoch(tools.convert(rule_value))>=tools.get_epoch(tools.convert(value)):
                    print "[INFO] Satisfies the Rule."
                else:
                    tools.writetofile(message)
                    print "[INFO] Violates the Rule."


if __name__=="__main__":

    """
       In the main function we connect to the consumer with the testdatastream_topic where the new set of data 
       will be consumed and verified whether it violates the given rules or not. 
    """

    rule_consumer = connections.kafka_connect(config.testdatastream_topic)
    running = True
    try:
        while running:
            kafka_msg = rule_consumer.poll()
            if kafka_msg != None:
                if not kafka_msg.error():
                    try:
                        jsonobject = json.loads(kafka_msg.value().decode('utf-8'))
                        verify_rules(jsonobject)

                    except:
                        LOGGER.info(traceback.print_exc())
                else:
                    print "[INFO] No kafka message."
            else:
                print "[INFO] KAFKA DONE"
    except:
        LOGGER.info(traceback.print_exc())

