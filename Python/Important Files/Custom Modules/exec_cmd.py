import os, sys, __main__

def cmdrun():

	File = __main__.__file__

	file_loc = File.removesuffix(os.path.basename(File)) + "temp"
	
	if os.path.exists(file_loc):

		os.remove(file_loc)
	
	else:

		with open(file_loc, "w+") as file:

			pass

		os.system(f'start cmd /k python "{File}"')