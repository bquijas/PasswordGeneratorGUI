import tkinter as tk
from tkinter import ttk
import pandas as pd
import random
import string

#Entry classes
main = tk.Tk() #this makes a plain window
label_name = tk.Label(main, text="Please enter desired password length: ",
                 font=('helvetica',14,'bold'))

length_var = tk.IntVar() #declares an integer variable
complex_slider = tk.IntVar() #declares an integer variable

length_entry = tk.Entry(main, #length prompt details
    textvariable = length_var, 
    font=('calibre',14,'normal'))

label_complex = ttk.Label(main, text="Password Complexity: ",
                 font=('helvetica',14,'bold'))
label_complex.pack()

complex_slider = ttk.Scale(main, from_=1, to=3, orient="horizontal")    #the complexity slider details
complex_slider.pack()

def passwordGen():  
    #Gets the password length and complexity
    length = length_var.get()
    complexity = complex_slider.get()
    
    #initializing the password and the characters that make it up
    password = ""
    chars = ""

    #Setting the parameters for different complexity states for the slider
    if complexity == 1:
        chars = string.ascii_letters
    elif complexity == 2:
        chars = string.ascii_letters + string.digits
    elif complexity == 3:
        chars = string.ascii_letters + string.digits + string.punctuation

    #This is what will build/generate the password based on the user input
    #We imported random so that random chars can be chosen to make up the password
    for i in range(length):
        password+=random.choice(chars)
    final.set(password)
 
    print("Password:", password)        #output
    print("Complexity: ", complexity)   #output

submit_button = tk.Button(main,         #submit button
    text="Submit",
    font=('calibre',14,'normal'),
    command = passwordGen)

label_name.pack()
length_entry.pack()
label_complex.pack()
submit_button.pack()

#Displaying the final generated password after submission:

final = tk.StringVar()                  #return
password_label = ttk.Label(main, textvariable=final)
password_label.pack()


main.mainloop()
