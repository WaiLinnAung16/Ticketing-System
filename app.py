import customtkinter

# Login Window
def login():
    credentials = {'username': 'admin', 'password': 'admin123'}
    username = username_entry.get()
    password = password_entry.get()

    if username != credentials["username"]:
        username_error = customtkinter.CTkLabel(app, text='Invalid Username!', text_color="red")
        username_error.place(relx=0.5, rely=0.5, anchor="center")
    elif password != credentials["password"]:
        password_error = customtkinter.CTkLabel(app, text='Invalid Password!', text_color="red")
        password_error.place(relx=0.5, rely=0.6, anchor="center")
    else:
        app.destroy()  # Close the login window
        open_main_window()  # Open the new main window

# Create Login Window
app = customtkinter.CTk()
app.title("Centrala Ticketing System")
app.geometry("400x600")

# Login Header
loginHeader = customtkinter.CTkLabel(app, text="Login", font=("Arial", 20))
loginHeader.place(relx=0.5, rely=0.3, anchor="center")  

# Username Entry
username_entry = customtkinter.CTkEntry(app, placeholder_text='Username', width=250)
username_entry.place(relx=0.5, rely=0.45, anchor="center")

# Password Entry
password_entry = customtkinter.CTkEntry(app, placeholder_text='Password', width=250)
password_entry.place(relx=0.5, rely=0.55, anchor="center")

# Login Button
loginButton = customtkinter.CTkButton(app, text='Login', command=login, width=150)
loginButton.place(relx=0.5, rely=0.7, anchor="center")

# Function to create the main window
def open_main_window():
    main_app = customtkinter.CTk()
    main_app.title("Main Dashboard")
    main_app.geometry("600x400")

    welcome_label = customtkinter.CTkLabel(main_app, text="Welcome to the Dashboard!", font=("Arial", 20))
    welcome_label.place(relx=0.5, rely=0.4, anchor="center")

    logout_button = customtkinter.CTkButton(main_app, text="Logout", command=main_app.destroy, width=150)
    logout_button.place(relx=0.5, rely=0.6, anchor="center")

    main_app.mainloop()

app.mainloop()
