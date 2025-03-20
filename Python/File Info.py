import os
import pandas as pd

cur_dir = os.path.dirname(os.path.abspath(__file__))

py_files = []

for par_dir, dirs, files in os.walk(cur_dir):
    py_files.extend([os.path.join(par_dir, file) for file in files if (".py" in file[-3:]) or (".pyw" in file[-4:])])

py_dict = dict()

for file in py_files:
    py_dict[file] = os.path.getsize(file)

sorted_py_dict = {"File Name": [""], "Bytes": [""], "Kilobytes": [""], "Megabytes": [""]}

for file in sorted(py_dict, key=py_dict.get, reverse=True):
    sorted_py_dict["File Name"].append(f"{os.path.basename(file)}")
    sorted_py_dict["Bytes"].append(f"{os.path.getsize(file)} Bytes")
    sorted_py_dict["Kilobytes"].append(f"{os.path.getsize(file)/1024:.2f} KB")
    sorted_py_dict["Megabytes"].append(f"{os.path.getsize(file)/1024**2:.2f} MB")

df = pd.DataFrame(sorted_py_dict)
df.index.name = "File Number"

print(df.to_string(), "\n")

os.system("pause")