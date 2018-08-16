import os

"""
    In this file we have default configurations.

"""

inputstream_topic = os.getenv('RULES_TOPIC',"{0}".format(b'input_rules'))

testdatastream_topic=os.getenv('DATASTREAM_TOPIC',"{0}".format(b'output_data'))

groupid = os.getenv('KAFKA_GROUPID',"{0}".format('RULEENGINEd'))

auth_provider=0

kafka_bootstrap_servers='localhost:9092'

cassandra_hosts=["localhost"]
