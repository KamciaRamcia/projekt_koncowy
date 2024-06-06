from tkinter import *
from tkinter import filedialog

import interface.interface_upload_status_window
import interface_fishcard_list
from features import feature_add_fishcard as aff


class AddFishcardPage:
    your_font = "Amatic SC"

    def __init__(self):
        self.root = Tk()
        self.cur_row = 2

    def set_window(self):
        self.root.geometry("750x600")
        self.root.resizable(width=False, height=False)

        AddFishcardPage.background_image = PhotoImage(file="../images/fish.gif")
        AddFishcardPage.button_image = PhotoImage(file="../images/button.png")
        AddFishcardPage.csv_file_screenshot = PhotoImage(file="../images/add_fishcard_tutorial/csv_tutorial_screen.gif")
        Label(self.root, image=AddFishcardPage.background_image).place(relheight=1, relwidth=1)

    def create_title(self):
        Label(self.root, text="DODAJ SWOJE FISZKI", bg='SkyBlue', font=(AddFishcardPage.your_font, 15, 'bold')).grid(
            row=1, column=2, pady=10)

    def find_file_path(self, path_textbox):
        findedFilePath = filedialog.askopenfilename()
        path_textbox.insert(INSERT, findedFilePath)
        path_textbox.grid()

    def elements_for_input_box(self):
        elements_start_row = self.cur_row
        Label(self.root, text="Ścieżka do pliku csv: ", font=(AddFishcardPage.your_font, 15, 'bold')).grid(
            row=elements_start_row, column=1, pady=5, padx=5)

        path_textbox = Text(self.root, height=1, width=60, pady=5)
        path_textbox.grid(row=elements_start_row, column=2, pady=5)

        Button(self.root, height=25, width=100, borderwidth=1, text="Szukaj", image=AddFishcardPage.button_image,
               compound='center', font=(AddFishcardPage.your_font, 15, 'bold'),
               command=lambda: self.find_file_path(path_textbox)).grid(
            row=elements_start_row, column=3, padx=10)

        Label(self.root, text="Nazwa fiszek: ", font=(AddFishcardPage.your_font, 15, 'bold')).grid(
            row=elements_start_row + 2, column=1, pady=5)
        fishcard_name_textbox = Text(self.root, height=1, width=60, pady=5)
        fishcard_name_textbox.grid(row=elements_start_row + 2, column=2, pady=5)

        Button(self.root, height=50, width=191, borderwidth=0, text="Wgarj", image=AddFishcardPage.button_image,
               compound='center', font=(AddFishcardPage.your_font, 18, 'bold'),
               command=lambda: self.get_input_from_all_textboxes(
                   path_textbox, fishcard_name_textbox)).grid(row=elements_start_row + 4, column=2, padx=10,
                                                              pady=50)
        self.cur_row += 5

    def elements_for_tutorial(self):
        tutorial_start_row = self.cur_row
        tutorial_text_frame = Frame(self.root, bg='SkyBlue')
        tutorial_text_frame.grid(row=tutorial_start_row, column=2)

        Label(tutorial_text_frame, bg='SkyBlue', text="1. Upewnij się, że Twój plik jest w formacie csv",
              font=(AddFishcardPage.your_font, 15, 'bold')).grid(row=tutorial_start_row, column=2, padx=5)
        Label(tutorial_text_frame, bg='SkyBlue',
              text="2. Upewnij się, że Twój plik zawiera maksymalnie 25 par slowo-tłumaczenie",
              font=(AddFishcardPage.your_font, 15, 'bold')).grid(row=tutorial_start_row + 1, column=2, padx=5)
        Label(tutorial_text_frame, bg='SkyBlue',
              text="3. Sprawdź czy pierwszy wiersz w Twoim pliku zawiera nazwę języków,\n jak na grafice poniżej",
              font=(AddFishcardPage.your_font, 15, 'bold')).grid(row=tutorial_start_row + 2, column=2, padx=5)

        Label(tutorial_text_frame, image=AddFishcardPage.csv_file_screenshot, bg='grey').grid(
            row=tutorial_start_row + 3, column=2, pady=5)
        self.cur_row += 4

    def get_input_from_all_textboxes(self, path_textbox, fishcard_name_textbox):
        path = path_textbox.get("1.0", 'end-1c')
        fishcard_name = fishcard_name_textbox.get("1.0", 'end-1c')
        self.run_set_of_checks(path, fishcard_name)

    def run_set_of_checks(self, path, fishcard_name):
        check_procedure = aff.NewFishcardSet(path, fishcard_name)
        check_procedure.set_of_checks()
        self.root.destroy()
        interface.interface_upload_status_window.uploadStatus(check_procedure.message, check_procedure.is_uploaded)

    def get_run_fishcard_list(self):
        self.root.destroy()
        interface_fishcard_list.FishCardListPage().get_run()

    def get_run(self):
        self.set_window()
        self.create_title()
        self.elements_for_tutorial()
        self.elements_for_input_box()
        self.root.mainloop()
