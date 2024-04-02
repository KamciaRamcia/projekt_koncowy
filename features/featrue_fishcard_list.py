import importlib
import os
import tkinter as tk

from interface import interface_memo_game


class NewListElement:

    start_row = 3

    def __init__(self,fishcard_set_name,root):
        self.fishcard_set_name=fishcard_set_name
        self.root = root
        self.lista_buttonow=[]


    def create_elements(self):

        text = importlib.import_module(f'tlumaczenia.{self.fishcard_set_name}') #sciezka w formie textu do przycisku PLAY
        label_name=tk.Label(self.root, text=self.fishcard_set_name)
        label_name.grid(row=NewListElement.start_row, column=1)
        button_play=tk.Button(self.root, text="Play Game", command=lambda: interface_memo_game.memoGame(text.slownik))\

        self.lista_buttonow.append(button_play)
        button_play.grid(row=NewListElement.start_row, column=6)
        button_remove = tk.Button(self.root, text="Remove fishcard set", command=lambda: self.delete_fishcard(button_play, button_remove, label_name))
        self.lista_buttonow.append(button_remove)
        button_remove.grid(row=NewListElement.start_row, column=7)
        NewListElement.start_row = + 1
        print(self.lista_buttonow)



    def delete_fishcard(self,button_play, button_remove,label_name):

        button_play.destroy()
        button_remove.destroy()
        label_name.destroy()

        sciezkaDoPliku = f"../tlumaczenia/{self.fishcard_set_name}.py" # usuwa sie na serio
        if os.path.isfile(sciezkaDoPliku):
             os.unlink(sciezkaDoPliku)
             self.delete_button()

        else:
            print("Wybacz, plik nie istnieje :(")


    def delete_button(self):
        pass






