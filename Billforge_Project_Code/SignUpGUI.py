import tkinter as tk
from tkinter import PhotoImage, filedialog
import os
import sys
import webbrowser
from PIL import Image, ImageTk

import GeneralDataProcessing as final
import time
#####################################################
from tkinter import ttk
import threading
import emailprint as ep

import datasave as DDS


import GeneralGuiLogin as GL
import BacklogGuiLogin as BLGLI

def SUG(flag):

##############################################################################################################
 import sqlite3
 import pickle
 
  #https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
 def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
  

 class ExampleClass:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        
        

 def savedata(name,value):  
# Connect to the SQLite database (creates a new database if it doesn't exist)
  conn = sqlite3.connect(resource_path('data\\database\\BillForge.db'))

# Create a cursor object to execute SQL queries
  cursor = conn.cursor()

# Define a table if it doesn't exist
  cursor.execute('''
    CREATE TABLE IF NOT EXISTS Bill (
        id INTEGER PRIMARY KEY,
        name TEXT,
        data BLOB
    )
  ''')
  
  



# Sample objects to be saved

  obj= ExampleClass(name=name, value=value)
    

# Save the objects to the database

    # Serialize the object using pickle
  serialized_object = pickle.dumps(obj)
    
    # Insert the serialized object into the table along with the name
  cursor.execute('INSERT INTO Bill (name, data) VALUES (?, ?)', (obj.name, serialized_object))

# Commit the changes
  conn.commit()

# Fetch and print the objects based on their names

# Close the connection
  conn.close()


#savedata("admin","swaraj")








###############################################################################################################






 def SignUp():
    entered_username = username_entry.get()
    entered_password = password_entry.get()
    
    
    
    
    
    if entered_username is not None:
      if entered_password is not None:
          DDS.savedata(entered_username,entered_password)
          SignUp_window.destroy()  # Close the login window
          if flag=="g":
           GL.LOGIN_GENERAL();
          else:
           BLGLI.LOGIN_BACKLOG();
      else:
        SignUp_status_label.config(text="Invalid username or password")
          
    else:
        SignUp_status_label.config(text="Invalid username or password")








# Create the SignUp window
 SignUp_window = tk.Tk()
 SignUp_window.title("BillForge-Signup Page")
 SignUp_window.iconbitmap(resource_path('data\\images\\general_logo.ico'))

# Background color gradient
 canvas = tk.Canvas(SignUp_window, width=400, height=300, highlightthickness=0)
 canvas.grid(row=0, column=0, rowspan=5, columnspan=2)

 color1 = "#aaffcc"  # Light green
 color2 = "#aaffcc" 
 color3 = "#003366"  # Dark blue
 colour4="26CE06"
 color5 = "#ffffff"
#gradient_color=color1

# Create a linear gradient
 for i in range(300):
    gradient_color = "#%02x%02x%02x" % (
        int((1 - i / 300) * int(color1[1:3], 16) + i / 300 * int(color2[1:3], 16)),
        int((1 - i / 300) * int(color1[3:5], 16) + i / 300 * int(color2[3:5], 16)),
        int((1 - i / 300) * int(color1[5:], 16) + i / 300 * int(color2[5:], 16))
    )
    canvas.create_line(0, i, 400, i, fill=gradient_color, width=1)

# Logo
 try:
    original_logo = Image.open(resource_path("data\\images\\logo5.png"))
    logo_image = ImageTk.PhotoImage(original_logo)
    logo_label = tk.Label(SignUp_window, image=logo_image, bg=color1)
    logo_label.grid(row=0, column=0, columnspan=2, pady=10, padx=10)
 except tk.TclError as e:
    print(f"Error: {e}")
    
    
 hi_kuet_label = tk.Label(SignUp_window, text="Khulna University of Engineering & Technology", font=("Helvetica", 12), bg=gradient_color)
 hi_kuet_label.grid(row=1, column=0, columnspan=2, pady=5)

# Create and configure widgets for SignUp window
 username_label = tk.Label(SignUp_window, text="Username:", bg=gradient_color)
 username_entry = tk.Entry(SignUp_window)
 password_label = tk.Label(SignUp_window, text="Password :", bg=gradient_color)
 password_entry = tk.Entry(SignUp_window, show="*")
 SignUp_button = tk.Button(SignUp_window, text="SignUp", command=SignUp, bg=color5)
 SignUp_status_label = tk.Label(SignUp_window, text="", bg=gradient_color)

# Grid layout for SignUp window
 username_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
 username_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")
 password_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
 password_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")
 SignUp_button.grid(row=4, column=0, columnspan=2, pady=10)
 SignUp_status_label.grid(row=5, column=0, columnspan=2, pady=5)

# Run the main loop for SignUp window
 SignUp_window.mainloop()