# All the imports
from tkinter import *
import requests

root = Tk()
root.title("Currency Converter")
root.geometry("500x500")
root.config(bg="green")

value = IntVar()

information = requests.get('https://v6.exchangerate-api.com/v6/89dcd9e8cc7777ded2575ce1/latest/USD')
information_json = information.json()

conversion_rate = information_json['conversion_rates']

value_label = Label(root, text="Value", font=("Arial", 20))
value_label.config(bg="white")
value_label.pack()

value_entry = Entry(root, textvariable=value, width=40)
value_entry.config(bg="white")
value_entry.pack()

from_label = Label(root, text="From: USD", font=("Arial", 20))
from_label.config(bg="white")
from_label.pack()

convert = Label(root, text="To:", font=("Arial", 20))
convert.config(bg="white")
convert.pack()

convert_list = Listbox(root, width=20)
for i in conversion_rate.keys():
    convert_list.insert(END, str(i))
    convert_list.pack()

convert_label = Label(root, text="Converted to: ", font=("", 20))
convert_label.config(bg="white")
convert_label.pack()


def convert_curr():
    num = float(value_entry.get())
    print(information_json['conversion_rates'][convert_list.get(ACTIVE)])
    ans = num * information_json['conversion_rates'][convert_list.get(ACTIVE)]
    convert_label['text'] = ans


convert_btn = Button(root, command=convert_curr, text="Convert", font=("Arial", 20), width=20)
convert_btn.config(bg="white")
convert_btn.pack()


root.mainloop()