from pymavlink import mavutil
from ArmDisarm import arm_drone, disarm_drone
from time import sleep

def change_mode(conn, mode):
    conn.set_mode(mode)

    print("entrando no modo de verificação...")
    msg = conn.recv_match(type="COMMAND_ACK", blocking=True)
    print(msg)
    #while True:
    #    msg = conn.recv_match(type="COMMAND_ACK", blocking=True)
    #    if msg == 1:
    #        break
    #    else:
    #        print("CHANGE_MODE: esperando confirmação do ACK")

def do_takeoff(conn, height):
    conn.mav.command_long_send(
        conn.target_system,
        conn.target_component,
        mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,
        0,0,
        0,0,0,0,0,height
    )

    print("entrando no modo de verificação...")
    msg = conn.recv_match(type="COMMAND_ACK", blocking=True)
    print(msg)

def main():
    CONNECTION = mavutil.mavlink_connection('udpin:localhost:14551')

    #cria a conexão:
    CONNECTION.wait_heartbeat()                                                            #espera a heartbeat (ou seja, o drone falar que ta tudo ok)
    print("heartbeat registrada, drone conectado!")                                         
    print(f"sistema {CONNECTION.target_system}, componente {CONNECTION.target_component}")    
    #comandos:

    change_mode(CONNECTION, "GUIDED")

    return 0

if __name__ == '__main__':
    print("fly my babies, fly!")
    code = main()
    if code == -1:
        print("execução do voo terminou em erro!")
    elif code == 0:
        print("execução do voo concluída com sucesso!")