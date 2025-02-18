from pathlib import Path
import tkinter as tk
from tkinter import Canvas, Entry, Button, PhotoImage, filedialog

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

#import spinner as SP

#SP.progress()

# Function to animate the GIF
def animate_gif(label, gif_frames):
    # Function to update the image on the label with the next frame
    def update(ind):
        frame = gif_frames[ind]
        label.configure(image=frame)
        ind += 1
        if ind >= len(gif_frames):
            ind = 0
        label.after(100, update, ind)

    update(0)

# Load the GIF frames
def load_gif(filename):
    gif = Image.open(filename)
    frames = []
    try:
        while True:
            # Convert each frame to PhotoImage and append to frames list
            frame = ImageTk.PhotoImage(gif.copy())
            frames.append(frame)
            gif.seek(len(frames))  # Move to the next frame
    except EOFError:
        pass  # End of GIF
    return frames





#main fun call
#For Relative Resource Path
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def f1():
    SP.progress()

def f2():
    final.call_to_main(docpath,xlpath,opfolderpath)    
    print("Done!")
    
    
    
    
def progress3():

 
    # GUI setup
    root = tk.Tk()
    root.title("BillForge")
    #loading_label = ttk.Label(loading_frame, text="Generating...", font=("Helvetica", 12))
    #loading_label.grid(row=2, column=0, columnspan=2, pady=5)
       
    def simulate_long_running_task():
        # Simulate a long-running task
        
        #final.main()
        #ep.emailextract(xlpath, opfolderpath)
        final.call_to_main(docpath,xlpath,opfolderpath)
        
        
    def simulate_long_running_task2():
        # Simulate a long-running task
      
        #final.main()
        SP.progress()
        #ep.emailextract(xlpath, opfolderpath)

    def start_loading():
        loading_frame.pack()
        # Start a new thread for the long-running task
        threading.Thread(target=simulate_long_running_task, daemon=True).start()
        # Poll the thread to check if it's still running
        root.after(100, check_thread)
        threading.Thread(target=simulate_long_running_task2, daemon=True).start()
        # Poll the thread to check if it's still running
        root.after(100, check_thread)

    def check_thread():
        #global loading_label
        # Check if the thread is still running
        if threading.active_count() > 1:
            # If the thread is still running, schedule another check
            print("Process Running .....")
            #loading_label = ttk.Label(loading_frame, text="Generating...", font=("Helvetica", 12))
            #loading_label.grid(row=2, column=0, columnspan=2, pady=5)
            root.after(100, check_thread)
        else:
            # If the thread has finished, hide the loading frame
            loading_frame.pack_forget()
            root.destroy()
            
    
    
    
    

    # Create a frame for the loading spinner with a width of 4 inches
    loading_frame = ttk.Frame(root, width=4*root.winfo_fpixels('1i'))
    loading_label = ttk.Label(loading_frame, text="Bill Generation in progress , please wait...", font=("Helvetica", 12))
    loading_label.grid(row=1, column=0, columnspan=2, pady=5)
    loading_spinner = ttk.Progressbar(loading_frame, mode="indeterminate")
    
    

    loading_label.pack(pady=10)
    loading_spinner.pack()

    #  start the loading process
    start_loading()

    root.mainloop()

    
    



    



