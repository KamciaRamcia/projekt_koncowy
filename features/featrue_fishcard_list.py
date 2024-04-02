import importlib
import os
import tkinter as tk

from interface import interface_memo_game


class NewListElement:

    start_row = 3

    def __init__(self,fishcard_set_name,root):
        self.fishcard_set_name=fishcard_set_name
        self.root = root

    def create_elements(self):

        text = importlib.import_module(f'tlumaczenia.{self.fishcard_set_name}') #sciezka w formie textu do przycisku PLAY
        label_name=tk.Label(self.root, text=self.fishcard_set_name).grid(row=NewListElement.start_row, column=1)
        button_play=tk.Button(self.root, text="Play Game", command=lambda: interface_memo_game.memoGame(text.slownik)).grid(row=NewListElement.start_row,column=6)
        button_remove = tk.Button(self.root, text="Remove fishcard set", command=lambda: self.delete_fishcard()).grid(row=NewListElement.start_row, column=7)
        NewListElement.start_row = + 1

    def delete_fishcard(self):
        print('****')
        print(os.listdir())

        sciezkaDoPliku = "../tlumaczenia/slowa.py"
        if os.path.isfile(sciezkaDoPliku):
            os.unlink(sciezkaDoPliku)
        else:
            print("Wybacz, plik nie istnieje :(")

    def delete_button(self):
        pass





