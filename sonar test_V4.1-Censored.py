from machine import Pin
import utime
    
trigger = Pin(26, Pin.OUT)
echo = Pin(18, Pin.IN)  

def ultra(): # Creating a function for data gathering 
    trigger.value(0) # Calling trigger pin 
    utime.sleep_us(2) # Waiting 2 micro-seconds before pulsing the trigger pin 
    trigger.value(1)
    utime.sleep_us(10) # Triggering pulse for 10 micro-seconds 
    trigger.value(0) # Setting trigger pin back to low
    
    # Timeout protection for signal start
    timeout = utime.ticks_us()
    while echo.value() == 0: # If no echo pulse is recieved:
        signaloff = utime.ticks_us() # Storing the time that no echo is recieved in the variable 'signaloff'
        if utime.ticks_diff(utime.ticks_us(), timeout) > 100000:  # 30ms timeout
            print("Sensor timeout - no signal start")
            return None
    
    # Timeout protection for signal end
    timeout = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us() # Storing time that the echo is recieving a pulse
        if utime.ticks_diff(utime.ticks_us(), timeout) > 100000:  # 30ms timeout
            print("Sensor timeout - no signal end")
            return None

    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    distance = "{:.1f}".format(distance)

    print(distance + " cm")
    return distance

while True:
    ultra()
    utime.sleep(0.5)