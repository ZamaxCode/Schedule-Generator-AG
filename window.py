from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1300x1000")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 1000,
    width = 1300,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 152, y = 1230,
    width = 398,
    height = 74)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 152, y = 1130,
    width = 398,
    height = 74)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    302.5, 835.5,
    image=background_img)

window.resizable(False, False)
window.mainloop()
