import sys
import subprocess
import os

os.makedirs(os.path.abspath("gen"), exist_ok=True)
# pyside6-uic "C:\Users\KoaPickett\Documents\GitHub\TaskTracker\forms\taskTrackerQT.ui" -o "C:\Users\KoaPickett\Documents\GitHub\TaskTracker\gen\taskTrackerQT_ui.py"   
# generate taskTrackerQT_ui.py
uic = "pyside6-uic.exe"
# in_file = r"C:\Users\KoaPickett\Documents\GitHub\TaskTracker\forms\taskTrackerQT.ui"
# out_file = r"C:\Users\KoaPickett\Documents\GitHub\TaskTracker\gen\taskTrackerQT_ui.py"
in_file = os.path.abspath(r"forms\taskTrackerQT.ui")
out_file = os.path.abspath(r"gen\taskTrackerQT_ui.py")
subprocess.call([uic, "--from-imports", in_file, '-o', out_file], shell=True)