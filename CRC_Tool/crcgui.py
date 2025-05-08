from tkinter import *
from tkinter import Toplevel
import binascii
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter.ttk import Progressbar
from tkinter.messagebox import showinfo
from editedflashcode import flashcode

# ROOT WINDOW
root = Tk()
root.title("Checksum")
root.geometry("700x700")
mc = 'white'
root.configure(background=mc)
root.resizable(False, False)

file_path = ""

# function that opens file explorer and chooses a .hex file
def import_file():
    global file_path
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Hex files", "*.hex"), ("All files", "*.*")])
    if file_path:
        print("Selected file:", file_path)

# function that calculates checksum
def calc_checksum():
    global file_path
    if not file_path:
        print("No file selected")
        return

    # calculates checksum for each line
    def checksum(hex_number):
        hex_number = str(hex_number)
        decimal_list = []
        for i in range(8, len(hex_number) - 2, 2):
            hex_pair = hex_number[i:i + 2]
            if len(hex_pair) == 2:
                decimal_value = int(hex_pair, 16)
                decimal_list.append(decimal_value)
        decimal_sum = sum(decimal_list)
        return decimal_sum

    total_decimal_sum = 0
    with open(file_path, 'r') as file:
        for line in file:
            hex_number = line.lstrip(':').strip()  # starts reading values per line after the colon
            if hex_number[6:8] == '00':
                decimal_sum = checksum(hex_number)
                total_decimal_sum += decimal_sum  # adds checksum of all lines

    total = str(hex(total_decimal_sum))
    total_hex_sum = '0x' + total[4:]
    result_label.config(text=f"{total_hex_sum}", fg='black')

# function that uses binascii.crc32 method to find unsigned 32-bit checksum of data
def crc():
    global file_path
    if not file_path:
        print("No file selected")
        return
    with open(file_path, 'rb') as file:
        fc = file.read()
    crc32_checksum = hex(binascii.crc32(fc) & 0xFFFFFFFF)  # AND so that unsigned crc becomes signed value
    result_label2.config(text=f"{crc32_checksum}", fg='black')

# calculates version of the file
def calc_version():
    global file_path
    if not file_path:
        print("No file selected")

    # searches for specific ID and converts certain indices to decimal to give version
    def find(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                hex_number = line.lstrip(':').strip()
                if hex_number[2:6] == "4CA0":
                    vers_r = hex_number[24:28]
                    vers_l = hex_number[28:32]
                    decr = int(vers_r, 16)
                    decl = int(vers_l, 16)

                    result_label3.config(text=f"{decr}.{decl}", fg='black')
                    return
        result_label3.config(text="Version not found", fg='black')

    find(file_path)

def everything():
    import_file()
    calc_checksum()
    crc()
    calc_version()

# function to upload file onto client
def flash():
    print ("we're working on it")
    flashcode(root, file_path)
    

def reset():  # resets result labels so new file can be uploaded
    result_label.config(text="")
    result_label2.config(text="")
    result_label3.config(text="")

if __name__ == "__main__":
    # LOAD AND SET BACKGROUND IMAGE
    bg = ImageTk.PhotoImage(file="/Users/smrithi/Downloads/ig1.png")
    labelbg = Label(root, image=bg)
    labelbg.pack(padx=190, pady=12)
    labelbg.place(x=0, y=0)

    # LOGO
    image_path = "/Users/smrithi/Downloads/plug-logo.png"
    try:
        pil_image = Image.open(image_path)
    except IOError:
        print(f"Unable to open image file {image_path}")
        exit()
    image = ImageTk.PhotoImage(pil_image)
    label = Label(root, image=image, bg=mc, highlightbackground="white")
    label.pack(padx=190, pady=5)

    # HEADINGS AND SUBHEADINGS
    w = Label(root, text='DC-DC Converter', fg='black', font=('Kalinga', 20, 'bold'), bg=mc)
    w.pack(pady=6)
    w2 = Label(root, text='Intel Hex – Checksum Utility V1.0', fg='black', font=('Kalinga', 14, 'bold'), bg=mc)
    w2.pack(pady=3)
    button1 = Button(root, text="Upload your file", bg="white", command=everything, relief="flat", highlightbackground="black", height=1, width=9)
    button1.pack(pady=8, padx=100)

    # RESULT CANVAS
    bgc = '#3aa25a'
    canvas4 = Canvas(root, bg=bgc, width=600, height=300, highlightthickness=2)
    canvas4.pack_propagate(False)
    canvas4.pack()

    # RESULT NAMES
    canvas1 = Canvas(canvas4, bg='white', height=25, highlightthickness=2)
    canvas1.pack(fill=X, padx=10, pady=25)
    dis = Label(canvas4, text='16-bit Checksum', fg='white', font=('Kalinga', 14), bg=bgc)
    dis.pack(anchor='w', padx=10)
    dis.place(x=7, y=57)
    result_label = Label(canvas4, text="", font=("Kalinga", 12), bg='white')
    canvas1.create_window((5, 14), window=result_label, anchor='w')

    canvas2 = Canvas(canvas4, bg='white', height=25, highlightthickness=2)
    canvas2.pack(fill=X, padx=10, pady=25)
    dis2 = Label(canvas4, text='CRC', fg='white', font=('Kalinga', 13), bg=bgc)
    dis2.pack(anchor='w', padx=10)
    dis2.place(x=7, y=138)
    result_label2 = Label(canvas4, text="", font=("Kalinga", 12), bg='white')
    canvas2.create_window((5, 14), window=result_label2, anchor='w')

    canvas3 = Canvas(canvas4, bg='white', height=25, highlightthickness=2)
    canvas3.pack(fill=X, padx=10, pady=25)
    dis3 = Label(canvas4, text='Software Version', fg='white', font=('Kalinga', 14), bg=bgc)
    dis3.pack(anchor='w', padx=10)
    dis3.place(x=7, y=218)
    result_label3 = Label(canvas4, text="", font=("Kalinga", 12), bg='white')
    canvas3.create_window((5, 14), window=result_label3, anchor='w')

    # FLASH BUTTON
    button2 = Button(root, text="FLASH", bg="white", command=flash, height=2, width=7)
    button2.pack(padx=50)
    button2.place(relx=0.32, rely=0.75)

    # RESET BUTTON
    reset = Button(root, text="RESET", bg="white", command=reset, height=2, width=7)
    reset.place(relx=0.52, rely=0.75)
    root.mainloop()
