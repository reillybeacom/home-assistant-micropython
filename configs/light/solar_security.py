import esp8266.wemos.d1mini.pinmap as pinmap

NAME = 'Light'

RETAIN = ('enable', 'auto', 'brightness')

#### LED ####

LED_GPIO = pinmap.LED

#### Light / Switch ####

## Change the component for Home Assistant:
COMPNT = 'light' # options: 'light', 'switch', None

## Relay shield is D1 by default:
GPIO = pinmap.D1

BRIGHTNESS = True

INIT_BRI = 10 # percent

#### Button ####

BTN = False

## Wemos 1-button shield is D3 by default:
BTN_GPIO = pinmap.D3

## Set to 0 for Wemos 1-button shield:
BTN_VAL = 0

#### Motion Sensor ####

MOTN = True

## Wemos PIR shield is D3 by default:
MOTN_GPIO = pinmap.D2

## Set to 1 for Wemos PIR Shield:
MOTN_VAL = 0

## Turn off light n-seconds after being turned on:
MOTN_TIME = 20 # seconds

#### Battery ####

BATT = True

BATT_ADC = pinmap.A0

## Update interval:
BATT_INT = 60 # seconds

## Disable light when battery below:
BATT_LOW = 50 # percent or None
