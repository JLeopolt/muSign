import tkinter as tk
from tkinter import ttk

from tkinterdnd2 import DND_FILES, TkinterDnD

from core import __main__
from core.gui import menubar, console
from core.services import sign
from core.utils import files

# The main application window.
root: tk.Tk

# StringVar containing filepath to the binary file.
filepathVar: tk.StringVar
filepath_entry: tk.Entry

# StringVar containing filepath to the keystore file.
keystorePathVar: tk.StringVar
keystore_path_entry: tk.Entry

# StringVar containing password to the keystore file.
keystorePwVar: tk.StringVar
keystore_pw_entry: tk.Entry

showPasswordVar: tk.IntVar
showPasswordButton: tk.Checkbutton

# StringVar containing type of keystore file.
keystoreTypeVar: tk.StringVar
keystore_type_entry: tk.Entry

# StringVar containing alias domain to use for signing.
domainVar: tk.StringVar
domain_entry: tk.Entry


# Called to build the window on application launch.
def run():
    global root
    root = TkinterDnD.Tk()

    # root window
    root.title(__main__.get_software_details())
    root.geometry('300x400')

    # create window icon
    ico = tk.PhotoImage(file=files.asset_path("muSign-icon.png"))
    root.wm_iconphoto(False, ico)

    # add menubar
    menubar.configure(root)

    # input file section
    input_lframe = ttk.Frame(master=root)
    input_lframe.pack(side='top', fill='x', anchor='n', pady=3)
    tk.Label(master=input_lframe, text='.EXE File:', anchor='n').pack(side='left', fill='x')
    # filepath entry box
    global filepathVar
    filepathVar = tk.StringVar()
    global filepath_entry
    filepath_entry = ttk.Entry(master=input_lframe, textvariable=filepathVar)
    filepath_entry.pack(side='left', fill='x', expand=True, padx=3)
    ttk.Button(input_lframe, text='📁', width=3,
               command=lambda: open_file(filepathVar,
                                         filepath_entry,
                                         'Select Binary File',
                                         files.binary_filetypes)).pack(side='left')

    # allow user to drag and drop a file into the filepath entry box
    input_lframe.drop_target_register(DND_FILES)
    input_lframe.dnd_bind('<<Drop>>',
                          lambda e: update_entry(filepathVar, filepath_entry, e.data.replace('{', '').replace('}', '')))

    # keystore file section
    keystore_path_lframe = ttk.Frame(master=root)
    keystore_path_lframe.pack(side='top', fill='x', anchor='n', pady=1)
    ttk.Label(master=keystore_path_lframe, text='Keystore File:', anchor='n') \
        .pack(side='left', fill='x')
    global keystorePathVar
    keystorePathVar = tk.StringVar()
    global keystore_path_entry
    keystore_path_entry = ttk.Entry(master=keystore_path_lframe, textvariable=keystorePathVar)
    keystore_path_entry.pack(side='left', fill='x', expand=True, padx=3)
    ttk.Button(keystore_path_lframe, text='📁', width=3,
               command=lambda: open_file(keystorePathVar,
                                         keystore_path_entry,
                                         'Select Keystore File',
                                         files.keystore_filetypes)).pack(side='left')
    # allow user to drag and drop a file into the keystore filepath entry box
    keystore_path_lframe.drop_target_register(DND_FILES)
    keystore_path_lframe.dnd_bind('<<Drop>>',
                                  lambda e: update_entry(keystorePathVar, keystore_path_entry,
                                                         e.data.replace('{', '').replace('}', '')))

    # keystore password section
    keystore_pw_lframe = ttk.Frame(master=root)
    keystore_pw_lframe.pack(side='top', fill='x', anchor='n', pady=3)
    ttk.Label(master=keystore_pw_lframe, text='Password:', anchor='n') \
        .pack(side='left', fill='x')
    global keystorePwVar
    keystorePwVar = tk.StringVar()
    global keystore_pw_entry
    keystore_pw_entry = ttk.Entry(master=keystore_pw_lframe, textvariable=keystorePwVar, show="*")
    keystore_pw_entry.pack(side='left', fill='x', expand=True, padx=3)
    # show password checkbox
    global showPasswordVar
    showPasswordVar = tk.IntVar()
    global showPasswordButton
    showPasswordButton = tk.Checkbutton(keystore_pw_lframe,
                                        text='Show Password',
                                        variable=showPasswordVar,
                                        onvalue=1,
                                        offvalue=0,
                                        command=toggle_password)
    showPasswordButton.pack(side='left', fill='x', expand=True, padx=3)

    # keystore type section
    keystore_type_lframe = ttk.Frame(master=root)
    keystore_type_lframe.pack(side='top', fill='x', anchor='n', pady=3)
    ttk.Label(master=keystore_type_lframe, text='Keystore Type:', anchor='n') \
        .pack(side='left', fill='x')
    global keystoreTypeVar
    keystoreTypeVar = tk.StringVar(value='PKCS12')
    global keystore_type_entry
    keystore_type_entry = ttk.Entry(master=keystore_type_lframe, textvariable=keystoreTypeVar)
    keystore_type_entry.pack(side='left', fill='x', expand=True, padx=3)

    # alias section
    alias_lframe = ttk.Frame(master=root)
    alias_lframe.pack(side='top', fill='x', anchor='n', pady=3)
    ttk.Label(master=alias_lframe, text='Alias (Website):', anchor='n') \
        .pack(side='left', fill='x')
    # enter the alias to use
    global domainVar
    domainVar = tk.StringVar()
    global domain_entry
    domain_entry = ttk.Entry(master=alias_lframe, textvariable=domainVar)
    domain_entry.pack(side='left', fill='x', expand=True, padx=3)

    # execute command button
    tk.Button(root, text='Sign', width=6, bg='blue', fg='white', command=sign.run).pack(side='top', anchor='n', pady=2)

    # Prepare the console frame, then build the console component.
    # The console must be initialized, but isn't packed until the end.
    console_container = ttk.LabelFrame(root, text='Console')
    console.build(console_container)
    console_container.pack(side='top', fill='both', expand=True)

    # finally, execute the window
    root.mainloop()


# updates the StringVar and Entrybox
def update_entry(var, entry, value):
    # protect against none values
    if value is None:
        console.printError('Failed to update StringVar since value is None.')
        return
    var.set(value)
    entry.delete(0, 'end')
    entry.insert(0, value)


# file open button, var is the StringVar to set, entry is the Entrybox to update.
def open_file(var, entry, title, filetypes):
    # prompt user to select the file in explorer
    fp = files.open_filepath(title, filetypes)
    # Fail if the file wasn't opened
    if fp is None:
        console.printError("Failed to open file.")
        return
    # update the StringVar and Entrybox
    update_entry(var, entry, fp)


def toggle_password():
    if showPasswordVar.get() == 0:
        keystore_pw_entry.config(show='*')
        showPasswordButton.config(text='Show Password')
    else:
        keystore_pw_entry.config(show='')
        showPasswordButton.config(text='Hide Password')
