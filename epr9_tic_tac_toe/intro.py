import tkinter as tk
from game import Game

class Intro(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Tic Tac Toe")
        self.label1 = tk.Label(self, text="Name Spieler 1")
        self.label1.grid()
        self.label2 = tk.Label(self, text="Name Spieler 2")
        self.label2.grid()

        self.entry1 = tk.Entry(self)
        self.entry1.grid(row=0,column=1)
        self.entry2 = tk.Entry(self)
        self.entry2.grid(row=1,column=1)

        self.button1 = tk.Button(self, text="Confirm", command=self.save)
        self.button1.grid()

        self.mainloop()

    def save(self):
        self.name1 = self.entry1.get()
        #print(self.name1)
        self.name2 = self.entry2.get()
        #print(self.name2)
        self.destroy()
        Game(self.name1, 0, self.name2, 0)



