import query.db as db
import unittest
import json

class TestStringMethods(unittest.TestCase):

    def test_execution(self):

        inputjson = json.loads(open('tests.json').read())

        for message in inputjson:

            key = message["signal"]
            value_type = message["value_type"]
            value = message["value"]
            rule_value = db.get_value(key, value_type)
            if rule_value == 0:
                print "[INFO] No Rule of this particular type."
            else:
                if value_type == "Integer":
                    if float(rule_value) <= float(value):
                        print "[INFO] Satisfies the Rule."
                    else:
                        print (message)
                        print "[INFO] Violates the Rule."
                elif value_type == "String":
                    if rule_value == value:
                        print "[INFO] Satisfies the Rule."
                    else:
                        print (message)
                        print "[INFO] Violates the Rule."
                elif value_type == "Datetime":
                    print "[CHECK] {0},{1}".format(rule_value, value)
                    if tools.get_epoch(tools.convert(rule_value)) >= tools.get_epoch(tools.convert(value)):
                        print "[INFO] Satisfies the Rule."
                    else:
                        print (message)
                        print "[INFO] Violates the Rule."



if __name__ == '__main__':
    unittest.main()