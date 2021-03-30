import framebuf
import time
from ssd1306 import SSD1306_I2C

class stfe(object):
    def __init__(self,tca):
        self.tca=tca
        ce=open("f.font","rb")
        self.q=ce.readlines()
        ce.close()

    def stf(self,x,oled):
        w="0123456789:.abcdefghijklmnopqrstuvwxyz ".index(x.lower())
        if w==38:
            oled.fill(0)
            oled.show()
        else:
            data=bytearray(self.q[w])
            fbuf = framebuf.FrameBuffer(data,128,32,framebuf.MONO_HLSB)
            oled.fill(0)
            oled.blit(fbuf,0,0)
            oled.show()
    
    def showStr(self,num,nx):
        self.tca.switch_channel(num)
        oled = SSD1306_I2C(128, 32, self.tca.bus)
        self.stf(str(nx),oled)

    def showFull(self,num,nx=0):
        self.tca.switch_channel(num)
        oled = SSD1306_I2C(128, 32, self.tca.bus)
        oled.fill(nx)
        oled.show()

    def showAll(self,strNum):
        c=str(strNum)
        if len(c)>8:
            c=c[0:8]
        for i in range(8):
            if i>len(c)-1:
                self.showFull(7-i,0)
            else:
                self.showStr(7-i,c[i])