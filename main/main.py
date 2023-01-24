from tkinter import *
from tkinter import ttk 
from tkinter import messagebox as tmsg

#colors 
col1 = "#f5f5f5" #off white
col2 = "#333333" # black
col3 = "#8AAAE5" #baby blue
col4 = "#D3D3D3" #light grey

#tkinter
window = Tk()
window.title("Currency Converter")
window.geometry("500x500")
# window.wm_iconbitmap("C:\\Users\\ACER\\Documents\\py project advanced\\convert currency\\idr.ico") 
window.configure(bg=col1)
window.resizable(height=FALSE, width=FALSE)

# definition 1
def convert():
    from forex_python.converter import CurrencyRates
    cr=CurrencyRates()
    # get te var
    from_currency = var1.get() 
    to_currency = var2.get()

    try:
        float(amountentry.get())
    except ValueError:
        tmsg.showinfo("Invalid","Tolong masukan angka dengan benar")
    
    if (amountentry.get()==""):
        tmsg.showinfo("Program Error","Jumlah mata uang anda kosong.\n Masukan jumlah mata uang anda dengan benar.")
    elif (from_currency=="currency" or to_currency=="currency"):
        tmsg.showinfo("Error !!","Anda tidak melakukan pilihan di tombol currency.\n Tekan dan pilih tombol currency di 2 tombol yang berbeda dengan benar.")
        
    else:
        result1 = cr.convert(from_currency,to_currency,float(amountentry.get()))
        new_result = float("{:.4f}".format(result1))
        resultentry.insert(0, str(new_result)) 

def clear():
	amountentry.delete(0, END) 
	resultentry.delete(0, END)

# definition 2
def help():
    button=tmsg.askquestion("kami akan membantu anda ","tekan 'yes' untuk melihat petunjuk")
    if button == "yes":
        msg = "Ikuti petunjuk berikut:\n1.Pilih mata uang yang anda miliki\n2.Pilih mata uang yang ingin anda konversikan\n3.Masukan jumlah uang yang anda ingin konversikan\n4.Tekan tombol convert untuk mendapatkan result\n5.Tekan tombol clear untuk menghapus riwayat konversi anda"
    else:
        msg = "Baiklah kalau begitu"
    tmsg.showinfo("Help", msg)

# Title text
title_text=Label(window,text="Currency Converter", bg=col3,fg=col1,padx=140,pady=10,font=("Times New Roman",18,"bold"), borderwidth=10, relief=RIDGE, bd=5)
title_text.grid()

# main text
from_currency = Label(window, text="From Currency: ",font=("Times New Roman",16,"bold"), bg=col1,fg =col2)
from_currency.place(x=25, y=100)
to_currency = Label(window, text="To Currency: ", font=("Times New Roman",16,"bold"), bg=col1,fg =col2)
to_currency.place(x=25, y=140)
amount = Label(window, text="Amount: ", font=("Times New Roman",16,"bold"), bg=col1,fg =col2)
amount.place(x=25, y=180)
result = Label(window, text="Result: ", font=("Times New Roman",16,"bold"), bg=col1,fg =col2)
result.place(x=25, y= 270)

# List
currency = [
    "IDR",
    "EUR",
    "GBP",
    "JPY",
    "AUD",
]

# value from main text
var1 = StringVar(window)
var1.set("currency")
var2 = StringVar(window)
var2.set("currency")
amountvalue=DoubleVar()
resultvalue=IntVar()

# options
from_options = OptionMenu(window, var1, *currency)
from_options.config(width=25, bd=3)
from_options.place(x=250,y=100)

to_options = OptionMenu(window, var2, *currency)
to_options.config(width=25,bd=3)
to_options.place(x=250, y=140)

# entry label
amountentry = Entry(window, textvariable=amountvalue, bd=4, width=40)
amountentry.place(x=250,y=180)

resultentry = Entry(window, textvariable=resultvalue, bd=4, width=40)
resultentry.place(x=250, y=270)

# Button
amountbutton=Button(text="convert",font=("Times New Roman",14,"bold"), bg=col4, command=convert, width=6,bd=3)
amountbutton.place(x=250, y=210)
resultbutton = Button(text="clear",font=("Times New Roman",14,"bold"), bg=col4, command=clear, width=6,bd=3)
resultbutton.place(x=250, y=300)

# Help Button
help_button=Menu(window)
h1=Menu(help_button,tearoff=0)
h1.add_command(label="help",command=help)
help_button.add_cascade(label="Help",menu=h1)
window.config(menu=help_button)




window.mainloop()
