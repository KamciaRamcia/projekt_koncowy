import importlib
import os
from tkinter import *
import interface_memo_game
from features import featrue_fishcard_list  as ffl

from interface.interface_memo_game import memoGame

def listOfFiles():
    files = os.listdir('../tlumaczenia/')
    files_file = [f for f in files if os.path.isfile(os.path.join('../tlumaczenia/', f))]
    return files_file

def create_one_row(root,fishcard_name):
    #Label(root, text="Path to your csv file: ").grid(row=3, column=1)
    pass


def generateFishcardList(): # ZMIEN NAZW NA ADD_FISHCARD
    root = Tk()
    root.geometry("600x600")


    Label(root,text="Lista Twoich fiszek",bg='blue').grid(row=1, column=2)
    start_row = 3
    for file in listOfFiles():
        print(file)
        dictionary_name = file[:-3]
        print(dictionary_name)
        ffl.NewListElement(dictionary_name,root).create_elements()



    #Label(root, text="Path to your csv file: ").grid(row=2, column=1)
    #Label(root, text="Name of fishcard: ").grid(row=3, column=1)


    root.mainloop()