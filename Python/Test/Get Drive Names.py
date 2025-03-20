import subprocess

sp_to_get_drives = subprocess.Popen('wmic logicaldisk get DeviceID ',shell=True,stdout=subprocess.PIPE,text=True)
x = (sp_to_get_drives.stdout.read()).split(" ")

list_drives=[]

for i in x:
    if ":" in i:
        list_drives.append(i.strip("\n"))

print(list_drives)