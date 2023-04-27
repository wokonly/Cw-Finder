import os
import zipfile

import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("CW Finder | By Wok")

directory = f'C:\\Users\\{os.getlogin()}\\AppData\\Roaming\\.minecraft\\mods'

cheat_filename = ""

for filename in os.listdir(directory):
    if filename.endswith(".jar"):
        with zipfile.ZipFile(os.path.join(directory, filename)) as jar_file:
            for file_info in jar_file.infolist():
                if (file_info.filename.endswith(".class") or file_info.filename.endswith(".java")) and "CwCrystal" in file_info.filename:
                    print(f"{filename} contains CwCrystal")
                    cheat_filename = filename
                if (file_info.filename.endswith(".class") or file_info.filename.endswith(".java")) and "AutoInventoryTotem" in file_info.filename:
                    print(f"{filename} contains AutoInventoryTotem")
                    cheat_filename = filename
                if (file_info.filename.endswith(".class") or file_info.filename.endswith(".java")) and "SkliggaHack" in file_info.filename:
                    print(f"{filename} This user is using SkliggaHack")
                    cheat_filename = filename
                if (file_info.filename.endswith(".class") or file_info.filename.endswith(".java")) and "Pugware" in file_info.filename:
                    print(f"{filename} This user is using Pugware hack")
                    cheat_filename = filename
                if (file_info.filename.endswith(".class") or file_info.filename.endswith(".java")) and "NoLoadingScreen" in file_info.filename:
                    print(f"{filename} contains NoLoadingScreen used by hacked clients")
                    cheat_filename = filename
                    
if cheat_filename:
    print(" ")
    print(f"The cheat is {cheat_filename}")
else:
    print(" ")
    print("No cheat found.")

print("Made by Wok")

input("")
