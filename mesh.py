import random
from tkinter import *
from PIL import ImageTk, Image


class Punkt():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Ziarno():

    def __init__(self, arrayZ):
        self.array = arrayZ  # tabela z pikselami ziarem


###### KOD DO OBRAZKA
root = Tk()
root.title("Mesh Generator")
backgroundImage = Image.open("zdj.jpg")
w, h = backgroundImage.size  # w - szerokosc h -wysokosc

canvas = Canvas(root, width=w, height=h, bg='white')
canvas.grid(row=4, column=6)
zdj = ImageTk.PhotoImage(backgroundImage)
canvas.create_image(0, 0, anchor=NW, image=zdj)
canvas.pack()


def pixelRandom(event):
    canvas.create_image(0, 0, anchor=NW, image=zdj)
    pR = []
    xR = random.randrange(0, w)
    yR = random.randrange(0, h)

    for x in range(w):
        for y in range(h):
            if p[x, y] == p[xR, yR]:
                new = Punkt(x, y)
                pR.append(new)

    ziarno = Ziarno(pR)
    mesh(ziarno)


button = Button(root, text="Mesh")
button.pack()

root.bind("<Button 1>", pixelRandom)
p = backgroundImage.load()


def mesh(ziarno):
    arrayX = []
    arrayY = []
    dlugosc = len(ziarno.array)
    for i in range(dlugosc):
        arrayX.append(ziarno.array[i].x)
        arrayY.append(ziarno.array[i].y)
    xM = max(arrayX)
    yM = max(arrayY)
    x = min(arrayX)
    y = min(arrayY)
    y0 = y
    A = (xM - x) / 10  # ilosc podzialow siatki
    B = (yM - y) / 10

    while x < xM:
        while y < yM:
            canvas.create_line(x, y, x + A, y, fill='black')
            canvas.create_line(x, y, x, y + B, fill='black')
            canvas.create_line(x, y, x + A, y + B, fill='black')

            y += B
        y = y0
        x += A


root.mainloop()
