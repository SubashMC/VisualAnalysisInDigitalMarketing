from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

from tkinter import *
from tkinter import filedialog

def browseFiles():
    filename = filedialog.askopenfilename(title="Select CSV file", filetypes=(("CSV files", "*.csv"),))
    label_file_explorer.configure(text="File Selected: " + filename, bg="#09eb58")
    button_2.config(state=NORMAL)  # Enable the Visual button
    button_3.config(state=NORMAL)

def visual():
    # Code for visualizing data from the selected file
    import visualize



def visualpro():
    import VADM_app


window = Tk()
window.title('File Explorer')
window.geometry("650x450")

window.configure(bg="#1f1e1e")


label_file_explorer = Label(window)
label_file_explorer.pack(pady=50)

button_explore = Button(window, text="Browse Files", bg="#2ce897", fg="#262323", relief=SUNKEN, command=browseFiles)
button_explore.pack(pady=20)

button_2 = Button(window, text="Visualize", bg="#2ce897", fg="#262323", relief=SUNKEN, command=visual, state=DISABLED)
button_2.pack(pady=20)

button_3 = Button(window, text="Visualize Pro", bg="#2ce897", fg="#262323", relief=SUNKEN, command=visualpro, state=DISABLED)
button_3.pack(pady=20)

button_exit = Button(window, text="Exit", bg="#2ce897", fg="#262323", relief=GROOVE, command=exit)
button_exit.pack(pady=20)

window.mainloop()

