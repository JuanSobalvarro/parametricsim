import turtle
from math import *

def coordrect(entry, a0, a1, escala) -> list: # calcular coordenada rectangular sea x o y
        array = []
        t = a0
        while t < a1:
            string = eval(entry, {'__builtins__': None}, {"t": t, "sen":sin, "cos": cos, "tan": tan, "sqrt": sqrt})
            array.append(string * escala)
            t += 0.1
        return array

def coordpol(entry: str,  a0: int, a1: int, eje: str, escala) -> list: # calcular coordenada polar segun eje puesto
    array = []
    if eje == "x":
        t = a0
        while t < a1:
            val = eval(entry, {'__builtins__': None}, {"t": t, "sen":sin, "cos": cos, "tan": tan, "sqrt": sqrt}) *  cos(t)
            array.append(val * escala)
            t += 0.01
        return array
    elif eje == "y":
        t = a0
        while t < a1:
            val = eval(entry, {'__builtins__': None}, {"t": t, "sen":sin, "cos": cos, "tan": tan, "sqrt": sqrt}) *  sin(t)
            array.append(val * escala)
            t += 0.01
        return array
    else:
        return TypeError
def simturtlearea(cx, cy, velocity, color, minval, maxval):
    turtle.title("Simulation")
    u = turtle.Turtle()
    u.speed(velocity)
    turtle.bgcolor("black")
    x = cx
    y = cy
    for i in range(minval, maxval):
        u.goto(x[i], y[i])
        u.pencolor(color)
        u.goto(0,0)
    turtle.done()

def simturtletrace(cx, cy, velocity, color, minval, maxval):
    turtle.title("Simulation")
    u = turtle.Turtle()
    u.speed(velocity)
    turtle.bgcolor("black")
    x = cx
    y = cy
    u.penup()
    u.goto(x[minval], y[minval])
    u.pendown()
    for i in range(minval, maxval):
        u.goto(x[i], y[i])
        u.pencolor(color)
    turtle.done()