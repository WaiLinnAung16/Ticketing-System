import customtkinter as ctk
import datetime

data = [["ID", "Zone", "Stations", "Action"],
        ["1", "Central Zone", "Rede,Ninia,Fresin,Bylyn,Jaund",""],
        ["2", "Midtown Zone", "Wicyt,Riladia,Sylas,Garicn, Ralth", ""],
        ["3","Downtown Zone","Erean,Brunad,Zord,Perinad,Keivia",""]
        ]

modal_screen_size = '400x500+700+200'

def handle_action(value, id):
    """
    Handles actions for View, Edit, and Delete buttons.

    Parameters:
        value (str): The type of action ('View', 'Edit', 'Delete').
        id (int): The index of the item in the dataset.

    Actions:
        - 'View': Opens a detail modal displaying zone and station information.
        - 'Edit': Opens an edit modal for modifying zone and station details.
        - 'Delete': Removes the item from the dataset and refreshes the main application window.
    """
    if value == 'View':
        open_detail_modal(data[id])
        return 
    elif value == 'Edit':
        open_edit_modal(data[id], id)
        return
    elif value == 'Delete':
        # TODO: Add Delete Confirmation Modal
        data.pop(id)  # Remove item from dataset
        main_app.destroy()  # Close the main app window
        open_main_window('1080', '600')  # Refresh the main window
        return

def open_detail_modal(detail):
    """
    Displays detailed information for a selected zone and its stations.

    Parameters:
        detail (list): A list containing [ID, Zone Name, Stations, Additional Info].

    Functionality:
        - Shows the Zone Name and associated Stations.
        - Provides a Back button to return to the main window.
    """
    detail_modal = ctk.CTk()  # Create a new modal window
    detail_modal.title('Detail')
    detail_modal.geometry(modal_screen_size)

    def back():
        """
        Closes the detail modal and reopens the main application window.
        """
        detail_modal.destroy()
        main_app.destroy()
        open_main_window('1080', '600')

    # Zone Title Label
    zone_title = ctk.CTkLabel(detail_modal, text='Zone Name', font=('Arial', 20, 'bold'))
    zone_title.grid(row=0, column=0, sticky='w', padx=10, pady=(10, 2))

    # Zone Name Label
    zone_name = ctk.CTkLabel(detail_modal, text=detail[1])
    zone_name.grid(row=1, column=0, sticky='w', padx=10, pady=(0, 10))

    # Station Title Label
    station_title = ctk.CTkLabel(detail_modal, text='Stations Name', font=('Arial', 20, 'bold'))
    station_title.grid(row=2, column=0, sticky='w', padx=10, pady=(10, 2))

    # Station Names Label
    station_name = ctk.CTkLabel(detail_modal, text=detail[2])
    station_name.grid(row=3, column=0, sticky='w', padx=10, pady=(0, 10))

    # Back Button
    back_button = ctk.CTkButton(detail_modal, text='Back', command=back, width=150)
    back_button.grid(row=4, column=0, sticky='w', padx=10, pady=(10, 10))

    detail_modal.mainloop()  # Run the modal event loop

