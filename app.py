import customtkinter as ctk
from dashboard import open_main_window

# Create Login Window
app = ctk.CTk()
app.title("Centrala Ticketing System")

# Set the desired window size
screen_w = '1080'
screen_h = '600'
app.geometry(f'{screen_w}x{screen_h}+300+100')

# User credentials for validation
CREDENTIALS = {'username': 'admin', 'password': 'admin123'}

def authenticate(username, password):
    """
    Validate username and password.
    Returns True if authentication is successful, else False.
    """
    return username == CREDENTIALS["username"] and password == CREDENTIALS["password"]

def login():
    """Handles user login by validating input fields and providing feedback."""
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    if not username:
        error_label.configure(text="Username cannot be empty!", text_color="red")
    elif not password:
        error_label.configure(text="Password cannot be empty!", text_color="red")
    elif authenticate(username, password):
        app.destroy()
        open_main_window(screen_w, screen_h)
    else:
        error_label.configure(text="Invalid username or password!", text_color="red")

# Login UI Elements
loginHeader = ctk.CTkLabel(app, text="Login", font=("Arial", 20))
loginHeader.place(relx=0.5, rely=0.3, anchor="center")  

username_entry = ctk.CTkEntry(app, placeholder_text='Username', width=250)
username_entry.place(relx=0.5, rely=0.4, anchor="center")

password_entry = ctk.CTkEntry(app, placeholder_text='Password', width=250, show="*")
password_entry.place(relx=0.5, rely=0.5, anchor="center")

error_label = ctk.CTkLabel(app, text="", text_color="red")  # Placeholder for error messages
error_label.place(relx=0.5, rely=0.55, anchor="center")

loginButton = ctk.CTkButton(app, text='Login', command=login, width=150)
loginButton.place(relx=0.5, rely=0.6, anchor="center")

app.mainloop()
