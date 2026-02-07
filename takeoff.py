from pymavlink import mavutil
from ArmDisarm import arm_drone, disarm_drone

def do_takeoff(conn, height):
    
    return

def main():
    CONNECTION = mavutil.mavlink_connection('udpin:localhost:14551')

    #cria a conexão:
    CONNECTION.wait_heartbeat()                                                            #espera a heartbeat (ou seja, o drone falar que ta tudo ok)
    print("heartbeat registrada, drone conectado!")                                         
    print(f"sistema {CONNECTION.target_system}, componente {CONNECTION.target_component}")    
    #comandos:

    arm_drone(CONNECTION)

    msg = CONNECTION.recv_match(type="COMMAND_ACK",blocking=True)
    
    if msg == 1:
        do_takeoff(CONNECTION, height=2)
        disarm_drone(CONNECTION)
        return 0
    else:
        disarm_drone(CONNECTION)
        return -1

if __name__ == '__main__':
    print("fly my babies, fly!")
    code = main()
    if code == -1:
        print("execução do voo terminou em erro!")
    elif code == 0:
        print("execução do voo concluída com sucesso!")