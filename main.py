import tkinter

from customtkinter import CTk
from pynput.mouse import Listener
import logging
import keyboard
import os.path
import os
import datetime
import customtkinter
from PIL import Image
from customtkinter import CTkToplevel


def python_file():
    mypath = os.getcwd()

    if os.path.isdir(f'{mypath}\\files\\') is False:
        os.mkdir(f'{mypath}\\files\\')

    todays_date = str(datetime.date.today())
    py = '.py'
    log_file_name = todays_date
    i = 1

    while True:
        if os.path.isfile(f'{mypath}\\files\\{log_file_name}{py}') is True:
            log_file_name = todays_date + '_' + str(i)
            i += 1
            continue
        else:
            log_file = open(f'{mypath}\\files\\{log_file_name}{py}', 'w+')
            log_file.write('import pyautogui as pg\nimport time\n\npg.PAUSE = 3.0\ntime.sleep(3)\n')
            log_file.close()
            break

    return f'{mypath}\\files\\{log_file_name}{py}'


def on_click(x, y, button, pressed):
    if pressed:
        logging.info('pg.click({0}, {1})'.format(x, y))


def listen():
    root.withdraw()
    file_name = python_file()
    logging.basicConfig(filename=file_name, level=logging.DEBUG, format='%(message)s', force=True)

    with Listener(on_click=on_click) as listener:
        while keyboard.wait('esc') is not None:
            listener.join()
    root.deiconify()


def run():
    root.withdraw()
    path = os.getcwd()
    os.chdir(f'{path}\\files\\')
    last_file = ''.join(sorted(os.listdir(f'{os.getcwd()}'))[-1::])
    os.system(f'python {last_file}')
    os.chdir(path)
    root.deiconify()


def delete():
    path = os.getcwd()
    os.chdir(f'{path}\\files\\')
    last_file = ''.join(sorted(os.listdir(f'{os.getcwd()}'))[-1::])
    os.remove(f'{last_file}')
    os.chdir(path)


def del_all():
    if sure_window() is True:
        path = os.getcwd()
        os.chdir(f'{path}\\files\\')
        files = [os.remove(i) for i in os.listdir(os.getcwd())]
        os.chdir(path)
    else:
        pass


def sure_window():
    top = CTkToplevel(root)

    top.geometry('300x300')
    top.resizable(True, True)

    top.columnconfigure(5, weight=1)
    top.rowconfigure(5, weight=1)

    text_box = customtkinter.CTkTextbox(master=top, width=300, corner_radius=50)
    text_box.grid(row=0, column=0)
    text_box.insert('10.300', 'Are you sure, that\n you want to DELETE ALL files?')


    yes = customtkinter.CTkButton(master=top,
                                      width=100,
                                      height=25,
                                      border_width=0,
                                      corner_radius=10,
                                      text='Yes')

    yes.grid(row=5, column=0)

    no = customtkinter.CTkButton(master=top,
                                  width=100,
                                  height=25,
                                  border_width=0,
                                  corner_radius=10,
                                  text='No')

    no.grid(row=5, column=2)



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
                                  command=listen)

    rec_btn.place(relx=0.8, rely=0.3, anchor=tkinter.CENTER)

    run_btn = customtkinter.CTkButton(master=root,
                                  width=250,
                                  height=50,
                                  border_width=0,
                                  corner_radius=10,
                                  text='Run',
                                  command=run)

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
                                     command=delete)

    del_bn.place(relx=0.8, rely=0.60, anchor=tkinter.CENTER)

    del_all_btn = customtkinter.CTkButton(master=root,
                                          width=250,
                                          height=50,
                                          border_width=0,
                                          corner_radius=10,
                                          text='Delete\nALL files',
                                          command=del_all)

    del_all_btn.place(relx=0.8, rely=0.75, anchor=tkinter.CENTER)


    combobox_var = customtkinter.StringVar(value='Default')
    combobox_values = ','.join(os.listdir(f'{os.getcwd()}\\files\\'))
    combobox = customtkinter.CTkComboBox(master=root, values=combobox_values, variable=combobox_var, width=200)
    combobox.place(relx=0.2, rely=0.3, anchor=tkinter.CENTER)


    root.mainloop()