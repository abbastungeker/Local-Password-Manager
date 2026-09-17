# Password Manager

A simple desktop password manager built with Python and Tkinter.

This project allows users to generate random passwords and save account details such as the website, email/username, and password to a local text file.

## Features

- Generate random passwords between 10–20 characters
- Uses lowercase letters, uppercase letters, numbers, and symbols
- Automatically inserts the generated password into the password field
- Save website, email/username, and password details
- Displays warning messages if any required fields are empty
- Displays a success message after details are saved
- Automatically creates a local `Data.txt` file when account details are saved
- Sets the cursor focus to the website field when the program starts
- Includes a default email/username value for quicker data entry

## Technologies Used

- Python
- Tkinter
- Python `random` module
- File handling

## How It Works

1. Enter the website name.
2. Enter your email or username.
3. Either type a password manually or click **Generate Password**.
4. Click **Add** to save the account details.
5. The information is stored locally in `Data.txt`.

## Project Structure

```text
password-manager-tkinter/
├── main.py
├── Key.png
└── README.md
