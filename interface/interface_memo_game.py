from tkinter import *
from features import feature_memo_game
import random

def memoGame(fishcard_dictionary):   # zmien nazwe na memo_game
    root = Tk()
    root.geometry("600x600")
    row = 1
    column = 1
    fishcard_dictionary
    list_to_generate = list(fishcard_dictionary.keys()) + (list(fishcard_dictionary.values()))
    random.shuffle(list_to_generate)

    for k in list_to_generate:
        if row>6: # umiejscowienie przyciskow w siatce (rzad-kolumna)
            column=column+1
            row=1
        feature_memo_game.Buttony(k, root, row, column, fishcard_dictionary).createButton()      # tworze przycisk
        row=row+1

    root.mainloop()