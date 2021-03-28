import tkinter as tk
from tkinter import *
import csv
import re as regex
import ast

class driver(tk.Frame):
    # Global vars
    Contacts = []
    contact_id_ct = 0
    Addresses = []
    address_id_ct = 0
    Phones = []
    phone_id_ct = 0

    ## Begin by loading data, if any
    # Contact data
    with open('./data/Contact.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            Contacts.append({
                'ID': int(row['ID']), # Primary Key
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'gender': row['gender'],
            })
        for x in Contacts:
            if x['ID'] > contact_id_ct:
                contact_id_ct = x['ID']

    # Address data
    with open('./data/Address.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            Addresses.append({
                'ID': int(row['ID']), # Foreign Key
                'aID': int(row['aID']), # Primary Key
                'address_1': row['address_1'],
                'address_2': row['address_2'],
                'apt': row['apt'],
                'city': row['city'],
                'state': row['state'],
                'country': row['country'],
            })
        for x in Addresses:
            if x['aID'] > address_id_ct:
                address_id_ct = x['aID']

    # Phone data
    with open('./data/Phone.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            Phones.append({
                'ID': int(row['ID']), # Foreign Key
                'pID': int(row['pID']), # Primary Key
                'type': row['type'],
                'number': row['number'],
            })
        for x in Phones:
            if x['pID'] > phone_id_ct:
                phone_id_ct = x['pID']

    # Init. GUI
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        fn = StringVar(value='')
        ln = StringVar(value='')
        gender = StringVar(value='')
        a1 = StringVar(value='')
        a2 = StringVar(value='')
        apt = StringVar(value='')
        city = StringVar(value='')
        state = StringVar(value='')
        country = StringVar(value='')
        phone_type = StringVar(value='')
        phone_number = StringVar(value='')

        # Display Contact.csv
        tk.Label(self, text="Contacts").grid(row = 0,column = 0)
        list_contacts = StringVar(value=self.Contacts)
        listbox_contacts = tk.Listbox(
            self,
            listvariable=list_contacts,
        )
        listbox_contacts.grid(row = 1, column = 0)

        # Delete Contact button
        self.delete_contact_btn = tk.Button(self)
        self.delete_contact_btn["text"] = "Delete selected Contact"
        self.delete_contact_btn["command"] = lambda: self.delete_contact(listbox_contacts.get(listbox_contacts.curselection()))
        self.delete_contact_btn.grid(row = 2, column = 0)

        # Display Address.csv
        tk.Label(self, text="Addresses").grid(row = 0,column = 1)
        list_addresses = StringVar(value=self.Addresses)
        listbox_addresses = tk.Listbox(
            self,
            listvariable=list_addresses,
        ).grid(row = 1, column = 1)

        # Display Phone.csv
        tk.Label(self, text="Phones").grid(row = 0,column = 2)
        list_addresses = StringVar(value=self.Addresses)
        listbox_addresses = tk.Listbox(
            self,
            listvariable=list_addresses,
        ).grid(row = 1, column = 2)

        CREATE_CONTACT_COL = 0
        CREATE_CONTACT_ROW = 3
        # Create Contact Labels
        tk.Label(self, text="Create Contact").grid(row = CREATE_CONTACT_ROW,column = CREATE_CONTACT_COL)
        fn_label = tk.Label(self ,text = "First Name").grid(row = CREATE_CONTACT_ROW+1,column = CREATE_CONTACT_COL)
        ln_label = tk.Label(self ,text = "Last Name").grid(row = CREATE_CONTACT_ROW+2,column = CREATE_CONTACT_COL)
        gender_label = tk.Label(self ,text = "Gender").grid(row = CREATE_CONTACT_ROW+3,column = CREATE_CONTACT_COL)
        a1_label = tk.Label(self ,text = "Address 1").grid(row = CREATE_CONTACT_ROW+4,column = CREATE_CONTACT_COL)
        a2_label = tk.Label(self ,text = "Address 2").grid(row = CREATE_CONTACT_ROW+5,column = CREATE_CONTACT_COL)
        apt_label = tk.Label(self ,text = "Apt #").grid(row = CREATE_CONTACT_ROW+6,column = CREATE_CONTACT_COL)
        city_label = tk.Label(self ,text = "City").grid(row = CREATE_CONTACT_ROW+7,column = CREATE_CONTACT_COL)
        state_label = tk.Label(self ,text = "State").grid(row = CREATE_CONTACT_ROW+8,column = CREATE_CONTACT_COL)
        country_label = tk.Label(self ,text = "Country").grid(row = CREATE_CONTACT_ROW+9,column = CREATE_CONTACT_COL)
        phone_type_label = tk.Label(self ,text = "Phone Type").grid(row = CREATE_CONTACT_ROW+10,column = CREATE_CONTACT_COL)
        phone_number_label = tk.Label(self ,text = "Phone Number").grid(row = CREATE_CONTACT_ROW+11,column = CREATE_CONTACT_COL)

        # Create Contact Entries
        fn_entry = tk.Entry(self, textvariable=fn).grid(row = CREATE_CONTACT_ROW+1,column = CREATE_CONTACT_COL+1)
        ln_entry = tk.Entry(self, textvariable=ln).grid(row = CREATE_CONTACT_ROW+2,column = CREATE_CONTACT_COL+1)
        gender_entry = tk.Entry(self, textvariable=gender).grid(row = CREATE_CONTACT_ROW+3,column = CREATE_CONTACT_COL+1)
        a1_entry = tk.Entry(self, textvariable=a1).grid(row = CREATE_CONTACT_ROW+4,column = CREATE_CONTACT_COL+1)
        a2_entry = tk.Entry(self, textvariable=a2).grid(row = CREATE_CONTACT_ROW+5,column = CREATE_CONTACT_COL+1)
        apt_entry = tk.Entry(self, textvariable=apt).grid(row = CREATE_CONTACT_ROW+6,column = CREATE_CONTACT_COL+1)
        city_entry = tk.Entry(self, textvariable=city).grid(row = CREATE_CONTACT_ROW+7,column = CREATE_CONTACT_COL+1)
        state_entry = tk.Entry(self, textvariable=state).grid(row = CREATE_CONTACT_ROW+8,column = CREATE_CONTACT_COL+1)
        country_entry = tk.Entry(self, textvariable=country).grid(row = CREATE_CONTACT_ROW+9,column = CREATE_CONTACT_COL+1)
        phone_type_entry = tk.Entry(self, textvariable=phone_type).grid(row = CREATE_CONTACT_ROW+10,column = CREATE_CONTACT_COL+1)
        phone_number_entry = tk.Entry(self, textvariable=phone_number).grid(row = CREATE_CONTACT_ROW+11,column = CREATE_CONTACT_COL+1)

        # Create Contact Submit button
        self.create_contact_btn = tk.Button(self)
        self.create_contact_btn["text"] = "Create Contact"
        self.create_contact_btn["command"] = lambda: self.create_contact(
            contact_entry = {
                'ID': self.contact_id_ct + 1,
                'first_name': fn.get(),
                'last_name': ln.get(),
                'gender': gender.get()
            },
            address_entry = {
                'ID': self.contact_id_ct + 1,
                'aID': self.address_id_ct + 1,
                'address_1': a1.get(),
                'address_2': a2.get(),
                'apt': apt.get(),
                'city': city.get(),
                'state': state.get(),
                'country': country.get()
            },
            phone_entry = {
                'ID': self.contact_id_ct + 1,
                'pID': self.address_id_ct + 1,
                'type': phone_type.get(),
                'number': phone_number.get()
            })
        self.create_contact_btn.grid(row = 15,column = CREATE_CONTACT_COL+1)

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)

        # Search Contact
        SEARCH_CONTACT_COLUMN = 2
        search_value = StringVar(value='')
        tk.Label(self, text="Select one key to search Contacts by:").grid(row = 2,column = SEARCH_CONTACT_COLUMN)
        search_entry = tk.Entry(self, textvariable=search_value)
        search_entry.grid(row = 5,column = SEARCH_CONTACT_COLUMN)
        # Display keys to search by
        search_keys = ['first_name', 'last_name', 'gender', 'address_1', 'address_2', 'apt', 'city', 'state', 'country', 'type', 'number']
        list_keys = StringVar(value=search_keys)
        listbox_keys = tk.Listbox(
            self,
            listvariable=list_keys,
        )
        listbox_keys.grid(row = 3, column = SEARCH_CONTACT_COLUMN)
        tk.Label(self, text="Enter value:").grid(row = 4,column = SEARCH_CONTACT_COLUMN)
        self.search_contact_btn = tk.Button(self)
        self.search_contact_btn["text"] = "Search"
        self.search_contact_btn["command"] = lambda: self.search_contact(listbox_keys.get(listbox_keys.curselection()), search_value.get())
        self.search_contact_btn.grid(row = 6, column = SEARCH_CONTACT_COLUMN)
        tk.Label(self, text="Search results:").grid(row = 7,column = SEARCH_CONTACT_COLUMN)
    # Data management methods
    def create_contact(self, contact_entry, address_entry, phone_entry):
        # Increment the id counters
        self.contact_id_ct += 1
        self.address_id_ct += 1
        self.phone_id_ct += 1

        self.Contacts.append(contact_entry)
        self.Addresses.append(address_entry)
        self.Phones.append(phone_entry)

        # Write to Contact.csv
        cfieldnames = ['ID', 'first_name', 'last_name', 'gender']
        with open('./data/Contact.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, cfieldnames)
            writer.writeheader()
            writer.writerows(self.Contacts)
        # Write to Address.csv
        afieldnames = ['ID', 'aID', 'address_1', 'address_2', 'apt', 'city', 'state', 'country']
        with open('./data/Address.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, afieldnames)
            writer.writeheader()
            writer.writerows(self.Addresses)
        # Write to Phone.csv
        pfieldnames = ['ID', 'pID', 'type', 'number']
        with open('./data/Phone.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, pfieldnames)
            writer.writeheader()
            writer.writerows(self.Phones)

        self.reload_UI()

    def reload_UI(self):
        # Reload UI
        # Display Contact.csv
        tk.Label(self, text="Contacts").grid(row = 0,column = 0)
        list_contacts = StringVar(value=self.Contacts)
        listbox_contacts = tk.Listbox(
            self,
            listvariable=list_contacts
        ).grid(row = 1, column = 0)

        # Display Address.csv
        tk.Label(self, text="Addresses").grid(row = 0,column = 1)
        list_addresses = StringVar(value=self.Addresses)
        listbox_addresses = tk.Listbox(
            self,
            listvariable=list_addresses
        ).grid(row = 1, column = 1)

        # Display Phone.csv
        tk.Label(self, text="Phones").grid(row = 0,column = 2)
        list_addresses = StringVar(value=self.Addresses)
        listbox_addresses = tk.Listbox(
            self,
            listvariable=list_addresses
        ).grid(row = 1, column = 2)

    def edit_contact(self):
        print("hi there, edit!")

    def search_contact(self, key, value):
        cfieldnames = ['first_name', 'last_name', 'gender']
        afieldnames = ['address_1', 'address_2', 'apt', 'city', 'state', 'country']
        pfieldnames = ['type', 'number']

        list_to_search = []
        search_keys = []
        for x in cfieldnames:
            if x == key:
                list_to_search = self.Contacts
                idx = 0
                for dictionary in list_to_search:
                    if dictionary[key] == value:
                        search_keys.append(self.Contacts[idx])
                        idx += 1
                    else:
                        idx += 1
        for y in afieldnames:
            if y == key:
                list_to_search = self.Addresses
                idx = 0
                for dictionary in list_to_search:
                    if dictionary[key] == value:
                        search_keys.append(self.Addresses[idx])
                        idx += 1
                    else:
                        idx += 1
        for z in pfieldnames:
            if z == key:
                list_to_search = self.Phones
                idx = 0
                for dictionary in list_to_search:
                    if dictionary[key] == value:
                        search_keys.append(self.Phones[idx])
                        idx += 1
                    else:
                        idx += 1

        list_results = StringVar(value=search_keys)
        listbox_results = tk.Listbox(
            self,
            listvariable=list_results,
        )
        listbox_results.grid(row = 8, column = 2)
    def delete_contact(self, selected_contact):
        to_delete = ast.literal_eval(selected_contact)
        for dictionary in self.Contacts:
            if dictionary['ID'] == to_delete['ID']:
                self.Contacts.remove(dictionary)
        for dictionary in self.Addresses:
            if dictionary['ID'] == to_delete['ID']:
                self.Addresses.remove(dictionary)
        for dictionary in self.Phones:
            if dictionary['ID'] == to_delete['ID']:
                self.Phones.remove(dictionary)
        # Write to Contact.csv
        cfieldnames = ['ID', 'first_name', 'last_name', 'gender']
        with open('./data/Contact.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, cfieldnames)
            writer.writeheader()
            writer.writerows(self.Contacts)
        # Write to Address.csv
        afieldnames = ['ID', 'aID', 'address_1', 'address_2', 'apt', 'city', 'state', 'country']
        with open('./data/Address.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, afieldnames)
            writer.writeheader()
            writer.writerows(self.Addresses)
        # Write to Phone.csv
        pfieldnames = ['ID', 'pID', 'type', 'number']
        with open('./data/Phone.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, pfieldnames)
            writer.writeheader()
            writer.writerows(self.Phones)
        self.reload_UI()

#print(list(pycountry.countries))
#print(list(pycountry.subdivisions))
root = tk.Tk()
root.title('COMP440 - Basic Data Management App - Kyle Chan')

root.geometry('1000x1000')
root.config(bg='#131921')

app = driver(master=root)
app.mainloop()
