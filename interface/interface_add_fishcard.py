import importlib
from tkinter import *

from PIL import ImageTk, Image

from features import feature_add_fishcard as aff
from interface import interface_memo_game as mg

class AddFishcardPage:

    def __init__(self):
        self.root = Tk()
        self.title_frame = Frame(self.root)
        self.elements_frame = Frame(self.root)
        self.success_frame = Frame(self.root)
        self.tutorial_frame = Frame(self.root)

    def set_window(self):
        self.root.geometry("600x600")
        self.root.configure(bg='skyblue')
        self.title_frame.grid(row=1, column=1, pady=5)
        self.tutorial_frame.grid(row=2, column=1, pady=5, padx=20)
        self.elements_frame.grid(row=3, column=1, pady=5)
        self.success_frame.grid(row=5, column=1,pady=5)


    def create_title(self):

        Label(self.title_frame, text="DODAJ SWOJE FISZKI", bg='blue').grid(row=1, column=2)
    def elements_for_enter_path(self):

        Label(self.elements_frame, text="Ścieżka do pliku csv: ").grid(row=2, column=1, pady=5)
        path_textbox = Text(self.elements_frame, height=1, width=40, pady=5)
        path_textbox.grid(row=2, column=2)

    def elements_for_fishcard_name(self):
        Label(self.elements_frame, text="Nazwa fiszek: ").grid(row=3, column=1,pady=5)
        fishcard_name_textbox = Text(self.elements_frame, height=1, width=40, pady=5)
        fishcard_name_textbox.grid(row=3, column=2)

    def elements_for_tutorial(self):
        Label(self.tutorial_frame,text="Jak dodać swoją liste fiszek? To bardzo proste! Musisz tylko przestrzegać kilku zasad").grid(row=1,column=1,padx=5)
        Label(self.tutorial_frame, text="1. Upewnij się, że Twój plik jest w formacie csv").grid(row=2, column=1,padx=5)
        Label(self.tutorial_frame, text = "2. Upewnij się, że Twój plik zawiera maksymalnie 25 par slowo-tłumaczenie").grid(row=3, column=1,padx=5)
        Label(self.tutorial_frame, text = "3. Sprawdź czy pierwszy wiersz w Twoim pliku zawiera nazwę języków, jak na grafice poniżej").grid(row=4, column=1,padx=5)
        csv_screenshot = ImageTk.PhotoImage(Image.open("../images/add_fishcard_tutorial/csv_tutorial_screen.png"))
        #MIEJJSCE NA SCREENA JAK JUZ OGARNIESZ JAK WSTAWIAĆ TE GŁUPIE OBRAZY
       # rejestracja_button = PhotoImage(file="../images/button.png")
       # rejestracja = Label(self.tutorial_frame, text="", image=csv_screenshot, height=50, width=200)
       # rejestracja.place(x=1, y=3)

        #label = Label(self.tutorial_frame, text="Image", image=csv_screenshot, compound="top")
        #label = Label(self.tutorial_frame,image=csv_screenshot)
        #label.grid()

    def get_input_from_path_textbox(self):
        path = r"C:\Users\siost\OneDrive\Pulpit\slowka_kuchnia.csv"
        return path
    def get_input_from_name_textbox(self):
        fishcard_name = 'nowy slownik'
        return fishcard_name
    def run_set_of_checks(self, path, fishcard_name):
        print(path)
        print(fishcard_name)
        check_procedure = aff.NewFishcardSet(path, fishcard_name)
        check_procedure.set_of_checks()
        if check_procedure.is_uploaded:
            text=importlib.import_module(f'tlumaczenia.{check_procedure.fishcard_set_name}')
            Label(self.success_frame, text="uploaded succesffully: ").grid(row=5, column=1)
            Button(self.success_frame, height=1, width=10, text="play", command=lambda: mg.MemoGamePage(text.slownik).get_run()).grid(row=4, column=2)

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

