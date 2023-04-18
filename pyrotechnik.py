#zapamatam si id vybusneho kabla alebo to dam do tag
import random
import tkinter as tk

win = tk.Tk()
colors = ["magenta", "turquoise", "yellow", "orange", "red"]

#ux a uy == lave horne rohy
ux = 70
uy = 100

width = 300
height = 10

wires = []
explosion = 0
pocet = 5
ftime = 100
status = True

def DrawWires():
    global wires, explosion
    for i in range(pocet):
        wires.append(canvas.create_rectangle(ux, uy + height*i, ux+width, uy+height*(i+1), fill=colors[i]))
    explosion = random.choice(wires)

def clicker(e):
    global x, y, status
    if ux < e.x < ux+width and uy < e.y < uy+height*pocet:
        color = canvas.find_overlapping(e.x,e.y,e.x,e.y)[0]
        if color == explosion:
            canvas.create_text(w/2, h-30, text="Vyhral si!", fill="black", font="Arial 25")
            status = False

def changer():
    global ftime
    ftime -= 1
    canvas.itemconfig(t, text=ftime)
    if status == True:
        canvas.after(100, changer)
    if ftime == 0:
        canvas.delete("all")

h, w = 200, 500
canvas = tk.Canvas(win, height=h, width=w, bg="white")
canvas.pack()

t = canvas.create_text(ux+width+35,uy+height*2.5, text=ftime, fill="red", font="Arial 25")

DrawWires()

canvas.create_text(w/2, 50, text="Pyrotechnik", fill="blue",font="Arial 20")
canvas.create_text(w/2, 70, text="označ správny kábel", fill="black",font="Arial 15")

changer()

canvas.bind("<Button-1>", clicker)

win.mainloop()
