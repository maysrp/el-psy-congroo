import machine
import ustruct

class TCA9548A():
    def __init__(self,address,scl_pin=22,sda_pin=21):
        self.address=address
        self.bus=machine.I2C(-1, machine.Pin(scl_pin), machine.Pin(sda_pin))

    def switch_channel(self,channel):
        self.bus.writeto(self.address,ustruct.pack('B',1 << channel))