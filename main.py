import tkinter
from customtkinter import CTk
import os
import customtkinter
from app import handlers


if __name__ == '__main__':

    customtkinter.set_appearance_mode('Dark')
    customtkinter.set_default_color_theme('blue')

    root = CTk()

    root.geometry('700x500')
    root.resizable(True, True)
    root.minsize(700, 500)

    root.title('Click Recorder')

    root.grid_rowconfigure(3, weight=1)
    root.grid_columnconfigure(5, weight=1)

    run_state = 'disabled' if os.path.isdir('files') is False or os.listdir('files') == [] else 'enabled'

    rec_btn = customtkinter.CTkButton(master=root,
                                  width=250,
                                  height=50,
                                  border_width=0,
                                  corner_radius=10,
                                  text='Rec.',
                                  command=handlers.listen())

    rec_btn.place(relx=0.8, rely=0.3, anchor=tkinter.CENTER)

    run_btn = customtkinter.CTkButton(master=root,
                                  width=250,
                                  height=50,
                                  border_width=0,
                                  corner_radius=10,
                                  text='Run',
                                  command=handlers.run())

    run_btn.place(relx=0.8, rely=0.45, anchor=tkinter.CENTER)

    ext_btn = customtkinter.CTkButton(master=root,
                                      width=250,
                                      height=50,
                                      border_width=0,
                                      corner_radius=10,
                                      text='Exit',
                                      command=root.quit,
                                      fg_color='black')

    ext_btn.place(relx=0.5, rely=0.90, anchor=tkinter.CENTER)

    del_bn = customtkinter.CTkButton(master=root,
                                     width=250,
                                     height=50,
                                     border_width=0,
                                     corner_radius=10,
                                     text='Delete\n last file',
                                     command=handlers.delete())

    del_bn.place(relx=0.8, rely=0.60, anchor=tkinter.CENTER)

    del_all_btn = customtkinter.CTkButton(master=root,
                                          width=250,
                                          height=50,
                                          border_width=0,
                                          corner_radius=10,
                                          text='Delete\nALL files',
                                          command=handlers.del_all())

    del_all_btn.place(relx=0.8, rely=0.75, anchor=tkinter.CENTER)

    combobox_var = customtkinter.StringVar(value='Default')
    combobox_values = ','.join(os.listdir(f'{os.getcwd()}\\files\\'))
    combobox = customtkinter.CTkComboBox(master=root, values=combobox_values, variable=combobox_var, width=200)
    combobox.place(relx=0.2, rely=0.3, anchor=tkinter.CENTER)


    root.mainloop()