def progress2():

 
    # GUI setup
    root = tk.Tk()
    root.title("BillForge")
    #loading_label = ttk.Label(loading_frame, text="Generating...", font=("Helvetica", 12))
    #loading_label.grid(row=2, column=0, columnspan=2, pady=5)
       
    def simulate_long_running_task():
        # Simulate a long-running task
       
        #final.main()
        ep.emailextract(xlpath, opfolderpath,docpath)

    def start_loading():
        loading_frame.pack()
        # Start a new thread for the long-running task
        threading.Thread(target=simulate_long_running_task, daemon=True).start()
        # Poll the thread to check if it's still running
        root.after(100, check_thread)

    def check_thread():
        #global loading_label
        # Check if the thread is still running
        if threading.active_count() > 1:
            # If the thread is still running, schedule another check
            print("Process Running .....")
            #loading_label = ttk.Label(loading_frame, text="Generating...", font=("Helvetica", 12))
            #loading_label.grid(row=2, column=0, columnspan=2, pady=5)
            root.after(100, check_thread)
        else:
            # If the thread has finished, hide the loading frame
            loading_frame.pack_forget()
            root.destroy()
            
            
            


    # Create a frame for the loading spinner with a width of 4 inches
    loading_frame = ttk.Frame(root, width=4*root.winfo_fpixels('1i'))
    loading_label = ttk.Label(loading_frame, text="Email Sending in progress , please wait...", font=("Helvetica", 12))
    loading_label.grid(row=1, column=0, columnspan=2, pady=5)
    loading_spinner = ttk.Progressbar(loading_frame, mode="indeterminate")
    
    

    loading_label.pack(pady=10)
    loading_spinner.pack()

    #  start the loading process
    start_loading()

    root.mainloop()

    
    





def progress():

 
    # GUI setup
    root = tk.Tk()
    root.title("BillForge")
    #loading_label = ttk.Label(loading_frame, text="Generating...", font=("Helvetica", 12))
    #loading_label.grid(row=2, column=0, columnspan=2, pady=5)
       
    def simulate_long_running_task():
        # Simulate a long-running task
        #final.main()
        final.call_to_main(docpath,xlpath,opfolderpath)

    def start_loading():
        loading_frame.pack()
        # Start a new thread for the long-running task
        threading.Thread(target=simulate_long_running_task, daemon=True).start()
        # Poll the thread to check if it's still running
        root.after(100, check_thread)

    def check_thread():
        #global loading_label
        # Check if the thread is still running
        if threading.active_count() > 1:
            # If the thread is still running, schedule another check
            print("Process Running .....")
            #loading_label = ttk.Label(loading_frame, text="Generating...", font=("Helvetica", 12))
            #loading_label.grid(row=2, column=0, columnspan=2, pady=5)
            root.after(100, check_thread)
        else:
            # If the thread has finished, hide the loading frame
            loading_frame.pack_forget()
            root.destroy()


    # Create a frame for the loading spinner with a width of 4 inches
    loading_frame = ttk.Frame(root, width=4*root.winfo_fpixels('1i'))
    loading_label = ttk.Label(loading_frame, text="Bill Generation in progress , please wait...", font=("Helvetica", 12))
    loading_label.grid(row=1, column=0, columnspan=2, pady=5)
    loading_spinner = ttk.Progressbar(loading_frame, mode="indeterminate")
    
    

    loading_label.pack(pady=10)
    loading_spinner.pack()

    #  start the loading process
    start_loading()

    root.mainloop()

    
    
    
    
    
def MultiT():
    # Create threads for f1 and f2
      thread_f1 = threading.Thread(target=f1)
      thread_f2 = threading.Thread(target=f2)

# Start the threads
      thread_f1.start()
      thread_f2.start()

# Wait for f2 to finish before exiting the program
      thread_f2.join()
   
    
    




xlpath = "demo"
docpath = "demo"
opfolderpath = "demo"


