import apicall1
import datasave
import datashow
import final3
import emailprint
import gui_login
import gui_mainscreen
import sendmail
import yearextractor





from pathlib import Path
import tkinter as tk
from tkinter import Canvas, Entry, Button, PhotoImage, Label
import gui_mainscreen as GM
import finalgui as FG


def ING():

# Get the current script's directory
  SCRIPT_PATH = Path(__file__).parent

  ASSETS_PATH = SCRIPT_PATH

  def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


        
        
        
        
        
        ################################################################################
  import sqlite3
  import pickle

  class ExampleClass:
    def __init__(self, name, value):
        self.name = name
        self.value = value

  def showdata(name):
# Connect to the SQLite database (creates a new database if it doesn't exist)
    conn = sqlite3.connect('BillForge.db')

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





    # Fetch the object from the database based on the name
    cursor.execute('SELECT data FROM Bill WHERE name = ?', (name,))
    row = cursor.fetchone()

    if row:
        # Deserialize the object using pickle
        fetched_object = pickle.loads(row[0])
        
        # Print the fetched object
        print(f"Fetched Object Name: {fetched_object.name}")
        print(f"Fetched Object Value: {fetched_object.value}")
        print('-' * 20)
        
        return fetched_object.value
        
    

# Close the connection
    

    conn.close()

#ss=showdata("admin")
#print(ss)

  def suu():
       window.destroy()
       FG.SUG()
      

  def login():

    entered_username = idinput.get()
    entered_password = passinput.get()
    
    print(entered_username)
    print(entered_password)
    
    fetched_value = showdata(entered_username)
    print("---------CK---------")
    print(fetched_value)
    
    
    
    if fetched_value is not None and entered_password == fetched_value:
        window.destroy()  # Close the login window
        #main_gui()  # Open the main GUI
        GM.gui2()
    else:
        login_status_label.config(text="Invalid username or password")        
        

        
        
        
        
        
        
        ###################################################################################

  window = tk.Tk()
  window.title("BillForge")
  window.geometry("751x451")
  window.configure(bg="#FFFFFF")

  canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=451,
    width=751,
    bd=0,
    highlightthickness=0,
    relief="ridge"
  )
  canvas.place(x=0, y=0)

  image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
  image_1 = canvas.create_image(
    375.0,
    225.0,
    image=image_image_1
  )

  canvas.create_text(
    31.0,
    30.0,
    anchor="nw",
    text="BillForge KUET Teachers’ Edition (An Automatic Bill Generator)",
    fill="#2F0DFF",
    font=("Imprima Regular", 24 * -1)
  )

  login_image_1 = PhotoImage(file=relative_to_assets("loginbtn.png"))
  loginbtn = Button(
    image=login_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=login,
    relief="flat"
  )
  loginbtn.place(
    x=117.0,
    y=296.0,
    width=99.0,
    height=32.0
  )

  userid_image_1 = PhotoImage(file=relative_to_assets("idinput.png"))
  userid_bg_1 = canvas.create_image(
    167.0,
    210.5,
    image=userid_image_1
  )
  idinput = Entry(
    bd=0,
    bg="#CFD1E6",
    fg="#000716",
    highlightthickness=0
  )
  idinput.place(
    x=109.0,
    y=195.0,
    width=116.0,
    height=29.0
  )

  passid_image_2 = PhotoImage(file=relative_to_assets("passinput.png"))
  passid_bg_2 = canvas.create_image(
    167.0,
    256.5,
    image=passid_image_2
)
  passinput = Entry(
    bd=0,
    bg="#CFD1E6",
    fg="#000716",
    highlightthickness=0,
    show="*"
  )
  passinput.place(
    x=109.0,
    y=241.0,
    width=116.0,
    height=29.0
  )

  canvas.create_text(
    21.0,
    200.0,
    anchor="nw",
    text="User_ID:",
    fill="#000000",
    font=("Imprima Regular", 14 * -1)
  )

  canvas.create_text(
    21.0,
    246.0,
    anchor="nw",
    text="Password:",
    fill="#000000",
    font=("Imprima Regular", 14 * -1)
  )

  admin_image_2 = PhotoImage(file=relative_to_assets("adminbtn.png"))
  adminbtn = Button(
    image=admin_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=suu,
    relief="flat"
  )  
  adminbtn.place(
    x=117.0,
    y=352.0,
    width=99.0,
    height=32.0
  )

# Create a label for displaying login status
  login_status_label = Label(
    window,
    text="",
    fg="red"
  )
  login_status_label.place(
    x=90.0,
    y=400.0,  # Adjust the y-coordinate to place it at the bottom
    width=200.0,
    height=25.0
  )

  window.resizable(False, False)
  window.mainloop()



if __name__ == "__main__":
    ING()
