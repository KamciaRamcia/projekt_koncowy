import importlib
from tkinter import *

from PIL import ImageTk, Image

from features import feature_add_fishcard as aff
from interface import interface_memo_game as mg
from interface import interface_main as im
class AddFishcardPage:

    global csv_file_screenshot   # obejscie do problemu z wyswietlaniem grafik --  Pytho removes image from memory when image is assigned to local variable (variable created in function). Change variable to global to make it save
    global background_image

    def __init__(self):
        self.root = Tk()
        self.tutorial_start_row = 2
        self.elements_start_row = 6


    def set_window(self):
        self.root.geometry("600x600")
        #self.root.resizable(width=False, height=False)


        AddFishcardPage.background_image = PhotoImage(file="../images/fish.gif")
        Label(self.root, image=AddFishcardPage.background_image).place(relheight=1, relwidth=1)

    def create_title(self):

        Label(self.root, text="DODAJ SWOJE FISZKI", bg='blue').grid(row=1, column=1)
    def elements_for_enter_path(self):

        Label(self.root, text="Ścieżka do pliku csv: ").grid(row=self.elements_start_row, column=1, pady=5, padx=5)
        path_textbox = Text(self.root, height=1, width=70, pady=5)
        path_textbox.grid(row=self.elements_start_row, column=2,pady=5)

    def elements_for_fishcard_name(self):
        Label(self.root, text="Nazwa fiszek: ").grid(row=self.elements_start_row+1, column=1,pady=5)
        fishcard_name_textbox = Text(self.root, height=1, width=70, pady=5)
        fishcard_name_textbox.grid(row=self.elements_start_row+1, column=2,pady=5)

    def elements_for_tutorial(self):
        Label(self.root,borderwidth=0,text="Jak dodać swoją liste fiszek? To bardzo proste! Musisz tylko przestrzegać kilku zasad")#.grid(row=2,column=1,padx=5)

        Label(self.root, text="1. Upewnij się, że Twój plik jest w formacie csv").grid(row=self.tutorial_start_row, column=2,padx=5)
        Label(self.root, text = "2. Upewnij się, że Twój plik zawiera maksymalnie 25 par slowo-tłumaczenie").grid(row=self.tutorial_start_row+1, column=2,padx=5)
        Label(self.root, text = "3. Sprawdź czy pierwszy wiersz w Twoim pliku zawiera nazwę języków, jak na grafice poniżej").grid(row=self.tutorial_start_row+2, column=2,padx=5)

        AddFishcardPage.csv_file_screenshot  =  PhotoImage(file="../images/add_fishcard_tutorial/csv_tutorial_screen.gif")
        Label(self.root, image=AddFishcardPage.csv_file_screenshot, bg='grey').grid(row=self.tutorial_start_row+3, column=2,pady=5)

    def get_input_from_path_textbox(self):
        path = r"C:\Users\siost\OneDrive\Pulpit\slowka_kuchnia.csv"
        return path
    def get_input_from_name_textbox(self):
        fishcard_name = 'nowy1 slownik'
        return fishcard_name
    def run_set_of_checks(self, path, fishcard_name):
        print(path)
        print(fishcard_name)
        check_procedure = aff.NewFishcardSet(path, fishcard_name)
        check_procedure.set_of_checks()
        if check_procedure.is_uploaded:
            text=importlib.import_module(f'tlumaczenia.{check_procedure.fishcard_set_name}')
            Label(self.root, text="uploaded succesffully: ").grid(row=10, column=2, padx=10)
            Button(self.root, height=1, width=10, text="play", command=lambda: mg.MemoGamePage(text.slownik).get_run()).grid(row=11, column=2, padx=10)

    def get_run(self):
        self.set_window()
        self.create_title()
        self.elements_for_enter_path()
        self.elements_for_fishcard_name()
        self.elements_for_tutorial()
        path = self.get_input_from_path_textbox()
        fishcard_name = self.get_input_from_name_textbox()
        self.run_set_of_checks(path, fishcard_name)

        self.root.mainloop()

#def show_message(var, dictionary):
#    if var:
#        return var, dictionary






    # Create a button for Comment
  #  Button(frame, height=1, width=10, text="Comment", command=lambda: get_input(path_textbox, fishcard_name_textbox)).grid(row=4, column=2)

