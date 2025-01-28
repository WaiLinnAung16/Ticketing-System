import customtkinter

def button_callback():
    print("button clicked !!!")

app = customtkinter.CTk()
app.title("Centrala Ticketing System")
app.geometry("400x150")

loginHeader = customtkinter.CTkLabel(app, text="Login").grid(row=0, column=5)
username = customtkinter.CTkEntry(app, placeholder_text='Username').grid(row=1)
password = customtkinter.CTkEntry(app, placeholder_text='Password').grid(row=2)
loginButton = customtkinter.CTkButton(app, text='Login').grid(row=3)

# lable = customtkinter.CTkLabel(app, text="Hello World")
# entry = customtkinter.CTkEntry(app, placeholder_text="CTkEntry")
# button = customtkinter.CTkButton(app, text="my button", command=button_callback)

# lable.pack(padx=20, pady=20)
# entry.pack(padx=20, pady=20)
# button.pack(padx=20, pady=20)

app.mainloop()