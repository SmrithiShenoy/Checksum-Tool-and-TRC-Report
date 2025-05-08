'''GUI that imports user-defined modules to take a .trc
file and convert it to colour coded excel filesbased on certain criteria'''

#importing in-built modules
from tkinter import *
import csv
from tkinter import filedialog
from tkinter import font
import tkinter as tk
import pandas as pd

#importing user-defined modules
from colourcoding import colourcoding
from showgraph import showgraph 
from newexcel import newexcel
from filterfile import filterfile
from convert import trc_to_csv

#Creating main window of GUI
root = Tk()
root.title("Filtered Excel generator")
root.geometry("500x300")
root.configure(background='pink')

#function to create file path in the same directory for converted csv
def process_file():
    global fil_path
    trc_to_csv(trc_path)
    #splitting the trc file path and appendind the name of the filtered file 
    l = trc_path.split("/")
    if trc_path[0] == '/':
        fil_path = '/'
    else:
        fil_path = ''
    for i in range(0, len(l) - 1):
        fil_path += l[i] + "/"
    fil_path += "filtered.csv"
    filterfile(fil_path)
    print("Processing completed.")
    csv_to_excel(fil_path) 

#function that uses pandas to convert .csv to .xlsx file with the same name
def csv_to_excel(csv_file_path):
    n=int(enterno.get())
    df = pd.read_csv(csv_file_path,encoding='utf-8')
    global excel_file_path
    excel_file_path = csv_file_path.replace('.csv', '.xlsx')
    df.to_excel(excel_file_path, index=False)
    print(f"Excel file created at {excel_file_path}.")
    colourcoding(excel_file_path)
    newexcel(excel_file_path, n)

#function that opens file explorer 
def import_file():
    global trc_path
    trc_path = filedialog.askopenfilename(title="Select a file", filetypes=[("TRC files", "*.trc"), ("All files", "*.*")])
    if trc_path:
        print("Selected file:", trc_path)

#function that displays graph for parameters 
def graph():
    showgraph(fil_path)


#Elements of the GUI like buttons, entry and labels
if __name__ == "__main__":
    n=0
    w = Label(root, text='PARAMETER ANALYZER', fg='black', justify="left", font=('Helvetica', 20, 'bold'), bg="pink")
    w.pack(pady=5, padx=20, anchor="w")
    w.place(relx=0.024, rely=0.1)
    w2 = Label(root, text='Produce an EXCEL file with filtered and calculated parameters', fg='black', justify="left", font=('Helvetica', 14), bg="pink")
    w2.pack(pady=10, padx=10, anchor="w")
    w2.place(relx=0.024, rely=0.25)

    button1 = Button(root, text="Upload your TRC file", bg="white", command=import_file, relief="sunken")
    button1.place(x=15, y=130)
    fil_path_label = Label(root, text="Enter number of entries before error", fg="black", bg="white", font=('Helvetica', 13))
    fil_path_label.place(x=15, y=190)
    enterno=Entry(root, text=n)
    enterno.place(x=250, y=185)
    process_button = Button(root, text="Process File", bg="white", command=process_file)
    process_button.place(x=15, y=250)
    graph_button=Button(root, text="Show Graph", bg="white", command=graph)
    graph_button.place(x=150, y=250)

    

    root.mainloop()
