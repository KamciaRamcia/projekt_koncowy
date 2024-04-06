from tkinter import *

import interface_memo_game
import interface_add_fishcard
import interface_fishcard_list
import tlumaczenia.slowa as slowa
import tksvg



class FirstPage0:

    def __init__(self, root):
        self.root = root


    def get_settings(self):
        # Window settings
        self.root.geometry("600x300")

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
        Button(self.root, text="Zagraj w memo", command=lambda:self.get_run_memo_game(), width=20, height=2).pack(pady=4)
        Button(self.root, text="Dodaj Fiszki", command=lambda:self.get_run_add_fishcard(),width=20, height=2).pack(pady=4)
        Button(self.root, text="Zarządzaj fiszkami", command=lambda:self.get_run_fishcard_list(),width=20, height=2).pack(pady=4)
        Button(self.root, text="Exit", command=self.root.destroy,width=20, height=2).pack(pady=4)
    def get_welcoem_sign(self):
        Label(self.root,text='Witaj!').pack(pady=5)
        Label(self.root, text='Aplikacja pomoże Ci w nauce słówek, Wgraj swoje fiszki, zarządzaj nimi lub zagraj w przykładową gre!').pack(pady=5)

    def get_run_first_page(self):
        # Launching the application
        self.get_settings()
        self.get_welcoem_sign()

        self.get_button()
        self.root.mainloop()

if __name__ == '__main__':
    first = FirstPage0(Tk())
    first.get_run_first_page()