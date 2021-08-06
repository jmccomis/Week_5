from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from time import sleep
from gpiozero import Button
owm = OWM('60e28eb1145d5d9330745ad3a0d5417e')
x=7
button=Button(26)
def pressed():
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place('Milwaukee,USA')
    W = observation.weather
    print("button was pushed and the temperature is " + str(W.temperature('fahrenheit').get('temp')) + " degrees")
    
while x<10:
    button.when_pressed = pressed
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place('Milwaukee,USA')
    W = observation.weather

    print("the temperature is " + str(W.temperature('fahrenheit').get('temp')) + " degrees")
    sleep(5)
    