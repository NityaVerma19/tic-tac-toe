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
        heading = Label(self.root ,text = 'TIC TAC TOE', bg = "black" , fg = "white" )
        heading.pack(pady = (20,20))
        heading.configure(font = ("Montserrat" ,32 , 'bold') )




        button = Button(self.root , text= 'PLAY', bg = 'black', fg ="white" ,command=self.on_button_click)
        button.place(relx=0.5, rely=0.5, anchor='center')
        button.configure(font = ('Montserrat', 20 ))


        button2 = Button(self.root, text = 'QUIT', bg = 'black', fg = 'white', command = self.quit_gui)
        button2.place(relx=0.5, rely=0.8, anchor= 'center')
        button2.configure(font=('Montserrat', 20))

    def on_button_click(self):
        print("Button clicked!")

    def quit_gui(self):
        self.root.destroy()

ttt = Ttt()


















