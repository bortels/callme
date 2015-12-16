# callme
Event notification server for sensu and prowl

This is a flack server that accepts events from Sensu monitoring, and notifies people via prowl as appropriate.
Notifications are sent with a response URL so that the person notified can acknowledge they received the page,
and perhaps defer or escalate it automatically. In the event of a lack of response, escalation is automatic. 

This app runs in a docker container; it expects to be able to talk to a linked redis container that is used to
store event state and contact information. 
