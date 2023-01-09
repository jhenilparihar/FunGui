from tkinter import *
import random

x_place = 200
y_place = 130


def changeOnHover(button):
    button.bind("<Enter>", func=lambda e: change_position())


def change_position():
    global x_place, y_place
    while True:
        y = random.randint(80, 180)
        if y_place - 30 > y or y > y_place + 30:
            break
    while True:
        x = random.randint(150, 250)
        if x_place - 30 > x or x > x_place + 30:
            break
    x_place = x
    y_place = y
    no.place(x=x, y=y)


window = Tk()
window.config(padx=30, pady=50)
window.title('Flashing Card')
window.geometry("400x300")

Label(window, text="Are u Dumb?", font=('SanSerif', 40, 'bold'), ).grid(column=0, row=0)

yes = Button(window, text="Yes", width=7, font="SanSerif 15", bg="#E0E0E0", border=1, relief="solid")
no = Button(window, text="No", width=7, font="SanSerif 15", bg="#E0E0E0", border=1, relief="solid",
            command=change_position)
yes.place(x=35, y=130)
no.place(x=200, y=130)

changeOnHover(no)


window.mainloop()
