import connections.connections as connections
import utils.tools as tools
import traceback

session=connections.cassandra_connection()

LOGGER=tools.getlogger()

def insert_rule(key,value,value_type):

    """
    Function insert_rule inserts the rule into the rules table of the rule_engine keyspace..

    """

    try:
        query="insert into ruleengine.rules(key,value,value_type) values(?,?,?)"
        prepared=session.prepare(query)
        result=session.execute(prepared,(key,value,value_type))
        return 1
    except:
        LOGGER.info(traceback.print_exc())
        return 0


def get_value(key,value_type):

    """
    Function get_value gives the value of the singal for the given value_type which was earlier defined by set of rules.

    """

    value=0
    query="select * from ruleengine.rules where key=? and value_type=?"
    prepared=session.prepare(query)
    result=session.execute(prepared,(key,value_type))
    for details in result:
        value=details.value
    return value

