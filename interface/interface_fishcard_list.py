import importlib
import os
import interface.interface_main as im
from features.featrue_fishcard_list import NewListElement

from interface.interface_memo_game import *

class FishCardListPage:

    global background_image
    global button_image
    def __init__(self):

        self.root = Tk()


    def set_window(self):
        self.root.geometry("650x750")
        self.root.resizable(width=False, height=False)

        FishCardListPage.button_image = PhotoImage(file="../images/add_fishcard_tutorial/button.png")
        FishCardListPage.background_image = PhotoImage(file="../images/fish.gif")
        Label(self.root, image=FishCardListPage.background_image).place(relheight=1, relwidth=1)

    def listOfFiles(self):
        files = os.listdir('../tlumaczenia/')
        files_file = [f for f in files if os.path.isfile(os.path.join('../tlumaczenia/', f))]
        return files_file

    def get_delete_button(self):
        pass

    def generateFishcardList(self): # ZMIEN NAZW NA ADD_FISHCARD

        # stworzenie framu z tytułem
        Label(self.root, text="Lista Twoich fiszek",bg = 'SkyBlue3', anchor='center',font=("Cooper Black", 15)).grid(padx=5, pady=5,row=0, column=1)

        NewListElement.button_image = PhotoImage(file="../images/add_fishcard_tutorial/button.png")

        for file in self.listOfFiles():
            dictionary_name = file[:-3]
            NewListElement(dictionary_name,self.root).create_elements()

        Button(self.root, text='Wróć do menu głównego',borderwidth=1,
                             image=NewListElement.button_image,
                             compound='center',width=191,font=("Cooper Black", 10), height=25, command=lambda: self.back_to_menu_actions()).grid(row=2, column=1, pady=10)

    def back_to_menu_actions(self):
        self.root.destroy()
        im.FirstPage0(Tk()).get_run_first_page()

    def get_run(self):
        self.set_window()
        self.generateFishcardList()

        self.root.mainloop()