
from machine import Pin
import utime
import network
import urequests
import ujson

# --------------------------
# WiFi Details
# --------------------------

SSID = "pmsTest"
Password = "connect12"

# --------------------------
# Power Automate URL
# --------------------------

FLOW_URL = "Censored_URL"
#SECRET = "Censored_Secret"

# --------------------------
# Ultrasonic Sensor Pins
# --------------------------

trigger = Pin(26, Pin.OUT)
echo = Pin(18, Pin.IN)

# --------------------------
# Connect to WiFi
# --------------------------

wifi = network.WLAN(network.STA_IF)
wifi.active(True)

print("Connecting to WiFi...")

wifi.connect(SSID, PASSWORD)

while not wifi.isconnected():
    utime.sleep(1)

print("Connected!")
print(wifi.ifconfig())

# --------------------------
# Distance Function
# --------------------------

def ultra():

    trigger.value(0)
    utime.sleep_us(2)

    trigger.value(1)
    utime.sleep_us(10)

    trigger.value(0)

    timeout = utime.ticks_us()

    while echo.value() == 0:
        signaloff = utime.ticks_us()

        if utime.ticks_diff(
            utime.ticks_us(),
            timeout
        ) > 100000:

            return None

    timeout = utime.ticks_us()

    while echo.value() == 1:
        signalon = utime.ticks_us()

        if utime.ticks_diff(
            utime.ticks_us(),
            timeout
        ) > 100000:

            return None

    timepassed = signalon - signaloff

    distance = (timepassed * 0.0343) / 2

    return distance

# --------------------------
# Send Power Automate Update
# --------------------------

def send_status(status):

    payload = {
        "bay_1": str(status).lower(),
        "secret": SECRET
    }

    try:

        response = urequests.post(
            FLOW_URL,
            headers={
                "Content-Type":
                "application/json"
            },
            data=ujson.dumps(payload)
        )

        print("Request Sent")
        print(payload)

        response.close()

    except Exception as e:
        print("Request Failed")
        print(e)

# --------------------------
# Parking Detection
# --------------------------

OCCUPIED_THRESHOLD = 100

last_status = None

while True:

    distance = ultra()

    if distance is not None:

        print("Distance:",
              round(distance, 1),
              "cm")

        occupied = (
            distance <
            OCCUPIED_THRESHOLD
        )

        if occupied != last_status:

            last_status = occupied

            if occupied:

                print(
                    "Bay Occupied"
                )

                send_status(True)

            else:

                print(
                    "Bay Empty"
                )

                send_status(False)

    utime.sleep(1)
