import customtkinter
import dashboard

# def open_create_modal():
modal = customtkinter.CTk()
modal.title('Create New Zone')
modal.geometry('400x500+0+0')

zone_error = None
station_error = None

def open_create_modal(add_new_row_callback):
    def create():
        global zone_error, station_error
        zone_entry_value = zone_entry.get().strip()  # Use .strip() to remove extra spaces
        stations_entry_value = stations_entry.get().strip()

        if zone_error:
            zone_error.destroy()
            zone_error = None
        if station_error:
            station_error.destroy()
            station_error = None
        
        if not zone_entry_value:
            zone_error = customtkinter.CTkLabel(frame, text='Zone is required!', text_color='red')
            zone_error.grid(row=1, column=0)
        if not stations_entry_value:
            station_error = customtkinter.CTkLabel(frame, text="At least one station is required!", text_color='red')
            station_error.grid(row=3, column=0)
        if zone_entry_value:
            for i, row in enumerate(dashboard.data):
                if row[1] == zone_entry_value and i != 0:
                    zone_error = customtkinter.CTkLabel(frame, text="Zone is already exit!", text_color='red')
                    zone_error.grid(row=1, column=0)
        
        # Ok
        new_data = [str(len(dashboard.data)), zone_entry_value, stations_entry_value, ""]
       
        cancel()

        add_new_row_callback(new_data)


    def cancel():
        modal.destroy()

    # Create a frame to hold input fields (optional but improves layout)
    frame = customtkinter.CTkFrame(modal)
    frame.pack(pady=20, padx=20, fill="both", expand=True)

    zone_entry = customtkinter.CTkEntry(frame, placeholder_text='Enter Zone')
    zone_entry.grid(row=0, column=0,sticky='we',padx=5,pady=10)

    stations_entry = customtkinter.CTkEntry(frame, placeholder_text='Enter Stations')
    stations_entry.grid(row=2, column=0,sticky='we',padx=5,pady=10)

    cancel_button = customtkinter.CTkButton(frame, text='Cancel', command=cancel, width=150)
    cancel_button.grid(row=5, column=0, sticky='ew')

    create_button = customtkinter.CTkButton(frame, text='Create', command=create, width=150)
    create_button.grid(row=5, column=1, sticky='ew')

    modal.mainloop()

        # try:
        #     if not zone_entry_value:
        #         ErrorMessage('Zone is empty!', 1)
        #     if not stations_entry_value:
        #         ErrorMessage("At least one station is required!", 3)
        #     if zone_entry_value:
        #         ErrorMessage('', 1)
        #         for i, row in enumerate(dashboard.data):
        #             if row[1] == zone_entry_value and i != 0:
        #                 ErrorMessage('Zone is already exit!', 1)

        #     # If no exception, print the values
        #     print(zone_entry_value)
        #     print(stations_entry_value)
        # except:
        #     print('Hello')