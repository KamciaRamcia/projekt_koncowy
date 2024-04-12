
from tkinter import Tk, Button, Toplevel
import interface.interface_memo_game as img
import interface.interface_winner_window as iww

class Buttony:

    clicked_quantity = 0
    current_pair = []
    lista_buttonow = dict()  # slownik {slowo: przycisk} np. {'dog': .!button2'}
    green_counter = 0
    red_counter = 0

    def __init__(self,value, frame,root, row,column,fishcard_dictionary):
        self.value = value
        self.frame = frame
        self.root = root
        self.row = row
        self.column = column
        self.fishcard_dictionary = fishcard_dictionary


    def createButton(self):

        click_button = Button(self.frame,bg='black', width=40, height=2)
        click_button.grid(row=self.row,column=self.column, padx=1, pady=1)# - odstep 1pixela od przyciskow
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
            Buttony.green_counter = Buttony.green_counter + 1
            self.correct_pair(Buttony.current_pair[0], Buttony.current_pair[1])


            Buttony.clicked_quantity = 0
            Buttony.current_pair = []


        elif (Buttony.current_pair[1] in self.fishcard_dictionary) and self.fishcard_dictionary[Buttony.current_pair[1]] == Buttony.current_pair[0]:  # gdy drugie wybrane slowo to klucz
            Buttony.green_counter = Buttony.green_counter + 1
            self.correct_pair(Buttony.current_pair[0],Buttony.current_pair[1])


            Buttony.clicked_quantity = 0
            Buttony.current_pair = []

        else:
            Buttony.red_counter=Buttony.red_counter+1
            self.incorrect_pair(Buttony.current_pair[0], Buttony.current_pair[1])

    def correct_pair(self, first_element_in_pair, second_element_in_pair ):
        Buttony.lista_buttonow[first_element_in_pair].config(bg='green')
        Buttony.lista_buttonow[second_element_in_pair].config(bg='green')

        self.check_if_all_green()

    def incorrect_pair(self, first_element_in_pair, second_element_in_pair ):
        Buttony.lista_buttonow[first_element_in_pair].config(bg='red')
        Buttony.lista_buttonow[second_element_in_pair].config(bg='red')

    def check_if_all_green(self):

        print(Buttony.green_counter)
        print(len(self.fishcard_dictionary))
        if Buttony.green_counter == len(self.fishcard_dictionary):

            # ustaw wartosci poczatkowe
            Buttony.green_counter = 0
            Buttony.red_counter = 0
            Buttony.lista_buttonow = dict()
            Buttony.clicked_quantity = 0
            Buttony.current_pair = []

            img.close_window(self.root)
            iww.winnerInformation(Buttony.green_counter, Buttony.red_counter)





