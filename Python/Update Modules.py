import subprocess, os

outdated_modules = subprocess.check_output("pip list -o").decode().split("\n")

modules = [i[:i.find(" ")] for i in outdated_modules[2:]]

os.system("python.exe -m pip install --upgrade pip")

[os.system(f"pip install --upgrade {i}") for i in modules]
