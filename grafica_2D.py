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

"""# dibujar una linea rectalinea_1 = c.create_line(BASE/2, ALTURA/2, BASE,0, fill="red", width=2)
linea_2 = c.create_line(BASE, ALTURA, BASE/2, ALTURA/2, fill="yellow", width=2)
linea_3 = c.create_line(0,ALTURA, BASE/2, ALTURA/2, fill="blue", width=2)
linea_4 = c.create_line(0,0, BASE/2,ALTURA/2, fill="green", width=2)
#linea_5 = c.create_line(BASE/2, ALTURA/2, BASE/2, ALTURA, fill="coral", width=2)

# bibujar texto
texto_1 = c.create_text(BASE/4, ALTURA/2, ancho="center", text="Sistemas!", font=("Arial",25, "bold"), fill="blue", activefill="yellow")
texto_2 = c.create_text(3*BASE/4, ALTURA/2, ancho="center", text="Colegio", font=("Arial",25, "bold"), fill="blue", activefill="yellow")
texto_3 = c.create_text(BASE/2, ALTURA/4, anchor="center", text="Especialidad", font=("Arial",25, "bold"), fill="blue", activefill="yellow")
texto_4 = c.create_text(BASE/2, 3*ALTURA/4, anchor="center", text="Guanenta", font=("Arial",25, "bold"), fill="blue", activefill="yellow")

#dibujaar rectandulo
rec_1 = c.create_rectangle(BASE/2, ALTURA/2, BASE, ALTURA, fill="pink", outline="blue")"""

# Cruz
cruz = c.create_line(25+BASE/2,ALTURA/2+75, 25+ALTURA/2,BASE/2+75, ancho="center", fill="red", activedash="blue")
cruz = c.create_polygon(BASE/2-25,ALTURA/2-75,BASE/2+25,ALTURA/2-75,BASE/2+25,ALTURA/2-25, BASE/2+75,ALTURA/2-25, BASE/2+75,ALTURA/2+25, BASE/2+25, ALTURA/2+25, BASE/2+25, ALTURA/2+75, BASE/2-25, ALTURA/2+75, BASE/2-25, ALTURA/2+25, BASE/2-75, ALTURA/2+25, BASE/2-75, ALTURA/2-25, BASE/2-25, ALTURA/2-25, fill="white")

#frame controles
frame_controles = Frame(ventana_principal)
frame_controles.config(bg="green", width=480, height=240)
frame_controles.place(x=10, y=260)

#desplegar ventana
ventana_principal.mainloop()