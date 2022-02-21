#Imports
import turtle, time
from tkinter import *
from tkinter import ttk

from drawFunctions import fractal, fractal2

#Instantiate window
root = Tk()
frm = ttk.Frame(root, padding = 10)
frm.grid()

#########Define variables###########
color1 = 33, 37, 41
color2 = 107, 216, 161
color3 = 56, 138, 178
bg = 248, 249, 250
angle = 90
iterations = 2
values = [0, 60, 0]
scale = 400
showturtle = False

#Add elements to frame
ttk.Label(frm, text = "Hello World!").grid(column = 0, row = 0)
ttk.Button(frm, text = "Quit", command = root.destroy).grid(column = 1, row = 0)
#Angle slider
ttk.Scale(frm, variable = angle, from_ = 0, to = 360).grid(column = 0, row = 1)

#Initialize turtle
s = turtle.Screen()
t = turtle.Turtle()
s.colormode(255)
s.setup(width = 1.0, height = 1.0)
t.hideturtle()

#Tutle code
s.bgcolor(bg)
if showturtle == False:
    s.tracer(0,0)

time.sleep(5)

for i in [75]:
    fractal(i, iterations, values, scale, 0, t)
    fractal2(i, iterations, values, scale, 0, t)

turtle.update()
input("This is your fractalz, press enter to continue...")
quit()


#Start frame
#root.mainloop()
