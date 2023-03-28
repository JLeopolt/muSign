import tkinter as tk

from core.utils import files
from core.services import config


# helper method which sets up the top Menubar of the window.
def configure(parent):
    # Create menubar
    menubar = tk.Menu(parent)

    # Prepare 'File' menu
    file_menu = tk.Menu(menubar, tearoff=0)
    # exits the program
    file_menu.add_command(label="Exit", command=parent.quit)
    menubar.add_cascade(label="File", menu=file_menu)

    # Prepare 'Config' menu
    config_menu = tk.Menu(menubar, tearoff=0)
    config_menu.add_command(label="Import Settings", command=prompt_load)
    config_menu.add_command(label="Export Settings", command=prompt_save)
    menubar.add_cascade(label="Config", menu=config_menu)

    # Prepare HelpMenu
    # help_menu = tk.Menu(menubar, tearoff=0)
    # help_menu.add_command(label="About", command=lambda: webbrowser.open('https://www.pyroneon.ml/'))
    # menubar.add_cascade(label="Help", menu=help_menu)

    # Add the Menu to window
    parent.config(menu=menubar)


# prompts the user to find a file and open it.
def prompt_load():
    path = files.load_config_from_file()
    if path is None:
        print('Error: Could not load file.')
        return
    config.load(path)
    print('Successfully loaded configuration from file.')


# prompts the user to save to a file.
def prompt_save():
    path = files.save_config_to_file()
    if path is None:
        print('Error: Could not save file.')
        return
    config.save(path)
    print('Successfully saved configuration to file.')
