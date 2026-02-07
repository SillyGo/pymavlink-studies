from pymavlink import mavutil

def arm_drone(conn):
    conn.mav.command_long_send(
        conn.target_system,
        conn.target_component,
        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
        0,1,
        0,0,0,0,0,0
    )

    print("entrando no modo de verificação...")
    msg = conn.recv_match(type="COMMAND_ACK", blocking=True)
    print(msg)

def disarm_drone(conn):
    conn.mav.command_long_send(
        conn.target_system,
        conn.target_component,
        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
        0,0,
        0,0,0,0,0,0
    )

    print("entrando no modo de verificação...")
    msg = conn.recv_match(type="COMMAND_ACK", blocking=True)
    print(msg)
    #while True:
    #    msg = conn.recv_match(type="COMMAND_ACK", blocking=True)
    #    if msg == 1:
    #        break
    #    else:
    #        print("DISARM: esperando confirmação do ACK")

def set_commands(conn):     #TODO: Implementar essa função nos próximos códigos
    return

CONNECTION = mavutil.mavlink_connection('udpin:localhost:14551')

CONNECTION.wait_heartbeat()                                                            #espera a heartbeat (ou seja, o drone falar que ta tudo ok)
print("heartbeat registrada, drone conectado!")                                         
print(f"sistema {CONNECTION.target_system}, componente {CONNECTION.target_component}")    

#2. ENVIANDO COMANDOS SIMPLES

arm_drone(CONNECTION) #  arma o drone, necessário para movimentarmos ele :D

set_commands(CONNECTION) #roda os comandos que quisermos que a controladora execute, como ir para determinadas posições

#PARA O ACK:
#msg = 0: MAV_RESULT_ACCEPTED
#msg = 1: MAV_RESULT_TEMPORARILY_REJECTED
#msg = 2: MAV RESULT DENIED
#msg = 3: MAV RESULT FAILED
#msg = 4: MAV RESULT IN PROGRESS
#msg = 5: MAV RESULT CANCELLED

disarm_drone(CONNECTION) #disarma o drone, importante para quando terminarmos de usar ele