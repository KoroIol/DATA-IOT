from machine import Pin # importe dans le code la lib qui permet de gerer les Pins de sortie
import utime # importe dans le code la lib qui permet de gerer le temps

pinNumber = 17 # declaration d'une variable pinNumber à 17
led = Pin(pinNumber, mode=Pin.OUT) # declaration d'une variable de type pin ici la 17 
                                   #et on prescise que c'est une pin de sortie de courant (OUT)
pinNumber = 14 # declaration d'une variable pinNumber à 17
led2 = Pin(pinNumber, mode=Pin.OUT) # declaration d'une variable de type pin ici la 14
                                   #et on prescise que c'est une pin de sortie de courant (OUT)
pinNumber = 27 # declaration d'une variable pinNumber à 17
led3 = Pin(pinNumber, mode=Pin.OUT) # declaration d'une variable de type pin ici la 27 
                                   #et on prescise que c'est une pin de sortie de courant (OUT)
while True:          # boucle infini
    led.toggle()     # change l'etat de la led
    utime.sleep(1)   # attendre 1 seconde 
    led.on()        #allume la led 
    led.off()       #eteind la led
         
    led2.toggle()     # change l'etat de la led
    utime.sleep(1)   # attendre 1 seconde 
    led2.on()        #allume la led 
    led2.off()       #eteind la led
        
    led3.toggle()     # change l'etat de la led
    utime.sleep(1)   # attendre 1 seconde 
    led3.on()        #allume la led 
    led3.off()       #eteind la led 
