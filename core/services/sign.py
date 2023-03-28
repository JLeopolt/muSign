import subprocess

from core.gui import gui


def build_command():
    return "\"D:\\Program Files\\Launch4j\\sign4j\\sign4j.exe\" java -jar " \
           "\"D:\\Java Projects\\PuzzleMinefield\\desktop\\build\\libs\\jsign-2.0.jar " \
           "--alias " + gui.domainVar.get() + " " \
           "--keystore " + gui.keystorePathVar.get() + " " \
           "--storepass " + gui.keystorePwVar.get() + " "  \
           "--storetype " + gui.keystoreTypeVar.get() + " "  \
           "\"" + gui.filepathVar.get() + "\""


def run():
    command_str = build_command()
    subprocess.run(command_str, shell=True)