def gui2():
    # # Get the current script's directory
    # SCRIPT_PATH = Path(__file__).parent
    # ASSETS_PATH = SCRIPT_PATH

    # def relative_to_assets(path: str) -> Path:
    #     return ASSETS_PATH / Path(path)

    # window = tk.Tk()
    # window.title("BillForge")
    # window.geometry("770x550")
    # window.configure(bg="#F0FBEB")

    # canvas = Canvas(
    #     window,
    #     bg="#F0FBEB",
    #     height=550,
    #     width=770,
    #     bd=0,
    #     highlightthickness=0,
    #     relief="ridge"
    # )

    # canvas.place(x=0, y=0)

    # # image_image_1 = PhotoImage(file=relative_to_assets(resource_path("data\\images\\image_12.png")))
    # # image_1 = canvas.create_image(
    # #     376.0,
    # #     148.0,
    # #     image=image_image_1
    # # )
    
    # # Load the animated GIF
    # gif_frames = load_gif(relative_to_assets(resource_path("data\\images\\image_13.gif")))

    # # Create a label to display the animated GIF
    # image_label = canvas.create_window(376.0, 148.0, window=Canvas(canvas, width=gif_frames[0].width(), height=gif_frames[0].height()))

    # # Start the animation
    # animate_gif(image_label, gif_frames)

    # canvas.create_text(
    #     314.0,
    #     312.0,
    #     anchor="nw",
    #     text="Bill Generator",
    #     fill="#0F32E9",
    #     font=("Imprima Regular", 20 * -1)
    # )

    # canvas.create_text(
    #     19.0,
    #     369.0,
    #     anchor="nw",
    #     text="Select Bill Docx File:",
    #     fill="#000000",
    #     font=("Imprima Regular", 15 * -1)
    # )

    # canvas.create_text(
    #     20.0,
    #     450.0,
    #     anchor="nw",
    #     text="Select Destination :",
    #     fill="#000000",
    #     font=("Imprima Regular", 15 * -1)
    # )

    # canvas.create_text(
    #     19.0,
    #     408.0,
    #     anchor="nw",
    #     text="Select Excel File: ",
    #     fill="#000000",
    #     font=("Imprima Regular", 15 * -1)
    # )
     # Get the current script's directory
    SCRIPT_PATH = Path(__file__).parent
    ASSETS_PATH = SCRIPT_PATH

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    window = tk.Tk()
    window.title("BillForge-General Version")
    window.geometry("770x550")
    window.configure(bg="#F0FBEB")
    #icon_path = r"D:\New folder\Working Area 7\Tkinter Design 3\build\assets\frame0\logo.ico"  # Full path to your .ico file
    window.iconbitmap(resource_path('data\\images\\general_logo.ico'))

    canvas = Canvas(
        window,
        bg="#F0FBEB",
        height=550,
        width=770,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    # Load the animated GIF
    gif_frames = load_gif(relative_to_assets(resource_path("data\\images\\image_14_green.gif")))

    # Create a label to display the animated GIF
    gif_label = tk.Label(canvas, bg= "#F0FBEB")  # Create a label widget instead of a window
    gif_label_window = canvas.create_window(376.0, 148.0, window=gif_label)  # Place the label in the canvas

    # Start the animation
    animate_gif(gif_label, gif_frames)  # Use the label here

    canvas.create_text(
        258.0,
        312.0,
        anchor="nw",
        text="Bill Generator General Version",
        fill="#0F32E9",
        font=("Imprima Regular", 20 * -1)
    )

    canvas.create_text(
        19.0,
        369.0,
        anchor="nw",
        text="Select Bill Docx File:",
        fill="#000000",
        font=("Imprima Regular", 15 * -1)
    )

    canvas.create_text(
        20.0,
        450.0,
        anchor="nw",
        text="Select Destination :",
        fill="#000000",
        font=("Imprima Regular", 15 * -1)
    )

    canvas.create_text(
        19.0,
        408.0,
        anchor="nw",
        text="Select Excel File: ",
        fill="#000000",
        font=("Imprima Regular", 15 * -1)
    )

    doc_entry_var = tk.StringVar()
    xl_entry_var = tk.StringVar()
    folder_entry_var = tk.StringVar()

    entry_image_1 = PhotoImage(file=relative_to_assets(resource_path("data\\images\\doc_entry.png")))
    entry_bg_1 = canvas.create_image(
        387.0,
        378.0,
        image=entry_image_1
    )
    doc_entry = Entry(
        bd=0,
        bg="#A6F0BF",
        fg="#000716",
        highlightthickness=0,
        textvariable=doc_entry_var,
        state='disabled'
    )
    doc_entry.place(
        x=168.0,
        y=363.0,
        width=438.0,
        height=28.0
    )

    entry_image_2 = PhotoImage(file=relative_to_assets(resource_path("data\\images\\xl_entry.png")))
    entry_bg_2 = canvas.create_image(
        387.0,
        418.0,
        image=entry_image_2
    )
    xl_entry = Entry(
        bd=0,
        bg="#A6F0BF",
        fg="#000716",
        highlightthickness=0,
        textvariable=xl_entry_var,
        state='disabled'
    )
    xl_entry.place(
        x=168.0,
        y=403.0,
        width=438.0,
        height=28.0
    )

    entry_image_3 = PhotoImage(file=relative_to_assets(resource_path("data\\images\\folder_entry.png")))
    entry_bg_3 = canvas.create_image(
        387.0,
        458.0,
        image=entry_image_3
    )
    folder_entry = Entry(
        bd=0,
        bg="#A6F0BF",
        fg="#000716",
        highlightthickness=0,
        textvariable=folder_entry_var,
        state='disabled'
    )
    folder_entry.place(
        x=168.0,
        y=443.0,
        width=438.0,
        height=28.0
    )

    def open_doc_dialog():
        global docpath
        doc_file_path = filedialog.askopenfilename(title="Select a .doc File", filetypes=[("Word files", "*.docx")])
        doc_entry_var.set(doc_file_path)
        docpath = doc_file_path
        if doc_file_path:
            doc_file_name = os.path.basename(doc_file_path)
            print(f"Selected .docx File: {doc_file_path}")

    def open_xl_dialog():
        global xlpath
        xl_file_path = filedialog.askopenfilename(title="Select a .xlsx File", filetypes=[("Excel files", "*.xlsx")])
        xl_entry_var.set(xl_file_path)
        xlpath = xl_file_path
        if xl_file_path:
            xl_file_name = os.path.basename(xl_file_path)
            print(f"Selected .xlsx File: {xl_file_path}")

    def open_folder_dialog():
        global opfolderpath
        folder_path = filedialog.askdirectory(title="Select a Folder")
        folder_entry_var.set(folder_path)
        opfolderpath = folder_path
        if folder_path:
            print(f"Selected Folder: {folder_path}")

    def edit_email():
        excel_file_path = xlpath
        if os.path.exists(excel_file_path):
            os.system(f'start excel "{excel_file_path}"')
        else:
            print(f"File '{excel_file_path}' not found.")

    def send_email():
        print("Send Email button clicked")
        progress2()
        #ep.emailextract(xlpath, opfolderpath)  

    def generate():
        print("Generate button clicked")
        #MultiT()
        #final.call_to_main(docpath,xlpath,opfolderpath)
        progress()  # Uncomment when progress function is available
        # Perform the main function

    doc_button = tk.Button(window, text="Open .docx File", command=open_doc_dialog, bg="#A6F0BF")
    xl_button = tk.Button(window, text="Open Email File", command=open_xl_dialog, bg="#A6F0BF")
    folder_button = tk.Button(window, text="Open Folder", command=open_folder_dialog, bg="#A6F0BF")

    doc_button.place(x=630.0, y=362.0, width=123.09381103515625, height=31.0)
    xl_button.place(x=630.0, y=402.0, width=123.09381103515625, height=31.0)
    folder_button.place(x=630.0, y=443.0, width=123.09381103515625, height=31.0)

    button_image_4 = PhotoImage(file=relative_to_assets(resource_path("data\\images\\generate_button.png")))
    generate_button = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=generate,
        relief="flat"
    )
    generate_button.place(x=304.0, y=488.0, width=180.0, height=40.0)

    button_image_5 = PhotoImage(file=relative_to_assets(resource_path("data\\images\\send_email_button.png")))
    send_email_button = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=send_email,
        relief="flat"
    )
    send_email_button.place(x=611.0, y=490.0, width=142.39999389648438, height=38.0)

    button_image_6 = PhotoImage(file=relative_to_assets(resource_path("data\\images\\edit_email_button.png")))
    edit_email_button = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=edit_email,
        relief="flat"
    )
    edit_email_button.place(x=25.0, y=488.0, width=142.0, height=37.822479248046875)

    window.resizable(False, False)
    window.mainloop()

# Call the gui2 function
#gui2()

