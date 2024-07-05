import sys
import subprocess
import os

print("Start")
os.makedirs(os.path.abspath("gen"), exist_ok=True)
# pyside6-uic "C:\Users\KaliCajala\Documents\GitHub\kali-first-task\forms\main_window.ui" -o "C:\Users\KaliCajala\Documents\GitHub\kali-first-task\gen\ui_main_window.py"   
# generate main_window.ui   
uic = "pyside6-uic.exe"
# in_file = r"C:\Users\KaliCajala\Documents\GitHub\kali-first-task\forms\main_window.ui"
# out_file = r"C:\Users\KaliCajala\Documents\GitHub\kali-first-task\gen\ui_main_window.py"
in_file = os.path.abspath(r"forms\taskTrackerQT.ui")
out_file = os.path.abspath(r"gen\taskTrackerQT_ui.py")
subprocess.call([uic, "--from-imports", in_file, '-o', out_file], shell=True)
print("End")