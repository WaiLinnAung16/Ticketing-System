data = [["ID",'Zone','Stations'],
        ["1","Central Zone",'Station one, Station Two'],
        ["2","Central Zone 1",'Station one 1, Station Two 1'],
        ]

for row in data:
    for col in row:
        print(col,end='')

class Authentication():
    """Check login entry username and password are correct."""
    def __init__(self, username, password):
        self.correct_username = 'admin'
        self.correct_password = 'admin123'

        if not username:
            raise validation.EmptyInput('Username')
        if not password:
            raise validation.EmptyInput('Password')
        if username != self.correct_username:
            raise validation.AuthenticationError("Invalid Username!")
        if password != self.correct_password:
            raise validation.AuthenticationError("Invalid Password!")
    try:
        Authentication(username_entry.get(), password_entry.get())
    except Exception as e:
        error_message = ctk.CTkLabel(app, text=e, text_color="red")
        error_message.grid(row=3,column=0)