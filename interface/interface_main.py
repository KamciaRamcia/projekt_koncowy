
from tkinter import *
import interface_add_fishcard
import interface_fishcard_list
import example_Fishcard.slowa as slowa
import interface.interface_memo_game as img


class FirstPage:
    global button_image # obejscie do problemu z wyswietlaniem grafik --  Python removes image from memory when image is assigned to local variable (variable created in function). Change variable to global to make it save
    global background_image
    your_font = "Amatic SC"
    def __init__(self, root):
        self.root = root

    def get_settings(self):

        self.root.geometry("750x400")
        self.root.resizable(width=False, height=False)
        FirstPage.background_image = PhotoImage(file="../images/fish.gif")
        Label(self.root, image = FirstPage.background_image).place(relheight=1, relwidth=1)
        FirstPage.button_image = PhotoImage(file="../images/button.png")

    def get_run_memo_game(self):
        self.root.destroy()
        img.MemoGamePage(slowa.slownik).get_run()

    def get_run_add_fishcard(self):
        self.root.destroy()
        interface_add_fishcard.AddFishcardPage().get_run()

    def get_run_fishcard_list(self):
        self.root.destroy()
        interface_fishcard_list.FishCardListPage().get_run()

    def get_button(self):

        Button(self.root, text="Zagraj w przykladową grę", borderwidth=0, image =  FirstPage.button_image, compound='center', command=lambda:self.get_run_memo_game(), width=191, height=50, font=(FirstPage.your_font, 18, 'bold')).pack(pady=4)
        Button(self.root, text="Dodaj Fiszki", borderwidth=0, image =  FirstPage.button_image, compound='center', command=lambda:self.get_run_add_fishcard(), width=191, height=50, font=(FirstPage.your_font, 18, 'bold')).pack(pady=4)
        Button(self.root, text="Lista Fiszek", borderwidth=0, image =  FirstPage.button_image, compound='center', command=lambda:self.get_run_fishcard_list(), width=191, height=50, font=(FirstPage.your_font, 18, 'bold')).pack(pady=4)
        Button(self.root, text="Wyjście", borderwidth=0, image = FirstPage.button_image, compound='center', command=self.root.destroy, width=191, height=50, font=(FirstPage.your_font, 18, 'bold')).pack(pady=4)
    def get_welcome_sign(self):

        welcome_text_frame = Frame(self.root,bg='SkyBlue')
        welcome_text_frame.pack(side=TOP,pady=10)

        Label(welcome_text_frame,text='Witaj!',font=(FirstPage.your_font, 15, 'bold'),bg='SkyBlue').pack(pady=5)
        Label(welcome_text_frame,text='Aplikacja pomoże Ci w nauce słówek. Wgraj swoje fiszki, zarządzaj nimi lub zagraj w grę Memo.', font=(FirstPage.your_font, 13,'bold'),bg='SkyBlue').pack(pady=5)

    def get_run_first_page(self):
        self.get_settings()
        self.get_welcome_sign()
        self.get_button()
        self.root.mainloop()

if __name__ == '__main__':

    first = FirstPage(Tk())
    first.get_run_first_page()