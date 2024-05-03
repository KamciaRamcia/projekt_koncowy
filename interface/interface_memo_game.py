from tkinter import *

import features.feature_grid_generate
from features import feature_memo_game
import random
from PIL import ImageTk, Image

class MemoGamePage:
    global background_image
    def __init__(self, fishcard_dictionary):
        self.fishcard_dictionary = fishcard_dictionary
        self.root = Tk()
        self.row = 2
        self.column=0
        self.your_font = "Amatic SC"

    def set_window(self):
        self.root.geometry("1600x600")
        self.root.resizable(width=False, height=False)
        MemoGamePage.background_image = PhotoImage(file="../images/fish-extend.gif")
        Label(self.root, image=MemoGamePage.background_image).place(relheight=1, relwidth=1)


    def shuffle_dictionary(self):
        list_to_generate = list(self.fishcard_dictionary.keys()) + (list(self.fishcard_dictionary.values()))
        random.shuffle(list_to_generate)
        return list_to_generate

    def memoGame(self):   # zmien nazwe na memo_game
        self.set_window()
        shuffled_list = self.shuffle_dictionary()

        # stworzenie framu z napisem
        frame1= Frame(self.root,height=20, bg='SkyBlue3')
        frame1.grid(row=0,column=0,padx=10,pady=10)
        Label(frame1, text="Naciskaj kwadraty w celu znlaezienia par slowo-tłumaczenie", bg='SkyBlue1',anchor='center', font=(self.your_font, 15,'bold')).grid(row=1, column=0, padx=5, pady=5)

        # stworzenie framu dla elementow slownika
        frame2=Frame(self.root, bg='SkyBlue1')
        frame2.grid(row=2, column=0,padx=10,pady=10)

        # generowanie siatki
        row_limit=features.feature_grid_generate.calculateRowsQuantity(self.fishcard_dictionary)
        for element in shuffled_list:
            if self.row>=row_limit+2: # umiejscowienie przyciskow w siatce (rzad-kolumna)
                self.column=self.column+1
                self.row=2
            feature_memo_game.ButtonWithWord(element, frame2, self.root, self.row, self.column, self.fishcard_dictionary).createButton()      # tworzenie przycisku
            self.row=self.row+1

    def get_run(self):
        self.set_window()
        self.memoGame()
        self.root.mainloop()

def close_window(root):
    root.destroy()