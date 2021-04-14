from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox

class tres_en_raya():
    def __init__(self):
        self.jugador1="jugador1"
        self.jugador2="jugador2"
        self.ficha="ficha"
        self.jugador1=False
        self.jugador2=False
        self.X=0
        self.O=0
        self.colocacion=True
    
    def colocar_fichas(self,x,y,b,c):
      if self.colocacion==True:#colocación de las trés fichas de cada jugador
        if self.O<3 or self.X<3:#condicion para completar las tres fichas de cada jugador
          if self.jugador1==True:#turno del primer jugador
            if  c.get()==" ":
              c.set("X")
              b=Button(self.raiz, textvariable=c,text=c,foreground = "red",bd=3,width=10,height=4,command=lambda:tres.colocar_fichas(x,y,b,c)).grid(padx=10, row=x, column=y)
              self.jugador1=False# termina turno de jugador1
              self.jugador2=True #dá paso el turno del jugador2
              self.X=self.X+1
            elif c.get()=="O":
              print("esa ficha no es tuya, prueba otro movimiento")
            else:
              print("Aquí ya tienes una ficha tuya, coloca primero tus trés fichas")
          
          elif self.jugador2==True:
            if c.get()==" ":
              c.set("O")
              b=Button(self.raiz, textvariable=c,text=c,foreground = "blue", bd=3,width=10,height=4,command=lambda:tres.colocar_fichas(x,y,b,c)).grid(padx=10, row=x, column=y)
              self.jugador2=False
              self.jugador1=True
              self.O=self.O+1
              print(self.O)
            elif c.get()=="X":
              print("esa ficha no es tuya, prueba otro movimiento")
            else:
              print("Aquí ya tienes una ficha tuya, coloca primero tus trés fichas")
          else:
            print("pulsa start para comenzar")
        else:
          self.colocacion=False
      
      elif self.colocacion==False:#aqui la condición cuandose ha terminado de colocar las fichas empezaria el juego
        if c.get()=="X":
          print("esta es una X")
        elif c.get()=="O":
          print("es una O")
        elif c.get()==" ":
          print("esta casilla aparece en blanco")  
        else:
          print(self.b1['texto'])
          print("en esta casilla no hay ficha intenta de nuevo:")
          #tres.cambio_botones""""()
        #aqui colocamos el final de la funcion de cambio_botones
      else:
        print("algo raro pasa")
    
    def start(self):
      self.jugador1=True
      Button(self.raiz,text="START",background = "gray",foreground = "red",command=tres.start,state=DISABLED).grid(padx=10,row=5,column=2)
      self.turno.set("Buena Suerte!!")
      self.texto1.set(" ")
      self.texto2.set(" ")
      self.texto3.set(" ")
      self.texto4.set(" ")
      self.texto5.set(" ")
      self.texto6.set(" ")
      self.texto7.set(" ")
      self.texto8.set(" ")
      self.texto9.set(" ")





    
      
    def juego(self,x,y):
      self.turno.set("Esto funciona")




    def interfaz(self):#pantalla interfaz principal
      self.raiz=Tk()
      self.nombre_usuario="Bienvenido!!!"
      self.raiz.geometry("320x345+0+0")
      self.turno=StringVar()
      self.texto1=StringVar()
      self.texto2=StringVar()
      self.texto3=StringVar()
      self.texto4=StringVar()
      self.texto5=StringVar()
      self.texto6=StringVar()
      self.texto7=StringVar()
      self.texto8=StringVar()
      self.texto9=StringVar()


      self.turno.set("presione start")

      self.raiz.title(self.nombre_usuario)
      Label(self.raiz,text='Trés en Raya',bg="black",fg="white",width=30).grid(padx=10, row=0, column=1,columnspan=4)
      Label(self.raiz,text=" ").grid(padx=10, row=1,column=0)
      self.b1=Button(self.raiz,textvariable=self.texto1, text=self.texto1,width=10,height=4,command=lambda:tres.colocar_fichas(2,1,self.b1,self.texto1)).grid(padx=10, row=2, column=1)
      self.b2=Button(self.raiz,textvariable=self.texto2, text=self.texto2,width=10,height=4,command=lambda:tres.colocar_fichas(2,2,self.b2,self.texto2)).grid(padx=10, row=2, column=2)
      self.b3=Button(self.raiz,textvariable=self.texto3, text=self.texto3,width=10,height=4,command=lambda:tres.colocar_fichas(2,3,self.b3,self.texto3)).grid(padx=10, row=2, column=3)
      self.b4=Button(self.raiz,textvariable=self.texto4, text=self.texto4,width=10,height=4,command=lambda:tres.colocar_fichas(3,1,self.b4,self.texto4)).grid(padx=10, row=3, column=1)
      self.b5=Button(self.raiz,textvariable=self.texto5, text=self.texto5,width=10,height=4,command=lambda:tres.colocar_fichas(3,2,self.b5,self.texto5)).grid(padx=10, row=3, column=2)
      self.b6=Button(self.raiz,textvariable=self.texto6, text=self.texto6,width=10,height=4,command=lambda:tres.colocar_fichas(3,3,self.b6,self.texto6)).grid(padx=10, row=3, column=3)
      self.b7=Button(self.raiz,textvariable=self.texto7, text=self.texto7,width=10,height=4,command=lambda:tres.colocar_fichas(4,1,self.b7,self.texto7)).grid(padx=10, row=4, column=1)
      self.b8=Button(self.raiz,textvariable=self.texto8, text=self.texto8,width=10,height=4,command=lambda:tres.colocar_fichas(4,2,self.b8,self.texto8)).grid(padx=10, row=4, column=2)
      self.b9=Button(self.raiz,textvariable=self.texto9, text=self.texto9,width=10,height=4,command=lambda:tres.colocar_fichas(4,3,self.b9,self.texto9)).grid(padx=10, row=4, column=3)
      Label(self.raiz,text="").grid(padx=10)
      Button(self.raiz,text="START",background = "green",foreground = "white",command=tres.start).grid(padx=10,row=5,column=2)
      self.t=Label(self.raiz,textvariable=self.turno,text=self.turno).grid(row=6,column=2)
         
      self.raiz.mainloop()


tres=tres_en_raya()
tres.interfaz()




