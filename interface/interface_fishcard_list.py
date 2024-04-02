import importlib
import os
from tkinter import *
import interface_memo_game
from features import featrue_fishcard_list  as ffl

from interface.interface_memo_game import memoGame

start_row=3
def listOfFiles():
    files = os.listdir('../tlumaczenia/')
    files_file = [f for f in files if os.path.isfile(os.path.join('../tlumaczenia/', f))]
    return files_file

def get_play_button():
    pass

def get_delete_button():
    pass

def create_one_row(root,fishcard_name,start_row):
        text = importlib.import_module(f'tlumaczenia.{fishcard_name}') #sciezka w formie textu do przycisku PLAY
        label_name = Label(root, text=fishcard_name).grid(row=start_row, column=1)
        button_play=Button(root, text="Play Game", command=lambda: interface_memo_game.memoGame(text.slownik)).grid(row=start_row,column=6)
        #button_remove = Button(root, text="Remove fishcard set", command=lambda: delete_fishcard()).grid(row=start_row, column=7)
        start_row = + 1




def generateFishcardList(): # ZMIEN NAZW NA ADD_FISHCARD
    root = Tk()
    root.geometry("600x600")



    Label(root,text="Lista Twoich fiszek",bg='blue').grid(row=1, column=2)
    start_row = 3
    for file in listOfFiles():
        print(file)
        dictionary_name = file[:-3]
        print(dictionary_name)
        #create_one_row(root,dictionary_name,start_row)
        ffl.NewListElement(dictionary_name,root).create_elements()



    #Label(root, text="Path to your csv file: ").grid(row=2, column=1)
    #Label(root, text="Name of fishcard: ").grid(row=3, column=1)


    root.mainloop()