# Rule-Engine

This project Includes Rule engine challenge where the rules are made from the given set of data and will be stored in the Cassandra database.These Rules will be used to evaluate the new data and will be able report whether the given data violates the given set of rules or not.



## Rule generation from the data:

![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Input.json------->passinputforrules.py-------->generaterules.py

Here the data from the Input.json will be read by the passinputforrules.py file where it will be sent to a kafka topic.
generaterules.py on the other side listens to the kafka messages and generates rules with the given set of data.



## Executing the data from Rules:

![#c5f015](https://placehold.it/15/c5f015/000000?text=+) executerules.json -------->passinputforexecution--------->executerules.py----------->violatedrules.txt

Here the data from the executerules.json will be read by the passinputrulesforexecution.py file where it will be sent to a kafka topic.
executerules.py on the other side listens to the kafka messages and executes the rules(checks the data whethere it violates the rules or not).If the data violates the rules then this data will be captured into violatedrules.txt
