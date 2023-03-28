from configparser import ConfigParser

from core.gui import gui

# Config settings
config = ConfigParser()


# Loads configuration from file. Expects a File object.
def load(file):
    # if main section doesn't exist yet, (new file) create one.
    if not config.has_section('main'):
        config.add_section('main')
    # read from the file object's filepath
    config.read(file.name)

    # Update all settings
    load_config_option('main', 'filepath', gui.filepathVar, gui.filepath_entry)
    load_config_option('main', 'keystore_filepath', gui.keystorePathVar, gui.keystore_path_entry)
    load_config_option('main', 'keystore_pw', gui.keystorePwVar, gui.keystore_pw_entry)
    load_config_option('main', 'keystore_type', gui.keystoreTypeVar, gui.keystore_type_entry)
    load_config_option('main', 'alias', gui.domainVar, gui.domain_entry)


def load_config_option(sect, opt, var, entrybox):
    # Get opt value
    value = config.get(sect, opt)
    # Set Stringvar
    var.set(value)
    # Update entrybox
    entrybox.delete(0, 'end')
    entrybox.insert(0, value)


# Saves configuration to file. Expects a File object.
def save(file):
    # if main section doesn't exist yet, (new file) create one.
    if not config.has_section('main'):
        config.add_section('main')

    # Set all the settings
    config.set('main', 'filepath', gui.filepathVar.get())
    config.set('main', 'keystore_filepath', gui.keystorePathVar.get())
    config.set('main', 'keystore_pw', gui.keystorePwVar.get())
    config.set('main', 'keystore_type', gui.keystoreTypeVar.get())
    config.set('main', 'alias', gui.domainVar.get())

    # write to file
    config.write(file)
