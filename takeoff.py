from pymavlink import mavutil
from ArmDisarm import arm_drone, disarm_drone
from time import sleep

def change_mode(conn, mode):
    conn.set_mode(mode)

    print("entrando no modo de verificação...")
    while True:
        msg = conn.recv_match(type="COMMAND_ACK", blocking=True)
        if msg == 1:
            break
        else:
            print("CHANGE_MODE: esperando confirmação do ACK")

def do_takeoff(conn, height):
    conn.mav.command_long_send(
        conn.target_system,
        conn.target_component,
        mavutil.mavlink.MAV_CMD_TAKEOFF,
        0,0,
        0,0,0,0,0,height
    )

    print("entrando no modo de verificação...")
    while True:
        msg = conn.recv_match(type="COMMAND_ACK", blocking=True)
        if msg == 1:
            break
        else:
            print("TAKEOFF: esperando confirmação do ACK")

def main():
    CONNECTION = mavutil.mavlink_connection('udpin:localhost:14551')

    #cria a conexão:
    CONNECTION.wait_heartbeat()                                                            #espera a heartbeat (ou seja, o drone falar que ta tudo ok)
    print("heartbeat registrada, drone conectado!")                                         
    print(f"sistema {CONNECTION.target_system}, componente {CONNECTION.target_component}")    
    #comandos:

    arm_drone(CONNECTION)

    change_mode(CONNECTION, mode="GUIDED")
    sleep(1)
    do_takeoff(CONNECTION, height=2)
    sleep(10)
    disarm_drone(CONNECTION)
    return 0

if __name__ == '__main__':
    print("fly my babies, fly!")
    code = main()
    if code == -1:
        print("execução do voo terminou em erro!")
    elif code == 0:
        print("execução do voo concluída com sucesso!")