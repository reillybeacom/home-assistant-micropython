from lib.esp8266.wemos.d1mini import oled
import wifi

oled.write('POWER ON')

class Display():
    def on_state_change(self, state, changed):
        oled.write('%-5s %s%s' % (
            state.mode,
            "+" if wifi.is_connected() else "-",
            "+" if state.telemetry else "-",
        ), False)
        oled.write('SOL %4d' % state.solar_temperature, False)
        oled.write('TNK %4d' % state.tank_temperature, False)
        oled.write('PUMP %3s' % ('ON' if state.pump else 'OFF'))
