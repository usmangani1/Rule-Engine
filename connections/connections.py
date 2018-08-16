from confluent_kafka import Consumer
from cassandra.cluster import Cluster
import utils.tools as tools
import configurations.config as config


LOGGER=tools.getlogger()

def kafka_connect(topic):

    """
    The function kafka_connect returns a kafka consumer with the specified topic mentioned ,The topic
    name will be sent given in the parameters

    """

    LOGGER.info("[KAFKA] Connecting to Topic -> (" + str(topic) + ")")

    consumer = Consumer(
        {
            'bootstrap.servers': config.kafka_bootstrap_servers,
            'group.id': '{0}'.format(config.groupid),
            'default.topic.config': {'auto.offset.reset': 'latest'},
            'session.timeout.ms': '300000',
            'enable.auto.commit': False
        }
    )
    LOGGER.info("[KAFKA] Subscribing to consumer on topic " + str(topic))


    consumer.subscribe([topic])

    return consumer



def cassandra_connection():

    """
        The function cassandra_connection gives a cassandra connection string which will be used to query the cassandra database.
    """

    auth_provider = config.auth_provider
    cluster = Cluster(config.cassandra_hosts, auth_provider=auth_provider, connect_timeout=300)
    session = cluster.connect()
    return session


