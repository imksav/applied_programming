import tkinter
from tkinter import *
from tkinter import messagebox

window = tkinter.Tk()
# to rename the title of the window
window.title("GUI")
window.geometry("700x350")
# pack is used to show the object in the window
label = tkinter.Label(window, text="Welcome to Tkinter!").pack()

count = 0


def button_click():
    global count
    count = count + 1
    return messagebox.showinfo(
        title="Output Screen", message=f"Your pressed {count} times."
    )


welcome_button = tkinter.Button(window, text="Click me!!!", command=button_click)


welcome_button.pack()


# main window will be in loop untill it closed
window.mainloop()
