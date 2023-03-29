import os
import sys
from tkinter import filedialog

from core.utils import utils

config_filetypes = [('μSign Configs', '*.ini'),
                    ('All Files', '*.*')]
binary_filetypes = [('Executables', '*.exe'),
                    ('All Files', '*.*')]
keystore_filetypes = [('Keystore Files', '*.pfx'),
                      ('All Files', '*.*')]


# Used to get a file.
# Must use this when compiling to .exe using Pyinstaller.
def resource_path(filename):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, filename)
    return os.path.join(os.path.abspath("."), filename)


# Used to retrieve files from the assets folder, by filename.
def asset_path(filename):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, "assets\\" + filename)
    return os.path.join(os.path.abspath("."), "assets\\" + filename)


# Returns the filepath to save to. Returns None if unsuccessful.
def save_config_to_file():
    return filedialog.asksaveasfile(initialdir=os.path.abspath("."),
                                    title='Save Configuration To File',
                                    defaultextension='*.ini',
                                    filetypes=config_filetypes)


# Returns the filepath to load from. Returns None if unsuccessful.
def load_config_from_file():
    return filedialog.askopenfile(initialdir=os.path.abspath("."),
                                  title='Load Configuration From File',
                                  defaultextension='*.ini',
                                  filetypes=config_filetypes)


def open_filepath(title, filetypes):
    return filedialog.askopenfilename(initialdir=os.path.abspath("."),
                                      title=title,
                                      defaultextension=filetypes[0][0],
                                      filetypes=filetypes)


# Returns true if the file dialog was cancelled or failed.
def was_cancelled(filepath):
    return utils.trim(filepath) == ''
