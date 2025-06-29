import os
import sys
import winshell
from win32com.client import Dispatch

# Path to your EXE file
target = os.path.join(os.path.expanduser("~"), "dist", "teja_assistant_gui.exe")

# Desktop path
desktop = winshell.desktop()
shortcut_path = os.path.join(desktop, "Teja Assistant.lnk")

# Create shortcut
shell = Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(shortcut_path)
shortcut.Targetpath = target
shortcut.WorkingDirectory = os.path.dirname(target)
shortcut.IconLocation = target
shortcut.save()

print("Shortcut created on Desktop ✔️")
