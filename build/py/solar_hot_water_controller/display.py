from lib.esp8266.wemos.d1mini.oled import OLED
from utime import sleep
import wifi

class Display():
    def __init__(self, status):
        self.oled = OLED()
        self.show_telemetry(status)
        
    def show_telemetry(self, status):
        self.oled.write_lines(
            'WIFI:',
            ('%8d' % wifi.rssi()) if wifi.is_connected() else ('%8s' % '--'),
            'MQTT:',
            '%8s' % ('OK' if status.telemetry else '--'),
        )            
        sleep(2)
    
    def on_state_change(self, state, changed):
        if 'telemetry' in changed:
            self.show_telemetry(state)
        else:
            self.oled.write_lines(
                'SOLR:%3d' % state.solar_temperature,
                'TANK:%3d' % state.tank_temperature,
                'TARG:%3d' % state.tank_target_temperature,
                '%-5s%3s' % (state.mode.upper(), 'ON' if state.pump else 'OFF'),
            )

    def deinit(self):
        self.oled.clear()
        self.oled.power_off()
