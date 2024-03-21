from tkinter import *
from tkinter import ttk

import rps
import PokerDice
import hangman

root = Tk()
root.title("Microgames Collection")

mainframe = Frame(root, height= 200, width= 500)
mainframe.pack_propagate(0)
mainframe.pack(padx= 5, pady= 5)

intro = Label(mainframe, text= """Welcome to Microgames Collection.
Please select one of the following games to play:
""")
intro.pack(side = TOP)

rps_button = Button(mainframe, text= "Rock, Paper, Scissors", command = rps.gui)
rps_button.pack()

hm_button = Button(mainframe, text = "Hangman", command = hangman.gui)
hm_button.pack()

pd_button = Button(mainframe, text = "Poker Dice", command = PokerDice.gui)
pd_button.pack()

exit_button = Button(mainframe, text = "Exit", command = root.destroy)
exit_button.pack(side = BOTTOM)

root.mainloop()
