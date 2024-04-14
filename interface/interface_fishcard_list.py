import importlib
import os
from tkinter import *
import interface_memo_game
from features import featrue_fishcard_list  as ffl
from features.featrue_fishcard_list import NewListElement

from interface.interface_memo_game import *

start_row=3
def listOfFiles():
    files = os.listdir('../tlumaczenia/')
    files_file = [f for f in files if os.path.isfile(os.path.join('../tlumaczenia/', f))]
    return files_file

def get_play_button():
    pass

def get_delete_button():
    pass






def generateFishcardList(): # ZMIEN NAZW NA ADD_FISHCARD
    root = Tk()
    root.geometry("600x600")


    # stworzenie framu z tytułem
    title_frame = Frame(root, height=20)
    title_frame.config(bg='orange')
    title_frame.grid(row=0, column=0, padx=10, pady=10)
    Label(title_frame, text="Lista Twoich fiszek", bg='red', anchor='center').grid(padx=5, pady=5)

    list_frame = Frame(root, height=20)
    list_frame.config(bg='black')
    list_frame.grid(row=2, column=0, padx=10, pady=10)


    start_row = 3
    for file in listOfFiles():
        print(file)
        dictionary_name = file[:-3]
        print(dictionary_name)
        ffl.NewListElement(dictionary_name,list_frame).create_elements()

    root.mainloop()