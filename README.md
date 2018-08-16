# Rule-Engine

This project Includes Rule engine challenge where the rules are made from the given set of data and will be stored in the Cassandra database.These Rules will be used to evaluate the new data and will be able report whether the given data violates the given set of rules or not.



## Rule generation from the data:

![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Input.json------->passinputforrules.py-------->generaterules.py

Here the data from the Input.json will be read by the passinputforrules.py file where it will be sent to a kafka topic.
generaterules.py on the other side listens to the kafka messages and generates rules with the given set of data.



## Executing the data using predefined Rules:

![#c5f015](https://placehold.it/15/c5f015/000000?text=+) executerules.json -------->passinputforexecution--------->executerules.py----------->violatedrules.txt

Here the data from the executerules.json will be read by the passinputrulesforexecution.py file where it will be sent to a kafka topic.
executerules.py on the other side listens to the kafka messages and executes the rules(checks the data whethere it violates the rules or not).If the data violates the rules then this data will be captured into violatedrules.txt



## Discussion

### Briefly describe the conceptual approach you chose! What are the trade-offs?
I have choosed the event based approach where the data will be generated when the event has been done,This is because the signal generated would be due to an event.We used kafka so that we can start as many consumers as possible which will automatically load balance and helps in the faster execution of the data.
 
 The only limitation is:
 The Rules should be predefined before the execution of the data because the there should be some set of rules in order for the data to be judged.

### What's the runtime performance? What is the complexity? Where are the bottlenecks?
A single kafka conumser will execute 1000 singals in 4 seconds.If we start multiple consumers then the execution time decreases in the order of n. The time complexity is in order 0(n).

### If you had more time, what improvements would you make, and in what order of priority?
I would have designed an UI where the user will upload a set of rules,and then after that UI where events which create the data.
When user has submitted some data this data will be sent to consumer and if it violates the given set of rules.An alert will be shown to the user that the data violates the given set of rules.
