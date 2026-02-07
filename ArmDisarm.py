from pymavlink import mavutil

CONNECTION = mavutil.mavlink_connection('udpin:localhost:14551')

def arm_drone():
    CONNECTION.mav.command_long_send(
        CONNECTION.target_system,
        CONNECTION.target_component,
        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
        0,1,
        0,0,0,0,0,0
    )

def disarm_drone():
    CONNECTION.mav.command_long_send(
        CONNECTION.target_system,
        CONNECTION.target_component,
        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
        0,0,
        0,0,0,0,0,0
    )

def set_commands():     #TODO: Implementar essa função nos próximos códigos
    return

CONNECTION.wait_heartbeat()                                                            #espera a heartbeat (ou seja, o drone falar que ta tudo ok)
print("heartbeat registrada, drone conectado!")                                         
print(f"sistema {CONNECTION.target_system}, componente {CONNECTION.target_component}")    

#2. ENVIANDO COMANDOS SIMPLES

arm_drone() #  arma o drone, necessário para movimentarmos ele :D

set_commands() #roda os comandos que quisermos que a controladora execute, como ir para determinadas posições

disarm_drone() #disarma o drone, importante para quando terminarmos de usar ele
