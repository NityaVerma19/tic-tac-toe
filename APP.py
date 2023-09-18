from tkinter import *
import tictactoe as t

class Ttt:
    def __init__(self):
        self.root = Tk()
        self.root.title('TIC TAC TOE')
        self.root.geometry("500x500")
        self.root.configure(bg = "black")
        self.root.mainloop()
    def home(self):
        heading = Label(self.root ,text = 'TIC TAC TOE', bg = "black" , fg = "white" )
        heading.pack(pady = (20,20))
        heading.configure(font = ("Times New Roman" ,32 , 'bold') )

ttt = Ttt()

















