import pygame
import random

#vamos a crear la ventana

#iniciaizar la biblioteca

pygame.init()

#Definir las dimensiones de la pantlla

dimensiones=(500, 500)


#Hay que poner la varible de las dimensiones en los parentesis para que la ventana no sea infinita y tegas el valor estipulado

miVentana= pygame.display.set_mode(dimensiones)

'''''
while True:
    #Rellenar de rojo
    miVentana.fill((255,0,0))

    #dibujar circulo en mi ventena con el color la psoicion y el radio

    pygame.draw.circle(miVentana, (255,255,255), (250, 250), 50)
    pygame.draw.circle(miVentana, (0,255,255), (250, 250), 40)
    pygame.draw.circle(miVentana, (255,255,0), (250, 250), 30)

    #Actualizar ventana: dar info de que quiero dar de info en la pnatlla, siempre actuaiza en un ciclo si no no funciona
    pygame.display.update()
'''''



#en programacionn basica
x=250
y=250
r=255
g=255
b=255
    
while True:
    #Rellenar de rojo
    miVentana.fill((255,0,0))

    pygame.draw.circle(miVentana, (r,g,b), (x, y), 50)
    #Actualizar ventana: dar info de que quiero dar de info en la pnatlla, siempre actuaiza en un ciclo si no no funciona
    pygame.display.update()

    x=random.randint(1,500)
    y=random.randint(1,500)
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    
 

