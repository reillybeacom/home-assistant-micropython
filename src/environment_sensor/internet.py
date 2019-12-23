from lib.home_assistant.mqtt import MQTT
from lib.home_assistant.sensor import Sensor
from lib.home_assistant.sensors.battery import Battery
from lib.home_assistant.sensors.humidity import Humidity
from lib.home_assistant.sensors.illuminance import Illuminance
from lib.home_assistant.sensors.temperature import Temperature
from lib.esp8266.wemos.d1mini import status_led
from micropython import schedule
from machine import reset_cause, DEEPSLEEP_RESET
from utime import sleep
import config
import secrets
import wifi

class Internet():
    def __init__(self, state):
        print(wifi.uid())

        if reset_cause() != DEEPSLEEP_RESET:
            status_led.slow_blink()
        wifi.connect(secrets.WIFI_NAME, secrets.WIFI_PASSWORD)
        status_led.off()

        mqtt = MQTT(config.NAME, secrets)

        opt = dict(exp_aft = config.FREQ * 2.5)

        if 'temp' in state:
            mqtt.add('Temp', Temperature, **opt).set_state(state['temp'])

        if 'humid' in state:
            mqtt.add('Humid', Humidity, **opt).set_state(state['humid'])

        if 'lux' in state:
            mqtt.add('Lux', Illuminance, **opt).set_state(state['lux'])

        if 'analog' in state:
            mqtt.add('Analog', Sensor, unit = "%", icon = "mdi:gauge", **opt).set_state(state['analog'])

        if 'battery' in state:
            mqtt.add('Battery', Battery, key = 'bat', **opt).set_state(state['battery'])
            mqtt.set_attr('battery', state['battery'])

        mqtt.set_attr("freq", config.FREQ)

        if wifi.is_connected():
            if reset_cause() != DEEPSLEEP_RESET:
                status_led.fast_blink()
            else:
                ha.do_pub_cfg = False
            mqtt.connect()
            mqtt.pub_state()
            status_led.off()
            sleep(5)
            mqtt.discon()
