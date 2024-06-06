from tkinter import Tk, PhotoImage, Label, Button
import interface.interface_main as im


def winnerInformation(click_counter):  # zmien nazwe na memo_game
    your_font = "Amatic SC"
    root = Tk()
    root.geometry("300x300")
    root.config(bg="skyblue")
    button_image = PhotoImage(file="../images/button.png")
    Label(root, text=f'Wygrałeś!', font=(your_font, 25, 'bold'), bg='SkyBlue').pack(pady=10)
    Label(root, text=f'Twoja liczka ruchów to: {click_counter}', font=(your_font, 18, 'bold'), bg='SkyBlue').pack(
        pady=10)  # ruch to wybor pary
    Button(root, image=button_image, borderwidth=0, compound='center', text='Wróć do menu głównego', width=191,
           font=(your_font, 18, 'bold'), height=50, command=lambda: back_to_menu_actions()).pack(pady=10)

    def back_to_menu_actions():
        root.destroy()
        im.FirstPage(Tk()).get_run_first_page()

    root.mainloop()
