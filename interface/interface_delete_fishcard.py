from tkinter import *
import os
import interface_fishcard_list

import interface.interface_memo_game as img

global button_image
def deleteFishcard(dictionary_name):
    root = Tk()
    root.geometry("500x300")
    root.config(bg="skyblue")
    button_image = PhotoImage(file="../images/button.png")


    Label(root, text=f'Czy na pewno chcesz trwale usunac fiszki: {dictionary_name}?').grid(column = 1, row=1, pady=10, padx=10)
    Button(root, text='Tak! Juz ich nie chce na mojej liście',borderwidth=0,image =  button_image,compound='center',width=191, height=50,command = lambda: deleteAllElements(dictionary_name, root)).grid(column = 1, row=2,pady=20)
    Button(root, text='Coo?! Nie chce nic usuwać!!',borderwidth=0,image = button_image,compound='center',width=191, height=50,command=  lambda : back_to_fishcard_list(root)).grid(column = 1, row=4)

    root.mainloop()

def deleteAllElements(dictionary_name, root):
    path_to_file = f"../tlumaczenia/{dictionary_name}.py"  # usuwa sie na serio
    print(path_to_file)
    if os.path.isfile(path_to_file):
        os.unlink(path_to_file)
    back_to_fishcard_list(root)

def back_to_fishcard_list(root):
    root.destroy()
    interface_fishcard_list.FishCardListPage().get_run()


