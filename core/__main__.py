import sys
import core
from core.gui import gui


def get_software_details():
    return "μSign v" + core.__version__


def get_license_details():
    return "Copyright (c) 2023 PyroNeon Software. Licensed under GPL-3.0 License."


def get_python_version():
    return sys.version.split(" ")[0]


if __name__ == '__main__':
    gui.run()
