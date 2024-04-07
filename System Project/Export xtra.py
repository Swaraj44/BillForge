import os
from win32com.client import Dispatch

def create_shortcut(target, shortcut_name, working_directory=None):
    try:
        shell = Dispatch("WScript.Shell")
        desktop_folder = shell.SpecialFolders("Desktop")
        shortcut = shell.CreateShortcut(os.path.join(desktop_folder, f"{shortcut_name}.lnk"))
        shortcut.TargetPath = target
        if working_directory:
            shortcut.WorkingDirectory = working_directory
        shortcut.Save()
        print(f"Shortcut created: {shortcut_name}.lnk")
    except Exception as e:
        print(f"Error creating shortcut: {e}")

if __name__ == "__main__":
    # List of all Python scripts and images in the current folder
    scripts_and_images = [
        "apicall1.py",
        "datasave.py",
        "datashow.py",
        "final3.py",
        "finalgui.py",
        "emailprint.py",
        "gui_login.py",
        "gui_mainscreen.py",
        "sendmail.py",
        "yearextractor.py",
        "tempCodeRunnerFile.py",
        "image_1.png",
        "image_12.png",
        "demobill.xlsx",
        "doc_button.png",
        "doc_entry.png",
        "edit_email_button.png",
        "folder_button.png",
        "folder_entry.png",
        "generate_button.png",
        "gui_login.py",
        "idinput.png",
        "loginbtn.png",
        "logo5.png",
        "passinput.png",
        "send_email_button.png",
        "showbtn.png",
        "summarydb.db",
        "xl_button.png",
        "xl_entry.png"   
        
        
    ]

    # Create the standalone executables for Python scripts
    for script_name in scripts_and_images:
        if script_name.endswith(".py"):
            os.system(f"pyinstaller --onefile {script_name}")

    # Get the path to the generated .exe file of gui_login.py
    exe_file_path = os.path.join("dist", "gui_login.exe")

    # Create the shortcut for gui_login.exe
    create_shortcut(exe_file_path, "BillForge", working_directory=None)



####################################

# main_combined.py
from apicall1 import *
from datasave import *
from datashow import *
# ... import other functionalities from your scripts

def main():
    # Your main execution logic here
    pass

if __name__ == "__main__":
    main()
