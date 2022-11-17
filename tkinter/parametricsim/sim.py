from tkinter import *
from math import *
from func_algorithm import *

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
    rang0 = int(r0.get())
    rang1 = int(r1.get())
    escaladox = int(escx.get())
    escaladoy = int(escy.get())
    if eqtype == "r":
        simturtlearea(coordrect(ex.get(), rang0, rang1, escaladox), coordrect(ey.get(), rang0, rang1, escaladoy), 0, "cyan", rang0, rang1)
    elif eqtype == "p":
        simturtlearea(coordpol(er.get(), rang0, rang1, "x", escaladox), coordpol(er.get(), rang0, rang1, "y", escaladoy), 0, "cyan", rang0, rang1)
    else:
        return TypeError

def graphtrace(eqtype: str):
    rang0 = int(r0.get())
    rang1 = int(r1.get())
    escaladox = int(escx.get())
    escaladoy = int(escy.get())
    if eqtype == "r":
        simturtletrace(coordrect(ex.get(), rang0, rang1, escaladox), coordrect(ey.get(), rang0, rang1, escaladoy), 0, "cyan", rang0, rang1)
    elif eqtype == "p":
        simturtletrace(coordpol(er.get(), rang0, rang1, "x", escaladox), coordpol(er.get(), rang0, rang1, "y", escaladoy), 0, "cyan", rang0, rang1)
    else:
        return TypeError
def graph(eqtype):
    rang0 = int(r0.get())
    rang1 = int(r1.get())
    escaladox = int(escx.get())
    escaladoy = int(escy.get())
    if dtype == "trace":
        if eqtype == "r":
            simturtletrace(coordrect(ex.get(), rang0, rang1, escaladox), coordrect(ey.get(), rang0, rang1, escaladoy), 0, "cyan", rang0, rang1)
        elif eqtype == "p":
            simturtletrace(coordpol(er.get(), rang0, rang1, "x", escaladox), coordpol(er.get(), rang0, rang1, "y", escaladoy), 0, "cyan", rang0, rang1)
    elif dtype == "area":
        if eqtype == "r":
            simturtlearea(coordrect(ex.get(), rang0, rang1, escaladox), coordrect(ey.get(), rang0, rang1, escaladoy), 0, "cyan", rang0, rang1)
        elif eqtype == "p":
            simturtlearea(coordpol(er.get(), rang0, rang1, "x", escaladox), coordpol(er.get(), rang0, rang1, "y", escaladoy), 0, "cyan", rang0, rang1)
    else:
        return TypeError

def drawtype(eqt):
    if dtype == "trace":
        graphtrace(eqt)
    elif dtype == "area":
        grapharea(eqt)
    else:
        return TypeError

dtype = ""
version = 0.1

window = Tk()
window.title("Parametric equations simulator v" + str(version))
window.resizable(True,True)
window.eval('tk::PlaceWindow . center')

"""
create widgets
"""

#labels

l0 = Label(window, text="Ecuaciones de coordenadas", relief="flat",
           borderwidth=3)
l1 = Label(window, text="Ecuacion x =", relief="groove",
           borderwidth=3)
l2 = Label(window, text="Ecuacion y =", relief="groove",
           borderwidth=3)

l3 = Label(window, text="Ecuacion polar", relief="flat",
           borderwidth=3)
l4 = Label(window, text="Ecuacion r =", relief="groove",
           borderwidth=3)
l5 = Label(window, text="Rango del parametro de grafica", relief="flat",
           borderwidth=3)
l6 = Label(window, text="Rango 1:", relief="groove",
           borderwidth=3)
l7 = Label(window, text="Rango 2:", relief="groove",
           borderwidth=3)
l8 = Label(window, text="Escalado de grafica", relief="flat",
           borderwidth=3)
l9 = Label(window, text="Escala x:", relief="groove",
           borderwidth=3)
l10 = Label(window, text="Escala y:", relief="groove",
           borderwidth=3)
l11 = Label(window, text="Seleccione que tipo de grafica quiere", relief="flat",
           borderwidth=3)

#entries

ex = Entry(window, relief="flat",
           borderwidth=0)
ey = Entry(window, relief="flat",
           borderwidth=0)
er = Entry(window, relief="flat",
           borderwidth=0)
r0 = Entry(window, relief="flat",
           borderwidth=0)
r1 = Entry(window, relief="flat",
           borderwidth=0)
escx = Entry(window, relief="flat",
           borderwidth=0)
escy = Entry(window, relief="flat",
           borderwidth=0)

#buttons

b0 = Button(window, text="Resultado", command= lambda: graph("r"))
b1 = Button(window, text="Resultado", command= lambda: graph("p"))
b2 = Button(window, text="Area", command= lambda: setdtype("area"))
b3 = Button(window, text="Trazado", command= lambda: setdtype("trace"))

"""
grideo
"""

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

window.mainloop()