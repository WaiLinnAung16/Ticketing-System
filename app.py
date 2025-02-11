import customtkinter as ctk
import dashboard

# TODO: Testing 
# TODO: Window Size

# Create Login Window
app = ctk.CTk()
app.title("Centrala Ticketing System")

# Set the desire window screen width and height
screen_w = '1080'
screen_h = '600'

app.geometry(f'{screen_w}x{screen_h}+300+100')

def login():
    """
    Login function get the username and password from user.
    Validate the username and password is correct and make sure both are not empty.
    If username and password valid close the login window and open the main window.
    """
    username_error = None
    password_error = None
    credentials = {'username': 'admin', 'password': 'admin123'}
    username = username_entry.get() # Username value
    password = password_entry.get() # Password value

    # Remove previous error messages if they exist
    if username_error:
        username_error.destroy()
        username_error = None  # Reset variable

    if password_error:
        password_error.destroy()
        password_error = None  # Reset variable

    if username != credentials["username"]:
        username_error = ctk.CTkLabel(app, text='Invalid Username!', text_color="red")
        username_error.place(relx=0.45, rely=0.45, anchor="center")
    elif password != credentials["password"]:  # TODO: Password Length
        password_error = ctk.CTkLabel(app, text='Invalid Password!', text_color="red")
        password_error.place(relx=0.45, rely=0.55, anchor="center")
    else:
        app.destroy()  # Close the login window
        dashboard.open_main_window(screen_w,screen_h)  # Open the main window

# Login Header
loginHeader = ctk.CTkLabel(app, text="Login", font=("Arial", 20))
loginHeader.place(relx=0.5, rely=0.3, anchor="center")  

# Username Entry
username_entry = ctk.CTkEntry(app, placeholder_text='Username',width=250)
username_entry.place(relx=0.5, rely=0.4, anchor="center")

# Password Entry
password_entry = ctk.CTkEntry(app, placeholder_text='Password',width=250)
password_entry.place(relx=0.5, rely=0.5, anchor="center")

# Login Button
loginButton = ctk.CTkButton(app, text='Login', command=login, width=150)
loginButton.place(relx=0.5, rely=0.6, anchor="center")

app.mainloop()
