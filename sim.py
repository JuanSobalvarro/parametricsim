from tkinter import *
from math import *
import turtle
import webbrowser

np = 0.1
queue = 0


def prec(p):
    global np
    np = p

def simulatearea(TurtleObject, entrytype, entry, velocity, color, minval, maxval, scalex, scaley):
    global break_confirm
    t = minval
    TurtleObject.speed(velocity)
    TurtleObject.penup()
    TurtleObject.goto(0,0)
    TurtleObject.pendown()
    TurtleObject.pencolor(color)

    if entrytype == 'polar':
        while t < maxval:

            val = eval(entry, {"t": t, "sin": sin, "sen":sin, "cos": cos, "tan": tan, "sqrt": sqrt})

            TurtleObject.goto(val * scalex * cos(t), val * scaley * sin(t))
            TurtleObject.goto(0,0)
            if break_confirm:
                break_confirm = False
                pass
            t += np
        TurtleObject.penup()
    elif entrytype == 'rect':
        while t < maxval:
            valx = eval(entry[0], {"t": t, "sin": sin, "sen":sin, "cos": cos, "tan": tan, "sqrt": sqrt})
            valy = eval(entry[1], {"t": t, "sin": sin, "sen":sin, "cos": cos, "tan": tan, "sqrt": sqrt})
            
            TurtleObject.goto(valx * scalex, valy * scaley)
            TurtleObject.goto(0,0)
            if break_confirm:
                break_confirm = False
                break
            t += np
        TurtleObject.penup()

def simulatetrace(TurtleObject, entrytype, entry, velocity, color, minval, maxval, scalex, scaley):
    global break_confirm
    TurtleObject.speed(velocity)
    TurtleObject.penup()
    TurtleObject.goto(0,0)
    TurtleObject.pencolor(color)
    t = minval

    if entrytype == 'polar':
        while t < maxval:

            val = eval(entry, {"t": t, "sin": sin, "sen":sin, "cos": cos, "tan": tan, "sqrt": sqrt})

            TurtleObject.goto(val * scalex * cos(t), val * scaley * sin(t))
            if break_confirm:
                break_confirm = False
                break
            TurtleObject.pendown()
            t += np
        TurtleObject.penup()
    elif entrytype == 'rect':
        while t < maxval:

            valx = eval(entry[0], {"t": t, "sin": sin, "sen":sin, "cos": cos, "tan": tan, "sqrt": sqrt})
            valy = eval(entry[1], {"t": t, "sin": sin, "sen":sin, "cos": cos, "tan": tan, "sqrt": sqrt})

            TurtleObject.goto(valx * scalex, valy * scaley)
            if break_confirm:
                break_confirm = False
                break
            TurtleObject.pendown()
            t += np
        TurtleObject.penup()

def setdtype(dt: str):
    global dtype
    dtype = dt
    if dt == "area":
        b3.config(relief=RAISED)
        b2.config(relief=SUNKEN)
    elif dt == "trace":
        b2.config(relief=RAISED)
        b3.config(relief=SUNKEN)

def grapharea(eqtype: str):
    global tcolor
    global queue
    rang0 = int(r0.get())
    rang1 = int(r1.get())
    escaladox = float(escx.get())
    escaladoy = float(escy.get())
    if eqtype == 'polar':
        simulatearea(TurtleObject=tscreen, entrytype=eqtype, entry=er.get(), 
                    velocity=0, color=tcolor, minval=rang0, 
                    maxval=rang1, scalex=escaladox, 
                    scaley=escaladoy)
    elif eqtype == 'rect':
        simulatearea(TurtleObject=tscreen, entrytype=eqtype, entry=[ex.get(), ey.get()], 
                    velocity=0, color=tcolor, minval=rang0, 
                    maxval=rang1, scalex=escaladox, 
                    scaley=escaladoy)
        
    else:
        TypeError

def graphtrace(eqtype: str):
    global tcolor
    global queue
    rang0 = int(r0.get())
    rang1 = int(r1.get())
    escaladox = float(escx.get())
    escaladoy = float(escy.get())
    if eqtype == "polar":
        simulatetrace(TurtleObject=tscreen, entrytype=eqtype, entry=er.get(), 
                    velocity=0, color=tcolor, minval=rang0, 
                    maxval=rang1, scalex=escaladox, 
                    scaley=escaladoy)
    elif eqtype == "rect":
        simulatetrace(TurtleObject=tscreen, entrytype=eqtype, entry=[ex.get(), ey.get()], 
                    velocity=0, color=tcolor, minval=rang0, 
                    maxval=rang1, scalex=escaladox, 
                    scaley=escaladoy)
    else:
        return TypeError

