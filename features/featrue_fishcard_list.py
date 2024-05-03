import importlib
import os

from tkinter import *

import interface.interface_delete_fishcard
from interface import interface_memo_game


class NewListElement:

    start_row = 3
    global button_image


    def __init__(self,dictionary_name,root):
        self.dictionary_name=dictionary_name
        self.root = root



    def prepare_image(self):
        NewListElement.button_image = PhotoImage(file="../images/add_fishcard_tutorial/button.png")
    def create_elements(self):

        frame = Frame(self.root, bg='SkyBlue')
        frame.columnconfigure(1, minsize=300)

        frame.grid(row=NewListElement.start_row, column=1, padx=50)
        text = importlib.import_module(f'tlumaczenia.{self.dictionary_name}')  # sciezka w formie textu do przycisku PLAY

        label_name = Label(frame, text=self.dictionary_name ,font=("Sitka Banner", 13))
        label_name.grid(row=NewListElement.start_row, column=1, padx=5, pady=5)

        button_play = Button(frame, text="Zagraj", borderwidth=1,
                             image=NewListElement.button_image,
                             compound='center', command=lambda: self.play_game_actions(text.slownik)
                             ,width=100, height=25,font=("Cooper Black", 10)
                             )
        button_play.grid(row=NewListElement.start_row, column=3, padx=5, pady=5)

        button_remove = Button(frame, text="Usuń zbiór fiszek", borderwidth=1,
                               image=NewListElement.button_image,
                               compound='center', command=lambda: self.delete_actions(),width=125, height=25,font=("Cooper Black", 10))
        button_remove.grid(row=NewListElement.start_row, column=4, padx=5, pady=5)
        print(self.dictionary_name)

        NewListElement.start_row = NewListElement.start_row + 1

    def delete_actions(self):
        self.root.destroy()
        interface.interface_delete_fishcard.deleteFishcard(self.dictionary_name)

    def play_game_actions(self, your_dictionary):
        self.root.destroy()
        interface_memo_game.MemoGamePage(your_dictionary).get_run()









