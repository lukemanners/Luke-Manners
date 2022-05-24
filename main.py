from tkinter import *
def test():
    print("test")
root = Tk()
button = Button(root, text="test", command=test)
button.pack()
root.mainloop()
