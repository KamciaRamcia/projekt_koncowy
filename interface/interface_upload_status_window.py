from tkinter import *

import interface.interface_main
from interface import interface_fishcard_list, interface_add_fishcard

global button_image
def uploadStatus(message, isUploaded):   # zmien nazwe na memo_game

    print(f'-------------------{message}')
    root = Tk()
    root.geometry("400x400")
    root.config(bg="skyblue")
    labelBackgroundColour = 'red'
    upload_status_text = 'Nie udało się.'
    your_font = "Amatic SC"
    button_image = PhotoImage(file="../images/button.png")
    if isUploaded ==True:
        labelBackgroundColour = 'green'
        upload_status_text = 'Udało się.'

    Label(root, text=f"{upload_status_text} ", bg=labelBackgroundColour, compound='center', font=(your_font, 16, 'bold')).pack(pady=5)
    Label(root,text=f"{message} ",bg = labelBackgroundColour,compound='center',font=(your_font, 16, 'bold')).pack(pady=5)
    Button(root,font=(your_font, 18,'bold'),width=191, height=50,borderwidth=0,compound='center', image =  button_image,text='Przejdź do listy fiszek', command=lambda: back_to_fishcard_list(root)).pack(pady=5)
    Button(root,font=(your_font, 18,'bold'),width=191, height=50,borderwidth=0,compound='center',image =  button_image, text='Przejdź do menu', command=lambda: back_to_menu(root)).pack(pady=5)
    Button(root,font=(your_font, 18,'bold'),width=191, height=50,borderwidth=0,compound='center',image =  button_image, text='Dodaj fiszki', command=lambda: back_to_upload(root)).pack(pady=5)
    root.mainloop()

def back_to_fishcard_list(root):
    root.destroy()
    interface_fishcard_list.FishCardListPage().get_run()

def back_to_menu(root):
    root.destroy()
    interface.interface_main.FirstPage(Tk()).get_run_first_page()

def back_to_upload(root):
    root.destroy()
    interface_add_fishcard.AddFishcardPage().get_run()


