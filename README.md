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

### 2. ArmDisarm.py

code that shows the logic for arming / disarming the drone, and also receiving ACK meessages.
ps. the same logic that goes for receiving the ACK message goes for receiving other messages, such as height.
COMMAND_LONG_SEND:

```
conn.mav.command_long_send(
        conn.target_system,
        conn.target_component,
        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
        0,1,
        0,0,0,0,0,0
)
```

this is used to send a long as a command, we could also use command_int_send(), but that would disable our capacity to use floating points in 5 and 6
this could also be done doing msg = mav.command_long_encode, so we encode first, then do mav.send(msg)
the '1' there is supposed to tell us that we want to arm the drone, to disarm it, we could simply set it to 0.

```
msg = CONNECTION.recv_match(type="COMMAND_ACK", blocking=True)
```

i could remove the 'type="COMMAND_ACK"' line, that would simply make it so that msg receives ALL messages available (however, that is generally not what we want)
ps. blocking=True makes it so that the function waits until the message is received to proceed to the next line of code

### 3. takeoff.py
=======
