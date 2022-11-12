
import math #Libreria para usar el coseno y seno
#import keyboard 
import serial
from kivy.app import App
#from kivy.uix.label import Label
#from kivy.uix.button import Button
from kivy.uix.widget import Widget
#from kivy.uix.boxlayout import BoxLayout
#from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.graphics.vertex_instructions import Line


#Inmobiliaria Mar De Cortez
#Carlos Octavio Solorzano Aguilar
#Daan Yael Lara Camorlinga 


dis = []
hoy = 0  
stop = 1
size = 1024

ang = []
coor_x = [] #Almacenaje de coordenadas horizontales
coor_y = [] #Almacenaje de coordenadas verticales

coor_linea = [0,0,0,0]

#ser = serial.Serial("com3",9600)


class Withg(Widget):

    coor_texto = StringProperty("")
    linea_texto = str(coor_linea)
    coor_linea = [0,0,0,0]

    def coor_act(self):
        
        ser = serial.Serial("com3",9600)
        while True:
    
               data = ser.readline(size)   

               if data:

                  xd = str(data).replace("\\r\\n'", "")
                  xd1 = str(xd).replace("b'","")
            
               if xd1 == "stop":
                    break;    
               avr = int(xd1)
               dis.append(avr)
               print(dis)



        num_ang = range(0,len(dis))

        num = range(0,len(dis)-1) #Numero de lineas (mas uno que se hara aparte)

        si = 1

        self.coor_linea = [0,0,0,0]

        for e in num_ang:  #Se asignan valores de coordenadas a partir de la distancias y el angulo
            ang.append(e * 360/len(dis))
            coor_x.append(e/len(dis))
            coor_y.append(e/len(dis))

        for a in num_ang:
            coor_x[a] = int (((math.sin((int (ang[a] ) * math.pi)/180))*dis[a] )) #Coordenadas horizontales X
            coor_y[a] = int ((((math.cos((int (ang[a] ) * math.pi)/180))*dis[a]  ) * -1)) #Coordenadas verticales Y  

        self.coor_linea.clear()
    
        for b in num_ang:
            self.coor_linea.append(coor_x[b]+300)
            self.coor_linea.append(coor_y[b]+300)  
            
        self.coor_linea.append(self.coor_linea[0])
        self.coor_linea.append(self.coor_linea[1]) 

        self.oli.points = (self.coor_linea)

        self.coor_texto = str(self.coor_linea)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            self.oli = Line(points=(self.coor_linea))
            self.coor_linea.clear()

        


class funkyApp(App):
    pass 

funkyApp().run()

 

