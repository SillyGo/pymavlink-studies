from pymavlink import mavutil

connect = mavutil.mavlink_connection('udpin:localhost:14551')

connect.wait_heartbeat()
print("heartbeat registrada, drone conectado!")
print(f"sistema {connect.target_system}, componente {connect.target_component}")