import os
  
Process = input("Do you wish to shutdown/restart your computer ? (s/r/no): ")
Time = int(input("Time after which You want to Execute the Process: "))
  
if Process == 's':
    
    os.system("shutdown /s /t " + str(Time))

elif Process == "r":

    os.system("shutdown /r /t " + str(Time))

elif Process == "no":

    print("Closing the Program")
    exit()
    
else:

    print("Invalid Option")
    exit()
