from tkinter import *

import interface_memo_game
import interface_add_fishcard
import interface_fishcard_list
#import tlumaczenia.slowa as slowa

class FirstPage0:

    def __init__(self, root):
        self.root = root

    def get_settings(self):
        # Window settings
        self.root.geometry("100x200")

    def get_run_memo_game(self):
        self.root.destroy()
        interface_memo_game.memoGame(slowa.slownik)

    def get_run_add_fishcard(self):
        self.root.destroy()
        interface_add_fishcard.addFishcard()

    def get_run_fishcard_list(self):
        self.root.destroy()
        interface_fishcard_list.generateFishcardList()

    def get_button(self):
        # Add buttons
        Button(self.root, text="Play example memo", command=lambda:self.get_run_memo_game()).pack()
        Button(self.root, text="Dodaj Fiszki", command=lambda:self.get_run_add_fishcard()).pack()
        Button(self.root, text="Moje Fiszki", command=lambda:self.get_run_fishcard_list()).pack()
        Button(self.root, text="Exit", command=self.root.destroy).pack()

    def get_run_first_page(self):
        # Launching the application
        self.get_settings()
        self.get_button()
        self.root.mainloop()

if __name__ == '__main__':
    first = FirstPage0(Tk())
    first.get_run_first_page()