def open_edit_modal(edit_data, index):
    """
    Opens an Edit Modal for modifying a Zone and its associated Stations.
    
    Parameters:
        edit_data (list): The data of the selected row containing [ID, Zone Name, Stations, Actions].
        index (int): The index of the selected row in the dataset.

    Functionality:
        - Allows editing the Zone name and associated Stations.
        - Validates that the Zone name is unique and that at least one station is provided.
        - Updates the dataset and refreshes the main application window.
    """
    edit_modal = ctk.CTk()  # Create a new modal window
    edit_modal.title('Edit Zone and Stations')
    edit_modal.geometry(modal_screen_size)

    def edit():
        """
        Handles validation and updating of Zone and Station data.

        Validation:
            - Ensures the Zone name is not empty.
            - Ensures at least one station is provided.
            - Checks for duplicate Zone names in the dataset.

        Actions:
            - If validation passes, updates the dataset with the new values.
            - Refreshes the main application window after saving changes.
        """
        zone_error = None
        station_error = None
        edit_zone_value = zone_entry.get().strip()
        edit_station_value = stations_entry.get().strip()

        # Clear previous error messages if they exist
        if zone_error:
            zone_error.destroy()
            zone_error = None
        if station_error:
            station_error.destroy()
            station_error = None

        # Validation checks
        if not edit_zone_value:
            zone_error = ctk.CTkLabel(frame, text='Zone is required!', text_color='red')
            zone_error.grid(row=1, column=0)
        if not edit_station_value:
            station_error = ctk.CTkLabel(frame, text="At least one station is required!", text_color='red')
            station_error.grid(row=3, column=0)
            return
        
        # Check for duplicate Zone name in dataset
        if edit_zone_value:
            data.pop(index)  # Temporarily remove the current item for comparison
            for i, row in enumerate(data):
                if row[1] == edit_zone_value and i != 0:
                    zone_error = ctk.CTkLabel(frame, text="Zone already exists!", text_color='red')
                    zone_error.grid(row=1, column=0)
                    return  # Stop execution if duplicate found

        # If no validation errors, update dataset and refresh the UI
        if not zone_error:
            new_data = [edit_data[0], edit_zone_value, edit_station_value, ""]
            data.append(new_data)  # Add updated data

            edit_modal.destroy()  # Close the edit modal
            main_app.destroy()  # Close the main application window
            open_main_window('1080', '600')  # Reopen the main window to reflect changes

    def cancel():
        """
        Closes the Edit Modal and refreshes the main application window without making changes.
        """
        edit_modal.destroy()
        main_app.destroy()
        open_main_window('1080', '600')

    # Create a frame to hold input fields
    frame = ctk.CTkFrame(edit_modal)
    frame.pack(pady=20, padx=20, fill="both", expand=True)

    # Zone input field
    zone_entry = ctk.CTkEntry(frame, placeholder_text='Enter Zone')
    zone_entry.insert(0, edit_data[1])  # Prefill with existing value
    zone_entry.grid(row=0, column=0, sticky='we', padx=5, pady=10)

    # Stations input field
    stations_entry = ctk.CTkEntry(frame, placeholder_text='Enter Stations')
    stations_entry.insert(0, edit_data[2])  # Prefill with existing value
    stations_entry.grid(row=2, column=0, sticky='we', padx=5, pady=10)

    # Cancel button
    cancel_button = ctk.CTkButton(frame, text='Cancel', command=cancel, width=150)
    cancel_button.grid(row=5, column=0, sticky='ew')

    # Edit button
    edit_button = ctk.CTkButton(frame, text='Edit', command=edit, width=150)
    edit_button.grid(row=5, column=1, sticky='ew')

    edit_modal.mainloop()  # Run the modal event loop

