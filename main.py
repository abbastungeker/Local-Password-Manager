# ---------------------------- Imports ------------------------------- #
from tkinter import *
from tkinter import messagebox
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def Password_Generate():
#Empty password list to store characters into
    password = []
# Lists the code will be randomly selecting from, includes letters, numbers and symbols
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# Randomly Selects the length of the password with a minimum of 10 characters and 40 characters
    length_of_password = random.randint(10, 20)
# Main for loop that will run until the random length of the password ends
    for character in range(length_of_password):
        #selects at random whether a letter or symbol is chosen
        character_selector = random.randint(1, 4)
        # Letter sequence
        if character_selector == 1:
            item = random.choice(letters)
            password.append(item)
        # Letter sequence
        if character_selector == 2:
            item = random.choice(letters).upper()
            password.append(item)
        # Numbers sequence
        if character_selector == 3:
            item = random.choice(numbers)
            password.append(item)
        # Symbols sequence
        if character_selector == 4:
            item = random.choice(symbols)
            password.append(item)
# Converts password list into string
    password = "".join(password)

    password_entry.delete(0, END)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def Warning_message():
    messagebox.showwarning(title="Entry Error", message="Please enter all field-boxes to successfully store details")

def Data_Insertion():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()

    if website != "" and email_username != "" and password != "":
        with open("Data.txt", mode="a") as Data:
            Data.write(f"\n{website} | {email_username} | {password}")
        messagebox.showinfo(title="Successful Storage", message=f"Your details for {website} have been successfully saved.")

    else:
        Warning_message()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Abbas' Password Manager")
window.geometry("450x375")
window.config(
    bg= '#E3E4E8',
    pady= 10,
    padx=10)
window.resizable(False, False)

key_logo = PhotoImage(file="Key.png")

#Canvas Code
canvas = Canvas(  #Sets the base parameters for the canvas in use
    bg= "#E3E4E8",
    width=200,
    height=200,
    highlightthickness=0
)

canvas.grid(
    column= 2,
    row= 0
)

canvas.create_image(130, 100, image=key_logo)



#WEBSITE SECTION
#Website Label
website_label= Label(text= "Website", font=("Arial",9), width= 10, bg='#E3E4E8', highlightthickness=0)
website_label.grid(
    column=0,
    row=1
)
#Website Entry box
website_entry = Entry(width=50)
website_entry.focus()
website_entry.grid(
    column=1,
    row= 1,
    columnspan=3,
    padx= (10,0)
)

#EMAIL/USERNAME SECTION
#Email/Username Label
email_username_label= Label(text= "Email/Username",font=("Arial",9), width= 13, bg='#E3E4E8', highlightthickness=0)
email_username_label.grid(
    column= 0,
    row=2
)
#Email/Username Entry
email_username_entry = Entry(width=50)
email_username_entry.insert(0, "sample@gmail.com")
email_username_entry.grid(
    row=2,
    column=1,
    columnspan=3,
    padx= (10,0)
)

#PASSWORD SECTION
#Password label
password_label = Label(text="Password", font=("Arial",9), width=10, bg="#E3E4E8", highlightthickness=0)
password_label.grid(
    column=0,
    row=3
)
#Password Entry
password_entry = Entry(width=30)
password_entry.grid(
    column=1,
    row= 3,
    columnspan= 2,
    padx= (5,0)
)

#Generate Password Button
password_button = Button(text="Generate Password", width=15, height=1, bg="#E3E4E8", highlightthickness=0, command= Password_Generate)
password_button.grid(
    column= 3,
    row=3
)

#ADD SECTION
#Add Button
add_button = Button(text="Add", width= 43, height=1, bg="#E3E4E8", highlightthickness=0, command= Data_Insertion)
add_button.grid(
    row= 4,
    column=1,
    columnspan= 3,
    padx=(10,0)


)




window.mainloop()