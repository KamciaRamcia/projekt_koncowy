import importlib
from tkinter import *
from features import feature_add_fishcard as aff
from interface.interface_memo_game import memoGame

#def show_message(var, dictionary):
#    if var:
#        return var, dictionary

def addFishcard(): # ZMIEN NAZW NA ADD_FISHCARD
    root = Tk()
    root.geometry("600x600")

    frame = Frame(root)
    frame.grid(row=1, column=1)

    Label(frame,text="ADD YOUR SET OF FISHACARDS",bg='blue').grid(row=1, column=2)
    Label(frame, text="Path to your csv file: ").grid(row=2, column=1)
    Label(frame, text="Name of fishcard: ").grid(row=3, column=1)

    # Creating a text box widget
    path_textbox = Text(frame, height=1, width=40)
    path_textbox.grid(row=2, column=2)

    # Creating a text box widget
    fishcard_name_textbox = Text(frame, height=1, width=40)
    fishcard_name_textbox.grid(row=3, column=2)

    def get_input(path_textbox, fishcard_name_textbox):

        fishcard_name = 'nowy slownik'
        path = r"C:\Users\siost\OneDrive\Pulpit\slowka_kuchnia.csv"
        objectowo = aff.NewFishcardSet(path, fishcard_name)
        objectowo.set_of_checks()

     #   if objectowo.is_uploaded:

      #      text=importlib.import_module(f'tlumaczenia.{objectowo.fishcard_set_name}')

       #     Label(frame, text="uploaded succesffully: ").grid(row=5, column=1)
        #    Button(frame, height=1, width=10, text="play", command=lambda: memoGame(text.slownik)).grid(row=4, column=2)


    # Create a button for Comment
    Button(frame, height=1, width=10, text="Comment", command=lambda: get_input(path_textbox, fishcard_name_textbox)).grid(row=4, column=2)

    root.mainloop()