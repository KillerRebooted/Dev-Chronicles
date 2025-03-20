File_Name = "69*deeznutsb oi |ss"

Invalid = ["<", ">", ":", '"', "\\", "|", "/", "?", "*"]

New_File_Name = ""

for i in File_Name:

    if not i in Invalid:

        New_File_Name += i

    File_Name = New_File_Name

print(File_Name)