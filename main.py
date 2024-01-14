from tkinter import *
import customtkinter as ttk

Converter = ttk.CTk()
Converter.title("Unit Converter")
Converter.geometry("700x500")
Converter.resizable(False, False)
Converter.config(bg="black")

menuOptions = ['fit', 'inch', 'km', 'cm', 'dm', 'mm', 'nm', 'mile', 'yard', 'm', 'micro']
value1 = StringVar()
value2 = StringVar()

logoPhoto = PhotoImage(file='assets/UNIT CONVERTER.png')
logo = logoPhoto.subsample(1, 1)

Label(Converter, image=logo, background="black").pack(pady=60)

inputOne = ttk.CTkFrame(Converter, fg_color="black", bg_color="black")

Input1 = ttk.CTkEntry(inputOne, width=350, height=40, textvariable=value1)
Input1.pack(padx=20, pady=10, side=LEFT)

combobox1 = ttk.CTkOptionMenu(master=inputOne,
                              values=menuOptions)
combobox1.pack(padx=20, pady=10, side=LEFT)
combobox1.set(menuOptions[0])

inputOne.pack(pady=10)
inputOne.focus()

inputTwo = ttk.CTkFrame(Converter, fg_color="black", bg_color="black")

Input2 = ttk.CTkEntry(inputTwo, width=350, height=40, textvariable=value2)
Input2.pack(padx=20, pady=10, side=LEFT)

combobox2 = ttk.CTkOptionMenu(master=inputTwo,
                              values=menuOptions)
combobox2.pack(padx=20, pady=10, side=LEFT)
combobox2.set(menuOptions[1])

inputTwo.pack(pady=10)
inputTwo.focus()


def converter():
    if combobox1.get() == "inch" and combobox2.get() == "cm":
        Input2.insert(0, int(value1.get()) * 2.54)
    elif combobox1.get() == "inch" and combobox2.get() == "fit":
        Input2.insert(0, int(value1.get()) / 12)
    elif combobox1.get() == "inch" and combobox2.get() == "m":
        Input2.insert(0, int(value1.get()) / 39.37)
    elif combobox1.get() == "inch" and combobox2.get() == "mm":
        Input2.insert(0, int(value1.get()) / 25.4)
    elif combobox1.get() == "inch" and combobox2.get() == "nm":
        Input2.insert(0, int(value1.get()) / 2.54)


ttk.CTkButton(Converter, text="Convert", font=("", 32, "bold"), bg_color="black", command=converter).pack(pady=20,
                                                                                                          ipadx=10,
                                                                                                          ipady=5)

Converter.mainloop()