def graph(eqtype):
    global break_confirm
    global queue
    if dtype == "trace":
        graphtrace(eqtype)
    elif dtype == "area":
        grapharea(eqtype)
    else:
        return TypeError

def drawtype(eqt):
    if dtype == "trace":
        graphtrace(eqt)
    elif dtype == "area":
        grapharea(eqt)
    else:
        return TypeError

def set_tcolor(hexcod): #setea el color del turtle
    global tcolor
    tcolor = hexcod

def stop_all(): #cancela trazado
    global break_confirm
    global queue
    break_confirm = True
    tscreen.penup()
    tscreen.goto(0,0)
    tscreen.pendown()
    queue -= 1



break_confirm = False #variable para el break de los trazos
tcolor = "cyan" #color predeterminado turtle
scolor = (0,0,0) #color predeterminado screen del turtle
dtype = "" #variable para el tipo de dibujo
version = 0.1

window = Tk()
window.title("Parametric equations simulator v" + str(version))
window.resizable(True,True)
window.iconbitmap('./img/parametric.ico')
width= window.winfo_screenwidth()               
height= window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))
window.state("zoomed")

"""
menu section
"""
#barra de menu
configbar = Menu(window)
window.config(menu=configbar)

#menus y sus comandos
file_menu = Menu(configbar, tearoff=False) #menu file 

prc_menu = Menu(file_menu, tearoff=False) #submenu nivel de precision de file
prc_menu.add_command(label="Alto(0.001)", command= lambda: prec(0.001))
prc_menu.add_command(label="Medio(0.01)", command= lambda: prec(0.01))
prc_menu.add_command(label="Bajo(0.1)(Recomendado)", command= lambda: prec(0.1))
file_menu.add_cascade(label="Nivel de precision", menu=prc_menu)

file_menu.add_command(label="Help", command= lambda: webbrowser.open_new("https://github.com/JuanSobalvarro/parametricsim"))
file_menu.add_separator()
file_menu.add_command(label="Exit", command= window.destroy)

turtle_menu = Menu(configbar, tearoff=False)#menu de grafica

tcolor_menu = Menu(turtle_menu, tearoff=False) #submenu colores de turtle
tcolor_menu.add_command(label="Black", command= lambda: set_tcolor("#000000"))
tcolor_menu.add_command(label="White", command= lambda: set_tcolor("#ffffff"))
tcolor_menu.add_command(label="Cyan", command= lambda: set_tcolor("#00ffff"))
tcolor_menu.add_command(label="Blue", command= lambda: set_tcolor("#0000ff"))
tcolor_menu.add_command(label="Green", command= lambda: set_tcolor("#00ff00"))
tcolor_menu.add_command(label="Purple", command= lambda: set_tcolor("#ca00d0"))
tcolor_menu.add_command(label="Yellow", command= lambda: set_tcolor("#ffff00"))

scolor_menu = Menu(turtle_menu, tearoff=False) #submenu colores de grafica
scolor_menu.add_command(label="Black", command= lambda: s.bgcolor("#000000"))
scolor_menu.add_command(label="White", command= lambda: s.bgcolor("#ffffff"))
scolor_menu.add_command(label="Cyan", command= lambda: s.bgcolor("#00ffff"))
scolor_menu.add_command(label="Blue", command= lambda: s.bgcolor("#0000ff"))
scolor_menu.add_command(label="Green", command= lambda: s.bgcolor("#00ff00"))
scolor_menu.add_command(label="Purple", command= lambda: s.bgcolor("#ca00d0"))


#agregar los elementos del menu
configbar.add_cascade(label="File", menu=file_menu)
configbar.add_cascade(label="Grafica", menu=turtle_menu)
turtle_menu.add_cascade(label="Color de puntero", menu=tcolor_menu)
turtle_menu.add_cascade(label="Color de fondo", menu=scolor_menu)


"""
Devuelve tscreen que es la pantalla turtle ya con el canva
"""

sectiont = Frame(window, highlightbackground="red", highlightthickness=2)
sectiont.pack(side=RIGHT, fill=BOTH, expand=True)
#sectiont.grid(row=0, column=1, columnspan=2, sticky=N+S+E+W)