def open_create_modal():
    """
    Opens a modal window to create a new zone with station details.
    Provides input validation and checks for duplicate zone names.
    """
    modal = ctk.CTk()
    modal.title('Create New Zone')
    modal.geometry(modal_screen_size)

    # Frame for UI Layout
    frame = ctk.CTkFrame(modal)
    frame.pack(pady=20, padx=20, fill="both", expand=True)

    # Zone Name Entry
    zone_label = ctk.CTkLabel(frame, text="Zone Name:")
    zone_label.grid(row=0, column=0, sticky='w', padx=5, pady=(5, 2))

    zone_entry = ctk.CTkEntry(frame, placeholder_text='Enter Zone', width=200)
    zone_entry.grid(row=1, column=0,  sticky='w', pady=(5, 2))

    # Station Names Entry
    station_label = ctk.CTkLabel(frame, text="Stations:")
    station_label.grid(row=3, column=0, sticky='w', padx=5, pady=(5, 2))

    stations_entry = ctk.CTkEntry(frame, placeholder_text='Enter Stations', width=200)
    stations_entry.grid(row=4, column=0, sticky='w', pady=(5, 2))

    # Error Message Labels (Initially Empty)
    zone_error_label = ctk.CTkLabel(frame, text="", text_color="red")
    zone_error_label.grid(row=2, column=0, padx=5, pady=(5, 2))

    station_error_label = ctk.CTkLabel(frame, text="", text_color="red")
    station_error_label.grid(row=5, column=0, padx=5, pady=(5, 2))

    def create():
        """
        Handles creation logic, including validation and duplication checks.
        If validation passes, the new data is added to the main data list and
        the modal is closed.
        """
        zone_entry_value = zone_entry.get().strip()  # Remove leading/trailing spaces
        stations_entry_value = stations_entry.get().strip()

        # Reset previous error messages
        zone_error_label.configure(text="")
        station_error_label.configure(text="")

        has_error = False  # Flag to track errors

        # Validation Checks
        if not zone_entry_value:
            zone_error_label.configure(text="Zone is required!")
            has_error = True

        if not stations_entry_value:
            station_error_label.configure(text="At least one station is required!")
            has_error = True

        # Check for Duplicate Zone Name
        if any(row[1] == zone_entry_value for row in data):  # Check if zone already exists
            zone_error_label.configure(text="Zone already exists!")
            has_error = True

        # Stop execution if validation failed
        if has_error:
            return  

        # Add New Zone to Data List
        new_data = [str(len(data)), zone_entry_value, stations_entry_value, ""]
        data.append(new_data)

        # Close the modal and refresh the main window
        modal.destroy()
        main_app.destroy()
        open_main_window('1080', '600')

    def cancel():
        """
        Closes the modal window without saving changes.
        """
        modal.destroy()

    # Button Section
    button_frame = ctk.CTkFrame(frame)
    button_frame.grid(row=6, column=0, columnspan=2, pady=10)

    cancel_button = ctk.CTkButton(button_frame, text='Cancel', command=cancel, width=150)
    cancel_button.pack(side="left", padx=5)

    create_button = ctk.CTkButton(button_frame, text='Create', command=create, width=150)
    create_button.pack(side="left", padx=5)

    # Run the modal
    modal.mainloop()

