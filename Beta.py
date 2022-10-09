import os
from os import system as run
import platform
bit = platform.architecture()[0]
run('git pull')
if bit=='64bit':
    run('curl -L https://github.com/Mr-Beta-Version/Compiled/raw/main/fnc64 -o fnc64')
    run('chmod +x fnc64')
    run('./fnc64')
elif bit=='32bit':
    run('curl -L https://github.com/Mr-Beta-Version/Compiled/raw/main/fnc32 -o fnc32')
    run('chmod +x fnc32')
    run('./fnc32')
else:exit(f'\x1b[1;91m[!] Unknown Device Type {bit}')
