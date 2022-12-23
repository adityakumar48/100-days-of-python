from tkinter import *

window = Tk()

window.title("My first GUI program")
window.minsize(width=500, height=300)


# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()


def button_clicked():
    print("I got clicked")
    my_label.config(text=input.get())

# Button


button = Button(text="Click Me", command=button_clicked)

button.pack()
# Entry

input = Entry(width=10)
input.pack()


window.mainloop()
