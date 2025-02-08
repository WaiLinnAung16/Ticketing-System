import customtkinter
import dashboard
import validation

# Create Login Window
app = customtkinter.CTk()
app.title("Centrala Ticketing System")

screen_w = '400'
screen_h = '600'

app.geometry(f'{screen_w}x{screen_h}+0+0')

# Initialize global variables for error messages
username_error = None
password_error = None

# class Authentication():
#     """Check login entry username and password are correct."""
#     def __init__(self, username, password):
#         self.correct_username = 'admin'
#         self.correct_password = 'admin123'

#         if not username:
#             raise validation.EmptyInput('Username')
#         if not password:
#             raise validation.EmptyInput('Password')
#         if username != self.correct_username:
#             raise validation.AuthenticationError("Invalid Username!")
#         if password != self.correct_password:
#             raise validation.AuthenticationError("Invalid Password!")
    # try:
    #     Authentication(username_entry.get(), password_entry.get())
    # except Exception as e:
    #     error_message = customtkinter.CTkLabel(app, text=e, text_color="red")
    #     error_message.grid(row=3,column=0)

# Login Window
def login():
    global username_error, password_error  # Use global variables to keep track of error labels
    credentials = {'username': 'admin', 'password': 'admin123'}
    username = username_entry.get()
    password = password_entry.get()

    # Remove previous error messages if they exist
    if username_error:
        username_error.destroy()
        username_error = None  # Reset variable

    if password_error:
        password_error.destroy()
        password_error = None  # Reset variable

    if username != credentials["username"]:
        username_error = customtkinter.CTkLabel(app, text='Invalid Username!', text_color="red")
        username_error.place(relx=0.45, rely=0.44, anchor="center")
    elif password != credentials["password"]:  # TODO: Password Length
        password_error = customtkinter.CTkLabel(app, text='Invalid Password!', text_color="red")
        password_error.place(relx=0.45, rely=0.54, anchor="center")
    else:
        app.destroy()  # Close the login window
        dashboard.open_main_window(screen_w,screen_h)  # Open the new main window

# Login Header
loginHeader = customtkinter.CTkLabel(app, text="Login", font=("Arial", 20))
loginHeader.place(relx=0.5, rely=0.3, anchor="center")  

# Username Entry
username_entry = customtkinter.CTkEntry(app, placeholder_text='Username',width=250)
username_entry.place(relx=0.5, rely=0.4, anchor="center")

# Password Entry
password_entry = customtkinter.CTkEntry(app, placeholder_text='Password',width=250)
password_entry.place(relx=0.5, rely=0.5, anchor="center")

# Login Button
loginButton = customtkinter.CTkButton(app, text='Login', command=login, width=150)
loginButton.place(relx=0.5, rely=0.6, anchor="center")

app.mainloop()
