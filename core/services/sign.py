import subprocess

from core.gui import gui
from core.utils import files


def build_command():
    return "\"" + files.resource_path('bin\\sign4j.exe') + "\" java -jar " \
           "\"" + files.resource_path('bin\\jsign-2.0.jar') + "\" " \
           "--alias \"" + gui.domainVar.get() + "\" " \
           "--keystore \"" + gui.keystorePathVar.get() + "\" " \
           "--storepass \"" + gui.keystorePwVar.get() + "\" "  \
           "--storetype " + gui.keystoreTypeVar.get() + " "  \
           "\"" + gui.filepathVar.get() + "\""


def run():
    command_str = build_command()
    subprocess.run(command_str, shell=True)
