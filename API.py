from machine import Pin, I2C, time_pulse_us
import utime
from ssd1306 import SSD1306_I2C

# Constants
SOUND_SPEED = 340  # Vitesse du son dans l'air en m/s
TRIG_PULSE_DURATION_US = 10  # Durée de l'impulsion du trigger en microsecondes

# Pins
TRIG_PIN = 15  # Broche GP15 de la Pico
ECHO_PIN = 14  # Broche GP14 de la Pico
SCL_PIN = 17  # Broche SCL pour l'I2C
SDA_PIN = 16  # Broche SDA pour l'I2C

# Initialisation des pins
trig_pin = Pin(TRIG_PIN, Pin.OUT)
echo_pin = Pin(ECHO_PIN, Pin.IN)

# Initialisation de l'I2C et de l'écran OLED
i2c = I2C(0, scl=Pin(SCL_PIN), sda=Pin(SDA_PIN), freq=400000)

# Vérifiez les périphériques I2C connectés
devices = i2c.scan()
if not devices:
    print("Aucun périphérique I2C trouvé")
else:
    for device in devices:
        print("Périphérique I2C trouvé à l'adresse :", hex(device))

# Initialiser l'écran OLED
oled = SSD1306_I2C(128, 64, i2c, addr=0x3C)

def mesure_distance():
    # Prépare le signal
    trig_pin.value(0)
    utime.sleep_us(5)
    
    # Crée une impulsion de 10 µs
    trig_pin.value(1)
    utime.sleep_us(TRIG_PULSE_DURATION_US)
    trig_pin.value(0)

    # Mesure la durée de l'écho en µs
    ultrason_duration = time_pulse_us(echo_pin, 1, 30000)  # Limite de 30ms pour éviter les blocages

    # Calcul de la distance en cm
    distance_cm = SOUND_SPEED * ultrason_duration / 20000  # Diviser par 2*1000*1000/100=20000

    return distance_cm

while True:
    distance = mesure_distance()
    print(f"Distance : {distance:.2f} cm")
    
    # Affiche la distance sur l'écran OLED
    oled.fill(0)  # Efface l'écran
    oled.text(f"Distance:", 0, 0)
    oled.text(f"{distance:.2f} cm", 0, 10)
    oled.show()
    
    utime.sleep(0.5)
