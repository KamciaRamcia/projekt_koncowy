
from tkinter import *
import interface_memo_game
import interface_add_fishcard
import interface_fishcard_list
import tlumaczenia.slowa as slowa

class FirstPage0:
    global button_image
    global background_image
    def __init__(self, root):
        self.root = root
        self.your_font = "Amatic SC"

    def get_settings(self):

        self.root.geometry("750x400")
        self.root.resizable(width=False, height=False)
        FirstPage0.background_image = PhotoImage(file="../images/fish.gif")
        Label(self.root,image = FirstPage0.background_image).place(relheight=1,relwidth=1)
        FirstPage0.button_image = PhotoImage(file="../images/add_fishcard_tutorial/button.png")

    def get_run_memo_game(self):
        self.root.destroy()
        interface_memo_game.MemoGamePage(slowa.slownik).get_run()

    def get_run_add_fishcard(self):
        self.root.destroy()
        interface_add_fishcard.AddFishcardPage().get_run()

    def get_run_fishcard_list(self):
        self.root.destroy()
        interface_fishcard_list.FishCardListPage().get_run()

    def get_button(self):

        Button(self.root, text="Zagraj w memo", borderwidth=0,image =  FirstPage0.button_image,compound='center',command=lambda:self.get_run_memo_game(), width=191, height=50,font=("Cooper Black", 11)).pack(pady=4)
        Button(self.root, text="Dodaj Fiszki", borderwidth=0, image =  FirstPage0.button_image,compound='center',command=lambda:self.get_run_add_fishcard(),width=191, height=50,font=("Cooper Black", 11)).pack(pady=4)
        Button(self.root, text="Lista Fiszek",borderwidth=0,image =  FirstPage0.button_image,compound='center', command=lambda:self.get_run_fishcard_list(),width=191, height=50,font=("Cooper Black", 11)).pack(pady=4)
        Button(self.root, text="Exit",borderwidth=0, image = FirstPage0.button_image,compound='center', command=self.root.destroy,width=191, height=50,font=("Cooper Black", 11)).pack(pady=4)
    def get_welcome_sign(self):

        welcome_text_frame = Frame(self.root,bg='SkyBlue')
        welcome_text_frame.pack(side=TOP,pady=10)

        Label(welcome_text_frame,text='Witaj!',font=(self.your_font, 15, 'bold'),bg='SkyBlue').pack(pady=5)
        Label(welcome_text_frame,text='Aplikacja pomoże Ci w nauce słówek. Wgraj swoje fiszki, zarządzaj nimi lub zagraj w przykładową gre!', font=(self.your_font, 13,'bold'),bg='SkyBlue').pack(pady=5)

    def get_run_first_page(self):
        self.get_settings()
        self.get_welcome_sign()
        self.get_button()
        self.root.mainloop()

if __name__ == '__main__':
    first = FirstPage0(Tk())
    first.get_run_first_page()