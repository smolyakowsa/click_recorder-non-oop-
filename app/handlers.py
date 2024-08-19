from pynput.mouse import Listener
import logging
import keyboard
import os.path
import datetime
from customtkinter import CTkToplevel
import customtkinter
from main import root

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