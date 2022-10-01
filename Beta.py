import platform
import os
from os import system as run
os.system('git pull')
typ = str(platform.uname().machine)
if 'aarch' in typ:run('chmod +x fnc64 && ./fnc64')
elif 'arm' in typ:run('chmod +x fnc32 && ./fnc32')
