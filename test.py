import revpimodio2
import struct
rpi = revpimodio2.RevPiModIO(autorefresh=True)
rpi.io.Master_Status_Reset.value=1
rpi.io.Action_Status_Reset_1.value=1
rpi.io.Action_Status_Reset_2.value=1
#rpi.io.belt_frequency.byteorder='big'
print('Master status ',rpi.io.Modbus_Master_Status.value)
rpi.io.belt_frequency.value = int(1234)
rpi.io.belt_start.value = 0
rpi.io.belt_stop.value = 1
print('set F ',rpi.io.belt_frequency.value)
print('read F ',rpi.io.belt_current_frequency.value)
print('Master status ',rpi.io.Modbus_Master_Status.value)
print('Action 1 status',rpi.io.Modbus_Action_Status_1.value)
print('action 2 status ',rpi.io.Modbus_Action_Status_2.value) 
rpi.io.belt_start.value = 0