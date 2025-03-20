import subprocess
import sys
from playsound import playsound

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'playsound'])

playsound ("Path_To_File")