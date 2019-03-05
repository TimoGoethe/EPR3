import tkinter as tk
import tkinter.messagebox as tkm


class Game(tk.Tk):
    def __init__(self, name1, win1, name2, win2):
        tk.Tk.__init__(self)
        self.title("Tic Tac Toe")
        self.name1 = name1
        self.name2 = name2
        self.win1 = win1
        self.win2 = win2
        self.turn = 1
        self.label00 = tk.Label(self, text="An der Reihe ist: ")
        self.label01 = tk.Label(self, text=self.name1)
        self.label1 = tk.Label(self, text="Spieler 1: ")
        self.label2 = tk.Label(self, text="Spieler 2: ")
        self.label3 = tk.Label(self, text=name1)
        self.label4 = tk.Label(self, text=name2)
        self.label5 = tk.Label(self, text=win1)
        self.label6 = tk.Label(self, text=win2)
        self.label7 = tk.Label(self, text="Siege")
        self.label8 = tk.Label(self, text="Siege")
        self.label1.grid()
        self.label2.grid(row=1)
        self.label3.grid(row=0, column=1)
        self.label4.grid(row=1, column=1)
        self.label5.grid(row=0, column=2)
        self.label6.grid(row=1, column=2)
        self.label7.grid(row=0, column=3)
        self.label8.grid(row=1, column=3)
        self.label00.grid(row=2)
        self.label01.grid(row=2, column=1)

        self.buttons = []
        self.field = []
        for i in range(9):
            self.field.append(0)


        self.buttons0 = tk.Button(self, text="", command=self.click0)
        self.buttons0.grid(row=3, column=0)
        self.buttons1 = tk.Button(self, text="", command=self.click1)
        self.buttons1.grid(row=3, column=1)
        self.buttons2 = tk.Button(self, text="", command=self.click2)
        self.buttons2.grid(row=3, column=2)
        self.buttons3 = tk.Button(self, text="", command=self.click3)
        self.buttons3.grid(row=4, column=0)
        self.buttons4 = tk.Button(self, text="", command=self.click4)
        self.buttons4.grid(row=4, column=1)
        self.buttons5 = tk.Button(self, text="", command=self.click5)
        self.buttons5.grid(row=4, column=2)
        self.buttons6 = tk.Button(self, text="", command=self.click6)
        self.buttons6.grid(row=5, column=0)
        self.buttons7 = tk.Button(self, text="", command=self.click7)
        self.buttons7.grid(row=5, column=1)
        self.buttons8 = tk.Button(self, text="", command=self.click8)
        self.buttons8.grid(row=5, column=2)


        self.mainloop()


    def click0(self):
        if self.field[0] == 0:
            self.field[0] = self.turn
            if self.turn == 1:
                self.turn = 2
                self.label01.configure(text=self.name2)
            elif self.turn == 2:
                self.turn = 1
                self.label01.configure(text=self.name1)
            if self.field[0] == 1:
                self.buttons0.configure(bg="blue")
            if self.field[0] == 2:
                self.buttons0.configure(bg="green")
            if self.win(1):
                self.destroy()
                Game(self.name1, self.win1+1, self.name2, self.win2)
            if self.win(2):
                self.destroy()
                Game(self.name1, self.win1, self.name2, self.win2+1)
            if self.win(0): #draw
                self.destroy()
                Game(self.name1, self.win1, self.name2, self.win2)

        else:
            tkm.showwarning("Warning", "Das Feld wurde bereits angeklickt!")


    def click1(self):
        if self.field[1] == 0:
            self.field[1] = self.turn
            if self.turn == 1:
                self.turn = 2
                self.label01.configure(text=self.name2)
            elif self.turn == 2:
                self.turn = 1
                self.label01.configure(text=self.name1)
            if self.field[1] == 1:
                self.buttons1.configure(bg="blue")
            if self.field[1] == 2:
                self.buttons1.configure(bg="green")
            if self.win(1):
                self.destroy()
                Game(self.name1, self.win1 + 1, self.name2, self.win2)
            if self.win(2):
                self.destroy()
                Game(self.name1, self.win1, self.name2, self.win2 + 1)
            if self.win(0): #draw
                self.destroy()
                Game(self.name1, self.win1, self.name2, self.win2)

        else:
            tkm.showwarning("Warning", "Das Feld wurde bereits angeklickt!")


    def click2(self):
        if self.field[2] == 0:
            self.field[2] = self.turn
            if self.turn == 1:
                self.turn = 2
                self.label01.configure(text=self.name2)
            elif self.turn == 2:
                self.turn = 1
                self.label01.configure(text=self.name1)
            if self.field[2] == 1:
                self.buttons2.configure(bg="blue")
            if self.field[2] == 2:
                self.buttons2.configure(bg="green")
            if self.win(1):
                self.destroy()
                Game(self.name1, self.win1 + 1, self.name2, self.win2)
            if self.win(2):
                self.destroy()
                Game(self.name1, self.win1, self.name2, self.win2 + 1)
            if self.win(0): #draw
                self.destroy()
                Game(self.name1, self.win1, self.name2, self.win2)

        else:
            tkm.showwarning("Warning", "Das Feld wurde bereits angeklickt!")


    def click3(self):
        if self.field[3] == 0:
            self.field[3] = self.turn
            if self.turn == 1:
                self.turn = 2
                self.label01.configure(text=self.name2)
            elif self.turn == 2:
                self.turn = 1
                self.label01.configure(text=self.name1)
            if self.field[3] == 1:
                self.buttons3.configure(bg="blue")
            if self.field[3] == 2:
                self.buttons3.configure(bg="green")
            if self.win(1):
                self.destroy()
                Game(self.name1, self.win1 + 1, self.name2, self.win2)
            if self.win(2):
                self.destroy()
                Game(self.name1, self.win1, self.name2, self.win2 + 1)
            if self.win(0): #draw
                self.destroy()
                Game(self.name1, self.win1, self.name2, self.win2)
        else:
            tkm.showwarning("Warning", "Das Feld wurde bereits angeklickt!")


    def click4(self):
        if self.field[4] == 0:
            self.field[4] = self.turn
            if self.turn == 1:
                self.turn = 2
                self.label01.configure(text=self.name2)
            elif self.turn == 2:
                self.turn = 1
                self.label01.configure(text=self.name1)
            if self.field[4] == 1:
                self.buttons4.configure(bg="blue")
            if self.field[4] == 2:
                self.buttons4.configure(bg="green")
            if self.win(1):
                self.destroy()
                Game(self.name1, self.win1 + 1, self.name2, self.win2)
            if self.win(2):
                self.destroy()
                Game(self.name1, self.win1, self.name2, self.win2 + 1)
            if self.win(0): #draw
                self.destroy()
                Game(self.name1, self.win1, self.name2, self.win2)
        else:
            tkm.showwarning("Warning", "Das Feld wurde bereits angeklickt!")


    def click5(self):
        if self.field[5] == 0:
            self.field[5] = self.turn
            if self.turn == 1:
                self.turn = 2
                self.label01.configure(text=self.name2)
            elif self.turn == 2:
                self.turn = 1
                self.label01.configure(text=self.name1)
            if self.field[5] == 1:
                self.buttons5.configure(bg="blue")
            if self.field[5] == 2:
                self.buttons5.configure(bg="green")
            if self.win(1):
                self.destroy()
                Game(self.name1, self.win1 + 1, self.name2, self.win2)
            if self.win(2):
                self.destroy()
                Game(self.name1, self.win1, self.name2, self.win2 + 1)
            if self.win(0): #draw
                self.destroy()
                Game(self.name1, self.win1, self.name2, self.win2)
        else:
            tkm.showwarning("Warning", "Das Feld wurde bereits angeklickt!")


    def click6(self):
        if self.field[6] == 0:
            self.field[6] = self.turn
            if self.turn == 1:
                self.turn = 2
                self.label01.configure(text=self.name2)
            elif self.turn == 2:
                self.turn = 1
                self.label01.configure(text=self.name1)
            if self.field[6] == 1:
                self.buttons6.configure(bg="blue")
            if self.field[6] == 2:
                self.buttons6.configure(bg="green")
            if self.win(1):
                self.destroy()
                Game(self.name1, self.win1 + 1, self.name2, self.win2)
            if self.win(2):
                self.destroy()
                Game(self.name1, self.win1, self.name2, self.win2 + 1)
            if self.win(0): #draw
                self.destroy()
                Game(self.name1, self.win1, self.name2, self.win2)
        else:
            tkm.showwarning("Warning", "Das Feld wurde bereits angeklickt!")


    def click7(self):
        if self.field[7] == 0:
            self.field[7] = self.turn
            if self.turn == 1:
                self.turn = 2
                self.label01.configure(text=self.name2)
            elif self.turn == 2:
                self.turn = 1
                self.label01.configure(text=self.name1)
            if self.field[7] == 1:
                self.buttons7.configure(bg="blue")
            if self.field[7] == 2:
                self.buttons7.configure(bg="green")
            if self.win(1):
                self.destroy()
                Game(self.name1, self.win1 + 1, self.name2, self.win2)
            if self.win(2):
                self.destroy()
                Game(self.name1, self.win1, self.name2, self.win2 + 1)
            if self.win(0): #draw
                self.destroy()
                Game(self.name1, self.win1, self.name2, self.win2)
        else:
            tkm.showwarning("Warning", "Das Feld wurde bereits angeklickt!")


    def click8(self):
        if self.field[8] == 0:
            self.field[8] = self.turn
            if self.turn == 1:
                self.turn = 2
                self.label01.configure(text=self.name2)
            elif self.turn == 2:
                self.turn = 1
                self.label01.configure(text=self.name1)
            if self.field[8] == 1:
                self.buttons8.configure(bg="blue")
            if self.field[8] == 2:
                self.buttons8.configure(bg="green")
            if self.win(1):
                self.destroy()
                Game(self.name1, self.win1 + 1, self.name2, self.win2)
            if self.win(2):
                self.destroy()
                Game(self.name1, self.win1, self.name2, self.win2 + 1)
            if self.win(3): #draw
                self.destroy()
                Game(self.name1, self.win1, self.name2, self.win2)
        else:
            tkm.showwarning("Warning", "Das Feld wurde bereits angeklickt!")


    def win(self, player):
        if player == 1 or player == 2:
            if self.field[0] == player:
                if self.field[1] == player:
                    if self.field[2] == player:
                        return True
            if self.field[3] == player:
                if self.field[4] == player:
                    if self.field[5] == player:
                        return True
            if self.field[6] == player:
                if self.field[7] == player:
                    if self.field[8] == player:
                        return True
            if self.field[0] == player:
                if self.field[3] == player:
                    if self.field[6] == player:
                        return True
            if self.field[1] == player:
                if self.field[4] == player:
                    if self.field[7] == player:
                        return True
            if self.field[2] == player:
                if self.field[5] == player:
                    if self.field[8] == player:
                        return True
            if self.field[0] == player:
                if self.field[4] == player:
                    if self.field[8] == player:
                        return True
            if self.field[2] == player:
                if self.field[4] == player:
                    if self.field[6] == player:
                        return True
        else:
            draw = True
            for i in range(9):
                if self.field[i] == 0:
                    draw = False
            return draw
    def player(self):
        if self.turn == 1:
            return self.name1
        if self.turn == 2:
            return self.name2