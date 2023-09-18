from tkinter import *
import tictactoe as t

class Ttt:
    def __init__(self):
        self.root = Tk()
        self.root.title('TIC TAC TOE')
        self.root.geometry("500x500")
        self.root.configure(bg = "black")

        self.home()

        self.root.mainloop()


    def home(self):
        heading = Label(self.root ,text = 'TIC TAC TOE', bg = "black" , fg = "#C4006E" )
        heading.pack(pady = (20,20))
        heading.configure(font = ("Times New Roman" ,32 , 'bold') )




        button = Button(self.root , text= 'PLAY', bg = 'black', fg ="#C4006E" ,command=self.on_button_click)
        button.place(relx=0.5, rely=0.5, anchor='center')
        button.configure(font = ('Times New Roman', 25 ))


    def on_button_click(self):
        print("Button clicked!")

ttt = Ttt()

















