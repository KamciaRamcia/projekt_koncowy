from tkinter import Tk, Button
#import tlumaczenia.slowa as sl
import interface.interface_memo_game

class Buttony:

    clicked_quantity = 0
    current_pair = []
    lista_buttonow = dict()  # slownik {slowo: przycisk} np. {'dog': .!button2'}


    def __init__(self,value, env,row,column,fishcard_dictionary):
        self.value = value
        self.env = env
        self.row = row
        self.column = column
        self.fishcard_dictionary=fishcard_dictionary

    def createButton(self):

        click_button = Button(self.env,bg='black', width=20)
        click_button.grid(row=self.row,column=self.column) #padx=1, pady=1 - odstep 1pixela od przyciskow
        click_button.config(command=lambda: self.click_action(click_button))
        Buttony.lista_buttonow[self.value] = click_button


    def click_action(self, click_button):
        if click_button.cget('bg') != 'green':  # spr czy przycisk nie zostal juz poprzednio poprawnie dopasowany

            click_button.config(bg='blue')

            click_button.config(text=self.value)
            Buttony.current_pair.append(self.value)
            Buttony.clicked_quantity += 1

            if Buttony.clicked_quantity == 2:
                self.check_pair(click_button)
            elif Buttony.clicked_quantity > 2:

                Buttony.lista_buttonow[Buttony.current_pair[0]].config(bg='black')
                Buttony.lista_buttonow[Buttony.current_pair[1]].config(bg='black')
                Buttony.clicked_quantity = 1
                Buttony.current_pair = [Buttony.current_pair[2]]
                click_button.config(bg='blue')

    def check_pair(self, click_button ):
        if (Buttony.current_pair[0] in self.fishcard_dictionary) and self.fishcard_dictionary[Buttony.current_pair[0]] == Buttony.current_pair[1]: # gdy pierwsze wybrane slowo to klucz
            self.correct_pair(Buttony.current_pair[0])
            self.correct_pair(Buttony.current_pair[1])

            Buttony.clicked_quantity = 0
            Buttony.current_pair = []

        elif (Buttony.current_pair[1] in self.fishcard_dictionary) and self.fishcard_dictionary[Buttony.current_pair[1]] == Buttony.current_pair[0]:  # gdy drugie wybrane slowo to klucz
            self.correct_pair(Buttony.current_pair[0])
            self.correct_pair(Buttony.current_pair[1])

            Buttony.clicked_quantity = 0
            Buttony.current_pair = []

        else:
            self.incorrect_pair(Buttony.current_pair[0])
            self.incorrect_pair(Buttony.current_pair[1])

    def correct_pair(self, zmienna ):
        Buttony.lista_buttonow[zmienna].config(bg='green')

    def incorrect_pair(self, zmienna):
        Buttony.lista_buttonow[zmienna].config(bg='red')










