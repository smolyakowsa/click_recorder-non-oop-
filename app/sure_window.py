import customtkinter as CTk
import tkinter

from app import handlers


def open():
    sure_window = CTk.CTkToplevel()

    CTk.set_appearance_mode('Light')
    CTk.set_default_color_theme('blue')

    sure_window.geometry('300x100')
    sure_window.resizable(True, True)
    sure_window.minsize(300, 200)

    sure_window.title('Are you sure?')
    sure_window.lift()
    sure_window.attributes('-topmost', True)

    yes_btn = CTk.CTkButton(master=sure_window,
                                      width=150,
                                      height=50,
                                      border_width=0,
                                      corner_radius=10,
                                      text='Yes',
                                      command=handlers.delete)

    yes_btn.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)


    no_btn = CTk.CTkButton(master=sure_window,
                            width=150,
                            height=50,
                            border_width=0,
                            corner_radius=10,
                            text='No',
                            command=sure_window.destroy)

    no_btn.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

