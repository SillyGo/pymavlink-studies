from pymavlink import mavutil
from ArmDisarm import arm_drone, disarm_drone
from takeoff import do_takeoff
from changeMode import change_mode
from time import sleep

def moveDroneLocal(conn, x_metros, y_metros, z_metros, use_position:bool, use_vel:bool, use_yaw:bool, use_acc:bool, use_yawRate:bool, vx,vy,vz,ax,ay,az,yaw,yawr):
    z_metros = -z_metros #da própria documentação do mavlink: "z: Z Position in meters (positive is down)"
    az = -az # pelo mesmo motivo que o de cima
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

    time_bootms = 10

    conn.mav.send(mavutil.mavlink.MAVLink_set_position_target_local_ned_message(
        time_bootms, conn.target_system, conn.target_component, mavutil.mavlink.MAV_FRAME_LOCAL_NED, int(bitmap), x_metros, y_metros, z_metros, 
        vx,vy,vz,ax,ay,az,yaw,yawr 
    ))

def moveDroneLocalPosition(conn, x_metros, y_metros, z_metros):
    z_metros = -z_metros #da própria documentação do mavlink: "z: Z Position in meters (positive is down)"
    bitmap = 0b110111111000

    time_bootms = 10

    conn.mav.send(mavutil.mavlink.MAVLink_set_position_target_local_ned_message(
        time_bootms, conn.target_system, conn.target_component, mavutil.mavlink.MAV_FRAME_LOCAL_NED, int(bitmap), x_metros, y_metros, z_metros, 
        0,0,0,0,0,0,0,0 
    ))

def main():
    connect = mavutil.mavlink_connection('udpin:localhost:14551')

    connect.wait_heartbeat()
    print("heartbeat registrada, drone conectado!")
    print(f"sistema {connect.target_system}, componente {connect.target_component}")

    arm_drone(connect)
    sleep(1)
    change_mode(connect, "GUIDED")
    sleep(5)
    do_takeoff(connect, 5)
    sleep(10)
    moveDroneLocalPosition(connect, 10, 0, 10)
    sleep(25)
    moveDroneLocalPosition(connect, -10,0,-10)
    sleep(25)
    change_mode(connect, "RTL")
    sleep(10)
    disarm_drone(connect)

if __name__ == '__main__':
    print("fly my babies, fly!")
    main()
    print("execução do voo terminada com sucesso!")