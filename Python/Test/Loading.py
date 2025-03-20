from time import sleep

for i in range(4*3):

	print(f"Connecting{'.'*(i%4)}{' '*(4-(i%4))}", end = "\r")
	sleep(0.5)