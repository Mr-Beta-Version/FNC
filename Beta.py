import platform
import os
os.system('git pull')
typ = str(platform.uname().machine)
if 'aarch' in typ:__import__("FNC").buynow()
elif 'arm' in typ:__import__("FNCarm").buynow()
