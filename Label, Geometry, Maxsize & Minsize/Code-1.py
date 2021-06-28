from tkinter import *

root = Tk()

# Width x Height
root.geometry("644x434")

# width, height
root.minsize(300,100)

# width, height
root.maxsize(1200, 988)

sx = Label(text="This is the GUI")
sx.pack()


root.mainloop()
