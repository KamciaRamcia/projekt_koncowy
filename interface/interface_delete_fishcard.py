import os
from tkinter import *

import interface_fishcard_list
from features.feature_delete_fishcard import deleteAllElements


def deleteFishcard(dictionary_name):
    root = Tk()
    root.geometry("500x300")
    root.config(bg="skyblue")
    button_image = PhotoImage(file="../images/button.png")
    your_font = "Amatic SC"

    Label(root, font=(your_font, 20, 'bold'),
          text=f'Czy na pewno chcesz trwale usunac fiszki: {dictionary_name}?').grid(column=1, row=1, pady=10, padx=10)
    Button(root, font=(your_font, 13, 'bold'), text='Tak! Juz ich nie chce na mojej liście', borderwidth=0,
           image=button_image, compound='center', width=191, height=50,
           command=lambda: deleteAllElementsAndExit(dictionary_name, root)).grid(column=1, row=2, pady=20)
    Button(root, font=(your_font, 13, 'bold'), text='Coo?! Nie chce nic usuwać!!', borderwidth=0, image=button_image,
           compound='center', width=191, height=50, command=lambda: back_to_fishcard_list(root)).grid(column=1, row=4)

    root.mainloop()


def deleteAllElementsAndExit(dictionary_name, root):
    deleteAllElements(dictionary_name)
    back_to_fishcard_list(root)


def back_to_fishcard_list(root):
    root.destroy()
    interface_fishcard_list.FishCardListPage().get_run()
