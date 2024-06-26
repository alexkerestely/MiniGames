from tkinter import *
from tkinter.ttk import *
from random import *

word = 0
word_length = 0
clue = 0

def gui():
    global word
    global word_length
    global clue
    global letters_right
    dictionary= ["peach","penguin","chocolate","ramen","purple"]
    word= choice(dictionary)
    word_length = len(word)
    clue = word_length * ["_"]
    tries = 6
    
    def hangedman(hangman):
        graphic = [
            """
+-------+
|
|
|
|
|
==============
""",
"""
+-------+
| |
| O
|
|
|
===============
""",
"""
+-------+
| |
| O
| |
|
|
===============
""",
"""
+-------+
| O
| -|
|
|
|
===============
""",
"""
+-------+
| |
| O
| -|-
|
|
===============
""",
"""
+-------+
| |
| O
| -|-
| /
|
===============
""",
            """
            +-------+
            |       |
            |       O
            |      -|-
            |      / \   
            |       
        ===============
        """, ]
        graphic_set = graphic[hangman]
        hm_graphic.set(graphic_set)

    letters_right = 0

    def game():
        letters_wrong = incorrect_guesses.get()
        letter = guess_letter()
        first_index = word.find(letter)
        if first_index == -1:
            letters_wrong +=1
            incorrect_guesses.set(letters_wrong)
        else:
            global letters_right
            letters_right += 1
            for i in range(word_length):
                if letter == word[i]:
                    clue[i] = letter

        hangedman(letters_wrong)
        clue_set = " ".join(clue)
        word_output.set(clue_set)
        if (letters_wrong + letters_right) == tries:
            result_text = "Game over. The word was " + word
            result_set.set(result_text)
            new_score = computer_score.get()
            new_score += 1
            computer_score.set(new_score)
        if "".join(clue) == word:
            result_text = "Congratulations! The word was " + word
            result_set.set(result_text)
            new_score = player_score.get()
            new_score += 1
            player_score.set(new_score)
            

    def guess_letter():
        letter = letter_guess.get()
        letter.strip()
        letter.lower()
        return letter

    def reset_game():
        global word
        global word_length
        global clue
        incorrect_guesses.set(0)
        hangedman(0)
        result_set.set("")
        letter_guess.set("")
        word= choice(dictionary)
        word_length = len(word)
        clue = word_length * ["_"]
        new_clue = " ".join(clue)
        word_output.set(new_clue)

    hm_window = Toplevel()
    hm_window.title("Hangman")
    incorrect_guesses = IntVar()
    incorrect_guesses.set(0)
    player_score = IntVar()
    computer_score = IntVar()
    result_set = StringVar()
    letter_guess = StringVar()
    word_output = StringVar()
    hm_graphic = StringVar()

    hm_frame = Frame(hm_window, padding = "3 3 12 12", width = 300)
    hm_frame.grid(column = 0, row = 0, sticky = (N,W,E,S))
    hm_frame.columnconfigure(0, weight = 0)
    hm_frame.rowconfigure(0, weight = 0)

    Label(hm_frame, textvariable = hm_graphic).grid(column = 2, row =1)
    Label(hm_frame, text = "Word").grid(column = 2, row =2)
    Label(hm_frame, textvariable = word_output).grid(column = 2, row=3)

    Label(hm_frame, text= "Enter a letter").grid(column = 2, row =1)
    hm_entry = Entry(hm_frame, exportselection = 0, textvariable = letter_guess).grid(column = 2, row =5)
    hm_entry_button = Button(hm_frame, text = "Guess", command = game).grid(column = 2, row = 0)

    Label(hm_frame, text= "Wins").grid(column= 1, row = 7, sticky = W)
    Label(hm_frame, textvariable = player_score).grid(column = 1, row = 8, sticky = W)
    Label(hm_frame, text = "Losses").grid(column = 3, row = 7, sticky = W)
    Label(hm_frame, textvariable = computer_score).grid(column = 3, row = 8 , sticky= W)
    Label(hm_frame, textvariable = result_set).grid(column =2, row = 9)
    replay_button = Button(hm_frame, text = "Reset", command = reset_game).grid(column = 2, row =10)

if __name__ == "__main__":
    gui()
         