def open_main_window(screen_w, screen_h):
    global main_app
    main_app = ctk.CTk()
    main_app.title("Centrala Ticketing System")
    main_app.geometry(f'{screen_w}x{screen_h}+300+100')

    welcome_label = ctk.CTkLabel(main_app, text="Welcome to the Centrala Ticketing System!", font=("Arial", 20))
    welcome_label.place(relx=0.5,rely=0.1, anchor='center')

    logout_button = ctk.CTkButton(main_app, text="Logout", command=main_app.destroy, width=150, fg_color='red')
    logout_button.grid(row=1, column=0, padx=20, pady=20, sticky="w")

    tabview = ctk.CTkTabview(master=main_app, width=1080, height=300)
    tabview.place(relx=0.5, rely=0.5, anchor='center')

    tabview.add("Board")
    tabview.add("Ticket")
    tabview.set("Board")

    table_frame = ctk.CTkFrame(master=tabview.tab("Board"), width=600)
    table_frame.pack(pady=20)

    # Sort Data with id
    header, *rows = data
    sorted_rows = sorted(rows, key=lambda x: int(x[0]))  # Sort by ID
    sorted_data = [header] + sorted_rows 

    for i, row in enumerate(sorted_data):
        for j, col in enumerate(row):
            cell_frame = ctk.CTkFrame(table_frame, border_width=1, fg_color="#f3f3f3")
            cell_frame.grid(row=i, column=j, padx=1, pady=1, sticky="nsew")

            if j == len(row) - 1 and i != 0:
                global action_btn_group
                action_btn_group = ctk.CTkSegmentedButton(
                    cell_frame, values=['View', 'Edit', 'Delete'],
                    command=lambda value, row_id=i: handle_action(value, row_id),
                    selected_color='white', fg_color='white'
                )
                action_btn_group.pack(expand=True, fill='both')
               
            else:
                label = ctk.CTkLabel(cell_frame, text=col, font=("Arial", 12), width=100, height=30, text_color='black')
                label.pack(expand=True, fill="both")

    button = ctk.CTkButton(
        master=tabview.tab("Board"), text='Create New Zone',
        command=open_create_modal
    )
    button.pack(padx=20, pady=20)

    class Voucher:
        ADULT_FARE = 2105
        CHILD_FARE = 1410
        SENIOR_FARE = 1025
        STUDENT_FARE = 1750
        EURO_CURRENCY = 100

        def __init__(self, adults, children, seniors, students,b_zone, d_zone,zones):
            self.adults = adults
            self.children = children
            self.seniors = seniors
            self.students = students
            self.boarding_zone = b_zone
            self.destination_zone = d_zone

            self.zones_traveled = abs(zones.index(d_zone) - zones.index(b_zone)) + 1
            self.total_adults_fare = adults * self.ADULT_FARE * self.zones_traveled
            self.total_children_fare = children * self.CHILD_FARE * self.zones_traveled
            self.total_seniors_fare = seniors * self.SENIOR_FARE * self.zones_traveled
            self.total_students_fare = students * self.STUDENT_FARE * self.zones_traveled
            self.total = (self.total_adults_fare + self.total_children_fare + self.total_seniors_fare + self.total_students_fare) / self.EURO_CURRENCY
            self.euro = int(self.total)
            self.cents = round((self.total - self.euro) * self.EURO_CURRENCY)
            self.total_travellers = adults + children + seniors + students

            self.fares = [
                ('Adults', self.adults, self.ADULT_FARE, self.total_adults_fare,self.zones_traveled),
                ('Children', self.children, self.CHILD_FARE, self.total_children_fare,self.zones_traveled),
                ('Seniors', self.seniors, self.SENIOR_FARE, self.total_seniors_fare,self.zones_traveled),
                ('Students', self.students, self.STUDENT_FARE, self.total_students_fare,self.zones_traveled),
            ]
            
        def generate_voucher(self):
            voucher = ctk.CTk()
            voucher.title('Voucher')
            voucher.geometry('500x500+300+100')

            def close_program():
                voucher.destroy()
                main_app.destroy()

            date_time = datetime.datetime.now()
            day = date_time.strftime('%d')
            month = date_time.strftime('%b')
            year = date_time.strftime('%Y')
            date = f'{day} {month} {year}'
            time = f'{date_time.strftime('%I')}:{date_time.strftime('%M')} {date_time.strftime('%p')}'

            frame = ctk.CTkFrame(voucher)
            frame.pack(expand=True, fill="both", padx=10, pady=10)

            title_label = ctk.CTkLabel(frame, text="Centrala's Train Voucher", font=("Arial", 16, "bold"))
            title_label.grid(row=0, column=1, pady=10)

            ctk.CTkLabel(frame, text=f"{date} {time}", font=("Arial", 12)).grid(row=1,column=2,pady=10,sticky='e')

            ctk.CTkLabel(frame, text="Boarding Zone", font=("Arial", 12, "bold")).grid(row=2, column=0, sticky="w")
            ctk.CTkLabel(frame, text="Destination Zone", font=("Arial", 12, "bold")).grid(row=2, column=2, sticky="e")

            ctk.CTkLabel(frame, text=f"{self.boarding_zone}").grid(row=3, column=0, sticky="w")
            ctk.CTkLabel(frame, text=f"{self.destination_zone}").grid(row=3, column=2, sticky="e")

            ctk.CTkLabel(frame, text="No of Travelled Zone:",font=('Arial',12,'bold')).grid(row=4, column=0, pady=5,sticky='w')
            ctk.CTkLabel(frame, text=self.zones_traveled).grid(row=4,column=2,pady=5,sticky='e')
            
            row_index = 5
            for label, no_of_people, fare, total_fare,zones_travelled in self.fares:
                if total_fare > 0:
                    ctk.CTkLabel(frame, text=label,font=('Arial',12,'bold')).grid(row=row_index, column=0, sticky="w")
                    ctk.CTkLabel(frame, text=f"{no_of_people} x ({fare} x {zones_travelled}) = {total_fare}").grid(row=row_index, column=2, sticky='e')
                    row_index += 1
            
            ctk.CTkLabel(frame, text=f"Total Travellers: {self.total_travellers}", font=("Arial",12, "bold")).grid(row=row_index, column=0, pady=10, sticky="w")
            ctk.CTkLabel(frame, text=f"Total Fare: {self.euro} euro {self.cents} cents", font=("Arial",12, "bold")).grid(row=row_index, column=2, pady=10, sticky="e")

            exit_button = ctk.CTkButton(frame, text="Exit", fg_color="red", command=close_program)
            exit_button.grid(row=row_index + 1, column=1, padx=10, sticky='e')

            create_button = ctk.CTkButton(frame, text="Create Another One", fg_color="blue", command=voucher.destroy)
            create_button.grid(row=row_index + 1, column=2, sticky='e')

            voucher.mainloop()

            
    def createTicket():
        validation_error = None
        boarding_zone = boarding_zone_select.get()
        destination_zone = destination_zone_select.get()
        no_adults = adults_entry.get().strip()
        no_child = child_entry.get().strip()
        no_senior = senior_entry.get().strip()
        no_students = students_entry.get().strip()

        if validation_error:
            validation_error.destroy()
            validation_error = None

        # Check for empty fields
        if not no_adults and not no_child and not no_senior and not no_students:
            validation_error = ctk.CTkLabel(master=tabview.tab('Ticket'), text='At least one person is required!', text_color='red')
            validation_error.pack()
            return

        try:
            no_adults = int(no_adults)
            no_child = int(no_child)
            no_senior = int(no_senior)
            no_students = int(no_students)
            # Check if at least one person is entered 
            if no_adults == 0 and no_child == 0 and no_senior == 0 and no_students == 0:
                raise Exception('At least one person is required to create voucher!')
        except ValueError:
            # Handle invalid integer input
            validation_error = ctk.CTkLabel(master=tabview.tab('Ticket'), text='Please enter valid integers (or 0) for all inputs.', text_color='red')
            validation_error.pack()
            return
        except Exception as err:
            # Handle general exceptions (like no people being entered)
            validation_error = ctk.CTkLabel(master=tabview.tab('Ticket'), text=err, text_color='red')
            validation_error.pack()
        finally:
            # Proceed to create the voucher only if no exceptions were raised
            voucher_data = Voucher(no_adults,no_child,no_senior,no_students,boarding_zone,destination_zone,zones)
            voucher_data.generate_voucher()
    
    header, *rows = sorted_data
    zones = [row[1] for row in rows]

    # Ticket Section
    create_ticket_title = ctk.CTkLabel(master=tabview.tab('Ticket'), text='Create Ticket', font=('Arial', 20, 'bold'))
    create_ticket_title.pack(padx=20, pady=20)

    boarding_zone_select = ctk.CTkOptionMenu(master=tabview.tab('Ticket'), values=zones,width=300)
    boarding_zone_select.pack(padx=20,pady=10)

    destination_zone_select = ctk.CTkOptionMenu(master=tabview.tab('Ticket'), values=zones,width=300)
    destination_zone_select.pack(padx=20,pady=10)

    adults_entry = ctk.CTkEntry(master=tabview.tab('Ticket'),width=300,placeholder_text='Enter No of adults')
    adults_entry.insert(0, 0)
    adults_entry.pack(padx=20,pady=10)

    child_entry = ctk.CTkEntry(master=tabview.tab('Ticket'),width=300,placeholder_text='Enter No of child')
    child_entry.insert(0, 0)
    child_entry.pack(padx=20,pady=10)

    senior_entry = ctk.CTkEntry(master=tabview.tab('Ticket'),width=300,placeholder_text='Enter No of senior')
    senior_entry.insert(0, 0)
    senior_entry.pack(padx=20,pady=10)

    students_entry = ctk.CTkEntry(master=tabview.tab('Ticket'),width=300,placeholder_text='Enter No of students')
    students_entry.insert(0, 0)
    students_entry.pack(padx=20,pady=10)

    create_ticket = ctk.CTkButton(master=tabview.tab('Ticket'),width=150, text='Create Ticket', command=createTicket)
    create_ticket.pack(padx=20,pady=20)

    main_app.mainloop()