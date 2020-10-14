from phue import Bridge
import logging
logging.basicConfig()

b = Bridge('192.168.0.4')

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single$
#b.connect()

b.set_light(1, 'on', False)

