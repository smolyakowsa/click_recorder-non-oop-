import customtkinter as CTk

def open():
    rename_window = CTk.CTkToplevel()

    CTk.set_appearance_mode('Light')
    CTk.set_default_color_theme('blue')

    rename_window.geometry('300x100')
    rename_window.resizable(True, True)
    rename_window.minsize(300, 200)

    rename_window.title('Rename')
    rename_window.lift()
    rename_window.attributes('-topmost', True)

