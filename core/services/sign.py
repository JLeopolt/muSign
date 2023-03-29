import subprocess

from core.gui import gui, console
from core.utils import files, utils


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
    proc = subprocess.run(command_str, shell=True, capture_output=True)
    console.printStdOutput('stdout', proc.stdout.decode())
    if utils.trim(proc.stderr.decode()) != '':
        console.printStdOutput('stderr', proc.stderr.decode())
