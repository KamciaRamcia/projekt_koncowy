
from tkinter import Tk, Button, Toplevel
import interface.interface_memo_game as img
import interface.interface_winner_window as iww

class ButtonWithWord:

    clicked_quantity = 0
    current_pair = []
    lista_buttonow = dict()  # slownik {slowo: przycisk} np. {'dog': .!button2'}
    green_counter = 0
    red_counter = 0
    your_font = "Amatic SC"
    green_colour = 'dark green'
    blue_colour = 'SkyBlue3'
    red_colour = 'red3'

    def __init__(self,value, frame,root, row,column,fishcard_dictionary):
        self.value = value
        self.frame = frame
        self.root = root
        self.row = row
        self.column = column
        self.fishcard_dictionary = fishcard_dictionary

    def createButton(self):

        click_button = Button(self.frame,bg='black',font=(ButtonWithWord.your_font, 13,'bold'), width=40, height=1)
        click_button.grid(row=self.row,column=self.column, padx=1, pady=1)
        click_button.config(command=lambda: self.click_action(click_button))
        ButtonWithWord.lista_buttonow[self.value] = click_button

    def click_action(self, click_button):
        if click_button.cget('bg') != ButtonWithWord.green_colour:  # spr czy przycisk nie zostal juz poprzednio poprawnie dopasowany

            click_button.config(bg=ButtonWithWord.blue_colour)
            click_button.config(text=self.value)
            ButtonWithWord.current_pair.append(self.value)
            ButtonWithWord.clicked_quantity += 1

            if ButtonWithWord.clicked_quantity == 2:
                self.check_pair(click_button)
            elif ButtonWithWord.clicked_quantity > 2:

                ButtonWithWord.lista_buttonow[ButtonWithWord.current_pair[0]].config(bg='black')
                ButtonWithWord.lista_buttonow[ButtonWithWord.current_pair[1]].config(bg='black')
                ButtonWithWord.clicked_quantity = 1
                ButtonWithWord.current_pair = [ButtonWithWord.current_pair[2]]
                click_button.config(bg=ButtonWithWord.blue_colour)

    def check_pair(self, click_button ):
        if (ButtonWithWord.current_pair[0] in self.fishcard_dictionary) and self.fishcard_dictionary[ButtonWithWord.current_pair[0]] == ButtonWithWord.current_pair[1]: # gdy pierwsze wybrane slowo to klucz
            ButtonWithWord.green_counter = ButtonWithWord.green_counter + 1
            self.correct_pair(ButtonWithWord.current_pair[0], ButtonWithWord.current_pair[1])

            ButtonWithWord.clicked_quantity = 0
            ButtonWithWord.current_pair = []

        elif (ButtonWithWord.current_pair[1] in self.fishcard_dictionary) and self.fishcard_dictionary[ButtonWithWord.current_pair[1]] == ButtonWithWord.current_pair[0]:  # gdy drugie wybrane slowo to klucz
            ButtonWithWord.green_counter = ButtonWithWord.green_counter + 1
            self.correct_pair(ButtonWithWord.current_pair[0], ButtonWithWord.current_pair[1])

            ButtonWithWord.clicked_quantity = 0
            ButtonWithWord.current_pair = []

        else:
            ButtonWithWord.red_counter= ButtonWithWord.red_counter + 1
            self.incorrect_pair(ButtonWithWord.current_pair[0], ButtonWithWord.current_pair[1])

    def correct_pair(self, first_element_in_pair, second_element_in_pair ):
        ButtonWithWord.lista_buttonow[first_element_in_pair].config(bg=ButtonWithWord.green_colour)
        ButtonWithWord.lista_buttonow[second_element_in_pair].config(bg=ButtonWithWord.green_colour)

        self.check_if_all_green()

    def incorrect_pair(self, first_element_in_pair, second_element_in_pair ):
        ButtonWithWord.lista_buttonow[first_element_in_pair].config(bg=ButtonWithWord.red_colour)
        ButtonWithWord.lista_buttonow[second_element_in_pair].config(bg=ButtonWithWord.red_colour)

    def check_if_all_green(self):

        if ButtonWithWord.green_counter == len(self.fishcard_dictionary):
            green_and_red_buttons = ButtonWithWord.green_counter + ButtonWithWord.red_counter
            # ustaw wartosci poczatkowe
            ButtonWithWord.green_counter = 0
            ButtonWithWord.red_counter = 0
            ButtonWithWord.lista_buttonow = dict()
            ButtonWithWord.clicked_quantity = 0
            ButtonWithWord.current_pair = []

            img.close_window(self.root)
            iww.winnerInformation(green_and_red_buttons)







