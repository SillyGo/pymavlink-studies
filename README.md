## pymavlink-studies
---

this is where i add all the stuff regarding my studies of pymavlink, this will probably be kindof short lived as i will just be pasting code here with all the stuff i learn about this protocol

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

### 3. takeoff.py and changeMode.py

there are two new things here, first of all, we must set the drone's takeoff, which consists of a simple long message as the ones seen before in arming / disarming:

```
conn.mav.command_long_send(
        conn.target_system,
        conn.target_component,
        mavutil.mavlink.MAV_CMD_TAKEOFF,
        0,0,
        0,0,0,0,0,height
)
```

the second one regards the changing of the drone's MODE. Here, we are worrying about two modes, 'GUIDED' and 'RTL'. Guided mode allows for manual control (such as takeoffs), while RTL sets the drone in resting mode, so that activating this mode has the drone land and stop. Changing modes is pretty straightforward, however:

```
conn.set_mode(mode)
```

the other things i added to the function are merely for debugging purposes 

### 4. movLocal.py

ok, this one may take some lines to explain

```
z_metros = -z_metros #da própria documentação do mavlink: "z: Z Position in meters (positive is down)"
az = -az # pelo mesmo motivo que o de cima
```

as the comments state, these two lines exist because of ardupilot's coordinate system, in which 'z' is facing downwards. For more intuitive code logic, i done that transformation for the user.

```
bitmapPosition = 0b110111111000
bitmapVelocity = 0b110111000111
bitmapAcc      = 0b110000111111
bitmapYaw      = 0b100111111111
bitmapYawRate  = 0b010111111111

bitmap = 0b111111111111

if use_position:
    bitmap = bitmap & bitmapPosition
if use_vel:
    bitmap = bitmap & bitmapVelocity
if use_yaw:
    bitmap = bitmap & bitmapYaw
if use_acc:
    bitmap = bitmap & bitmapAcc
if use_yawRate:
    bitmap = bitmap & bitmapYawRate
```

oh hear haha, so, there are many fields you can pass into the position message, ardupilot has a method for automatically filtering out inputs depending on the type of movement you want. So if you wanted to send a position message that contains both cartesian and yaw changes, you would have to manually bitwise AND the two bitmaps. So i decided to do that automatically, as can be seen in the sequence of if statements. Maybe i could have done it more efficiently if i used only bitwise operations, and i tried doing that, but gave up and just went with the 'if' cascade implementation instead (although i think it possible to use just bitwise ops)

anyway, after setting the bitmap, you can just send the movement command via

```
time_bootms = 10

conn.mav.send(mavutil.mavlink.MAVLink_set_position_target_local_ned_message(
    time_bootms, conn.target_system, conn.target_component, mavutil.mavlink.MAV_FRAME_LOCAL_NED, int(bitmap), x_metros, y_metros, z_metros, 
    vx,vy,vz,ax,ay,az,yaw,yawr 
))
```

finally, there is also the function moveDroneLocalPosition, its nothing very interesting, just a function that doesnt require all those fields that moveDroneLocal has, and is easier for the task of setting simple cartesian movements.
ps. all the functions defined here perform movement in the local coordinate system, so the x,y,z system we are all used to. But there is also the global system, which uses GPS coordinates, that is, latitude, longitude and altitude.

TODO: testar movLocal.py \
TODO: estudar sobre mudança de velocidade e yaw durante o voo \
TODO: as todos que surjam dps \
