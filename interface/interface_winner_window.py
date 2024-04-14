from tkinter import *
import interface.interface_main as im
import interface.interface_memo_game as img



def winnerInformation(green_counter, red_counter):   # zmien nazwe na memo_game
    root = Tk()
    root.geometry("300x300")
    root.config(bg="skyblue")
    Label(root, text=f'Wygrałeś!').pack()
    Label(root, text=f'Twoja liczka ruchów to: {red_counter + green_counter}').pack()
    Button(root, text='Wróć do menu głównego', command= lambda: back_to_menu_actions()).pack()
    def back_to_menu_actions():
        root.destroy()
        im.FirstPage0(Tk()).get_run_first_page()

    root.mainloop()