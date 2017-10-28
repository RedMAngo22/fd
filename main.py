from halo import Halo
spinner = Halo()

spinner.start("Importing modules")
import os, sys
import getpass
import traceback
from colorama import Fore, Back, Style
raw_prompt = ""
prompt = ""
class utils:
    cmdhelp = None
    license = None
    ext_cmds = {}
    prompt = Fore.CYAN + Style.BRIGHT + getpass.getuser() + "@" + sys.platform + Style.RESET_ALL + ":{}$ "
    initial_dir = os.getcwd()
    def format_dir(d):
        return d.replace(utils.initial_dir, "~")
spinner.stop()

spinner.start("Loading files")
os.chdir('utils')
f = open('help.txt')
utils.cmdhelp = f.read()
f.close()
os.chdir('..')
f = open('LICENSE.md')
utils.license = f.read()
f.close()
spinner.stop()

spinner.start("Loading external commands")
os.chdir('ext_commands')
ext_cmds = []
for f in os.listdir(os.getcwd()):
    if f.endswith('.py'):
        ext_cmds.append(f.strip('.py'))
os.chdir('..')
spinner.stop()

# Main terminal loop

while True:
    try:
        while raw_prompt.split() == []:
            print(utils.prompt.format(utils.format_dir(os.getcwd())), end="")
            raw_prompt = input()

        prompt = raw_prompt.split()
        raw_prompt = ""

        if prompt[0] == "exit":
            if len(prompt) > 1:
                exit(int(prompt[1]))
            else:
                exit(0)
        elif prompt[0] == "help":
            print(utils.cmdhelp)
            print("EXTERNAL")
            print(', '.join(ext_cmds))
        elif prompt[0] == "cd":
            os.chdir(' '.join(prompt[1:]))
        elif prompt[0] == "ls":
            for f in os.listdir(os.getcwd()):
                if os.path.isdir(os.path.join(os.getcwd(), f)):
                    print(Fore.BLUE + Style.BRIGHT + f)
                else:
                    print(f)
        elif prompt[0] == "pwd":
            print('Active directory is {}'.format(os.getcwd()))
        elif prompt[0] == "clear":
            if os.name == "nt":
                os.system('cls')
            else:
                os.system('clear')
        else:
            if prompt[0] in ext_cmds:
                spinner.start('Loading command ' + prompt[0])
                _dir = os.getcwd()
                os.chdir(os.path.join(utils.initial_dir,'ext_commands'))
                f = open(prompt[0] + '.py')
                r = f.read()
                os.chdir(_dir)
                f.close()
                spinner.stop()
                exec(r)
            else:
                print(prompt[0] + ": command not found")
    except Exception as e:
        print("\nfail: {0}: {1}".format(type(e).__name__, e))
        spinner.stop()
    except KeyboardInterrupt:
        exit(0)
