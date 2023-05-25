from tkinter import *

#----------------------
#variables globales
#----------------------
BASE = 460
ALTURA = 220

#------------------------
#ventana principal
#------------------------
ventana_principal = Tk()
ventana_principal.title("Graficas 2D")
ventana_principal.resizable(False, False)
ventana_principal.geometry("500x500")
ventana_principal.config(bg="white")

#--------------------------
#frame de graficas
#--------------------------
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="green", width=480, height=240)
frame_graficacion.place(x=10, y=10)

#creacion canvas
c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.config(bg="black")
c.place(x=10, y=10)

#dibujaar rectandulo
#rec_1 = c.create_rectangle(0,0, BASE/4, ALTURA/2, fill="pink", outline="blue")
#rec_2 = c.create_rectangle(1*0,ALTURA, BASE/4, ALTURA/2, fill="coral", outline="blue")
#rec_3 = c.create_rectangle(BASE/2, ALTURA/2, BASE/4, ALTURA, fill="yellow", outline="blue")
#rec_4 = c.create_rectangle(BASE/4, ALTURA/2, fill="white", outline="blue")

#frame controles
frame_controles = Frame(ventana_principal)
frame_controles.config(bg="green", width=480, height=240)
frame_controles.place(x=10, y=260)

#desplegar ventana
ventana_principal.mainloop()