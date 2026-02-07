## pymavlink-studies
---

this is where i add all the stuff regarding my studies of pymavlink, this will probably be kindof short lived as i will just be pasting code here with all the stuff i learn about this protocol
TODO: make a nice looking readme.md file later

### 1. listen.py:
that is the hello world of pymavlink. Essentially, all im doing is creating the connection to the drone and creating a print statement to confirm to the user that it went well.
my only question is regarding the line:

```
connect = mavutil.mavlink_connection('udpin:localhost:14551')
```

how would i know the actual IP to the drone ? TODO: come back here once you know the answer and put it down here 
PROBLEM ANSWER:

### 2. arm.py