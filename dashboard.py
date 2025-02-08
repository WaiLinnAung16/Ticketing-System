import customtkinter
import create_modal

data = [["ID", "Zone", "Stations", "Action"],
        ["1", "Central Zone", "Station one, Station Two", ""],
        ["2", "Central Zone 1", "Station one 1, Station Two 1", ""]]

def handle_action(value, i):
    print(value, i)

def add_new_row(table_frame, new_row):
    """Dynamically adds a new row to the table without refreshing."""
    i = len(data) - 1  # Get the index of the new row
    data.append(new_row)
    print(data)
    for j, col in enumerate(new_row):
        cell_frame = customtkinter.CTkFrame(table_frame, border_width=1, fg_color="#f3f3f3")
        cell_frame.grid(row=i, column=j, padx=1, pady=1, sticky="nsew")

        if j == len(new_row) - 1:
            action_btn_group = customtkinter.CTkSegmentedButton(
                cell_frame, values=['View', 'Edit', 'Delete'],
                command=lambda value, row_id=new_row[0]: handle_action(value, row_id),
                selected_color='white', fg_color='white'
            )
            action_btn_group.pack(expand=True, fill='both')
        else:
            label = customtkinter.CTkLabel(cell_frame, text=col, font=("Arial", 12), width=100, height=30, text_color='black')
            label.pack(expand=True, fill="both")

def open_main_window(screen_w, screen_h):
    main_app = customtkinter.CTk()
    main_app.title("Centrala Ticketing System")
    main_app.geometry(f'{screen_w}x{screen_h}+0+0')

    welcome_label = customtkinter.CTkLabel(main_app, text="Welcome to the Centrala Ticketing System!", font=("Arial", 20))
    welcome_label.place(relx=0.5, rely=0.05, anchor="center")

    logout_button = customtkinter.CTkButton(main_app, text="Logout", command=main_app.destroy, width=150, fg_color='red')
    logout_button.place(relx=0.15, rely=0.08)

    tabview = customtkinter.CTkTabview(master=main_app, width=1080, height=600)
    tabview.place(relx=0.5, rely=0.5, anchor='center')

    tabview.add("Board")
    tabview.add("Ticket")
    tabview.set("Board")

    table_frame = customtkinter.CTkFrame(master=tabview.tab("Board"), width=600)
    table_frame.pack(pady=20)

    for i, row in enumerate(data):
        for j, col in enumerate(row):
            cell_frame = customtkinter.CTkFrame(table_frame, border_width=1, fg_color="#f3f3f3")
            cell_frame.grid(row=i, column=j, padx=1, pady=1, sticky="nsew")

            if j == len(row) - 1 and i != 0:
                action_btn_group = customtkinter.CTkSegmentedButton(
                    cell_frame, values=['View', 'Edit', 'Delete'],
                    command=lambda value, row_id=row[0]: handle_action(value, row_id),
                    selected_color='white', fg_color='white'
                )
                action_btn_group.pack(expand=True, fill='both')
            else:
                label = customtkinter.CTkLabel(cell_frame, text=col, font=("Arial", 12), width=100, height=30, text_color='black')
                label.pack(expand=True, fill="both")

    button = customtkinter.CTkButton(
        master=tabview.tab("Board"), text='Create New Zone',
        command=lambda: create_modal.open_create_modal(lambda new_row: add_new_row(table_frame, new_row))
    )
    button.pack(padx=20, pady=20)

    main_app.mainloop()
