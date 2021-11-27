import requests
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

key=open("api_key.txt")
# Basic information about API
api = key.readlines()[0]


# Conversion Function
def convert_currency(your_api_code, converted_rate, from_, to, amount):
	data = requests.get(f'https://v6.exchangerate-api.com/v6/{api}/pair/{from_[:3]}/{to[:3]}/{amount}')

	res = data.json()

	converted_rate.set(str(res['conversion_result']))


# Creating a GUI window for the project
root = Tk()
root.title("Sagveek Currency Converter")
root.geometry('500x250')
root.resizable(0, 0)
root.configure(bg='RoyalBlue')


# Assigning a logo to the GUI
logo = ImageTk.PhotoImage(Image.open('Sagveek_Logo.png'))
root.iconphoto(False, logo)


# Creating a Heading for the window
Label(root, text='Sagveek Currency Converter', font=('Comic Sans MS', 18), bg='RoyalBlue').place(x=70)


# Creating a StringVar object of the list of currencies
li_currencies = list()   # Variable name 'li_currencies' is a contraction of 'list_of_currencies'

codes = f'https://v6.exchangerate-api.com/v6/{api}/codes'
codes_res = requests.get(codes)

for pair in codes_res.json()['supported_codes']:
	li_currencies.append(f'{pair[0]} - {pair[1]}')


# 'Convert from' portion of the window
Label(root, text='Convert from:', font=('Georgia', 13, 'italic'), bg='RoyalBlue').place(x=60, y=60)

amnt_from = Entry(root, width=25)
amnt_from.place(x=45, y=100)

FROM__currency_names = ttk.Combobox(root, state='readonly', values=li_currencies, width=30)
FROM__currency_names.place(x=20, y=140)
FROM__currency_names.current((li_currencies.index("INR - Indian Rupee")))


# 'Convert to' portion of the window
Label(root, text='Convert to:', font=('Georgia', 13, 'italic'), bg='RoyalBlue').place(x=330, y=60)

converted_currency = StringVar(root)
amnt_to = Entry(root, width=25, textvariable=converted_currency)
amnt_to.place(x=300, y=100)

TO__currency_names = ttk.Combobox(root, state='readonly', values=li_currencies, width=30)
TO__currency_names.place(x=275, y=140)
TO__currency_names.current((li_currencies.index("INR - Indian Rupee")))


# Submit Button
submit_btn = Button(root, text='Submit', bg='SpringGreen', command=lambda: convert_currency(api, converted_currency,
                                        FROM__currency_names.get(), TO__currency_names.get(), amnt_from.get()))
submit_btn.place(x=225, y=190)


# Finalizing the GUI
root.update()
root.mainloop()