#tscreen is the generated turtle screen
ts = Canvas(sectiont, cursor="circle", relief=FLAT, highlightbackground="blue", highlightthickness=2,width=window.winfo_width()*2/3, height=window.winfo_height())
ts.pack(anchor=CENTER, expand=True)
s = turtle.TurtleScreen(ts)
#s.setworldcoordinates(llx = 0, lly = height*2/3, urx = width*2/3, ury = 0) #llx lly urx ury (lower leftx, upper rightx)
s.bgcolor("#ffffff")
tscreen = turtle.RawTurtle(s)




"""
data section
"""
#the data frame is where all the information is going to be enter by the user is
data = Frame(window, highlightbackground="blue", highlightthickness=2)
data.pack(side=LEFT, fill=BOTH, expand=True)
#data.grid(row=0, column=0, columnspan=1, sticky=N+S+E+W)


#labels

l0 = Label(data, text="Ecuaciones de coordenadas", relief="flat",
           borderwidth=3)
l1 = Label(data, text="Ecuacion x =", relief="groove",
           borderwidth=3)
l2 = Label(data, text="Ecuacion y =", relief="groove",
           borderwidth=3)

l3 = Label(data, text="Ecuacion polar", relief="flat",
           borderwidth=3)
l4 = Label(data, text="Ecuacion r =", relief="groove",
           borderwidth=3)
l5 = Label(data, text="Rango del parametro de grafica", relief="flat",
           borderwidth=3)
l6 = Label(data, text="Rango 1:", relief="groove",
           borderwidth=3)
l7 = Label(data, text="Rango 2:", relief="groove",
           borderwidth=3)
l8 = Label(data, text="Escalado de grafica", relief="flat",
           borderwidth=3)
l9 = Label(data, text="Escala x:", relief="groove",
           borderwidth=3)
l10 = Label(data, text="Escala y:", relief="groove",
           borderwidth=3)
l11 = Label(data, text="Seleccione que tipo de grafica quiere", relief="flat",
           borderwidth=3)
l12 = Label(data, text="Limpiar pantalla")
l13 = Label(data, text="Detener simulacion")

#entries

ex = Entry(data, relief="flat",
           borderwidth=0)
ey = Entry(data, relief="flat",
           borderwidth=0)
er = Entry(data, relief="flat",
           borderwidth=0)
r0 = Entry(data, relief="flat",
           borderwidth=0)
r1 = Entry(data, relief="flat",
           borderwidth=0)
escx = Entry(data, relief="flat",
           borderwidth=0)
escy = Entry(data, relief="flat",
           borderwidth=0)

#buttons

b0 = Button(data, text="Resultado", command= lambda: graph("rect"))
b1 = Button(data, text="Resultado", command= lambda: graph("polar"))
b2 = Button(data, text="Area", command= lambda: setdtype("area"))
b3 = Button(data, text="Trazado", command= lambda: setdtype("trace"))
b4 = Button(data, text="Clean", command= lambda: tscreen.clear())
b5 = Button(data, text="Stop", command= lambda: stop_all())

#grideo data

#gridlabels

l0.grid(row=0, column=0, columnspan=2)
l1.grid(row=1, column=0)
l2.grid(row=2, column=0)
l3.grid(row=4, column=0, columnspan=2)
l4.grid(row=5, column=0)
l5.grid(row=0, column=2, columnspan=2)
l6.grid(row=1, column=2)
l7.grid(row=2, column=2)
l8.grid(row=3, column=2, columnspan=2)
l9.grid(row=4, column=2)
l10.grid(row=5, column=2)
l11.grid(row=7, column=0, columnspan=2)
l12.grid(row=9, column=0)
l13.grid(row=9, column=1)

#gridentries

ex.grid(row=1, column=1)
ey.grid(row=2, column=1)
er.grid(row=5, column=1)
r0.grid(row=1, column=3)
r1.grid(row=2, column=3)
escx.grid(row=4, column=3)
escy.grid(row=5, column=3)


#gridbuttons

b0.grid(row= 3, column=1)
b1.grid(row=6, column=1)
b2.grid(row=8, column=0)
b3.grid(row=8, column=1)
b4.grid(row=10, column=0)
b5.grid(row=10, column=1)




window.mainloop()

