from pynput.mouse import Listener
import logging
import keyboard
import os.path
import datetime
import main


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
    main.root.withdraw()
    file_name = python_file()
    logging.basicConfig(filename=file_name, level=logging.DEBUG, format='%(message)s', force=True)
    with Listener(on_click=on_click) as listener:
        while keyboard.wait('esc') is not None:
            listener.join()
    main.root.deiconify()


def run():
    main.root.withdraw()
    path = os.getcwd()
    os.chdir(f'{path}\\files\\')
    last_file = ''.join(sorted(os.listdir(f'{os.getcwd()}'))[-1::])
    os.system(f'python {last_file}')
    os.chdir(path)
    main.root.deiconify()


def delete():
    path = os.getcwd()
    os.chdir(f'{path}\\files\\')
    last_file = ''.join(sorted(os.listdir(f'{os.getcwd()}'))[-1::])
    os.remove(f'{last_file}')
    os.chdir(path)