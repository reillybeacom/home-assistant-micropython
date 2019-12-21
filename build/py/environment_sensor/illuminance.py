from lib.esp8266.wemos.d1mini import pinmap
from machine import Pin, I2C

class Illuminance():
    def __init__(self, state):
        i2c = I2C(
            scl = Pin(pinmap.SCL),
            sda = Pin(pinmap.SDA)
        )

        from lib.esp8266.bh1750.bh1750 import BH1750
        bh1750 = BH1750(i2c)
        
        if bh1750.is_present():
            lux = bh1750.luminance(BH1750.ONCE_HIRES_1)
            bh1750.off()
            state.set(illuminance = lux)