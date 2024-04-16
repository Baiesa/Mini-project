'''
Project Requirements

Your task is to develop a Contact Management System with the following features:

User Interface (UI):
Create a user-friendly command-line interface (CLI) for the Contact Management System.
Display a welcoming message and provide a menu with the following options: <div class='oc-markdown-custom-container oc-markdown-activatable' contenteditable='false' data-value='```
Welcome to the Contact Management System! Menu:
Add a new contact
Edit an existing contact
Delete a contact
Search for a contact
Display all contacts
Export contacts to a text file
Import contacts from a text file
Quit
'>
Welcome to the Contact Management System!
Menu:
Add a new contact
Edit an existing contact
Delete a contact
Search for a contact
Display all contacts
Export contacts to a text file
Import contacts from a text file
Quit
```
Contact Data Storage:
Use nested dictionaries as the main data structure for storing contact information.
Each contact should have a unique identifier (e.g., a phone number or email address) as the outer dictionary key.
Store contact details within the inner dictionary, including:
Name
Phone number
Email address
Additional information (e.g., address, notes).
Menu Actions:
Implement the following actions in response to menu selections:
Adding a new contact with all relevant details.
Editing an existing contact's information (name, phone number, email, etc.).
Deleting a contact by searching for their unique identifier.
Searching for a contact by their unique identifier and displaying their details.
Displaying a list of all contacts with their unique identifiers.
Exporting contacts to a text file in a structured format.
Importing contacts from a text file and adding them to the system.
User Interaction:
Utilize input() to enable users to select menu options and provide contact details.
Implement input validation using regular expressions (regex) to ensure correct formatting of contact information.
Error Handling:
Apply error handling using try, except, else, and finally blocks to manage unexpected issues that may arise during execution.
'''










import re
import json

contacts = {}

def display_menu():
    print("\nWelcome to the Contact Management System!")
    print("Menu:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file")
    print("8. Quit")

def add_contact():
    print("\nAdd a New Contact:")
    unique_id = input("Enter unique identifier (e.g., phone number or email address): ")
    if unique_id in contacts:
        print("Contact already exists.")
        return
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email address: ")
    additional_info = input("Enter additional information: ")
    contacts[unique_id] = {'Name': name, 'Phone Number': phone_number, 'Email': email, 'Additional Info': additional_info}
    print("Contact added successfully.")

def edit_contact():
    print("\nEdit an Existing Contact:")
    unique_id = input("Enter unique identifier of the contact to edit: ")
    if unique_id not in contacts:
        print("Contact not found.")
        return
    print("Current details:")
    print_contact(unique_id)
    name = input("Enter new name (leave blank to keep current): ")
    phone_number = input("Enter new phone number (leave blank to keep current): ")
    email = input("Enter new email address (leave blank to keep current): ")
    additional_info = input("Enter new additional information (leave blank to keep current): ")
    if name:
        contacts[unique_id]['Name'] = name
    if phone_number:
        contacts[unique_id]['Phone Number'] = phone_number
    if email:
        contacts[unique_id]['Email'] = email
    if additional_info:
        contacts[unique_id]['Additional Info'] = additional_info
    print("Contact updated successfully.")

def delete_contact():
    print("\nDelete a Contact:")
    unique_id = input("Enter unique identifier of the contact to delete: ")
    if unique_id not in contacts:
        print("Contact not found.")
        return
    del contacts[unique_id]
    print("Contact deleted successfully.")

def search_contact():
    print("\nSearch for a Contact:")
    unique_id = input("Enter unique identifier of the contact to search for: ")
    if unique_id not in contacts:
        print("Contact not found.")
        return
    print_contact(unique_id)

def display_all_contacts():
    print("\nAll Contacts:")
    if not contacts:
        print("No contacts found.")
        return
    for unique_id in contacts:
        print_contact(unique_id)

def export_contacts():
    print("\nExport Contacts:")
    filename = input("Enter the filename to save contacts (e.g., contacts.txt): ")
    try:
        with open(filename, 'w') as file:
            json.dump(contacts, file, indent=4)
        print("Contacts exported successfully.")
    except Exception as e:
        print("Error exporting contacts:", e)

def import_contacts():
    print("\nImport Contacts:")
    filename = input("Enter the filename to import contacts from: ")
    try:
        with open(filename, 'r') as file:
            imported_contacts = json.load(file)
            contacts.update(imported_contacts)
        print("Contacts imported successfully.")
    except FileNotFoundError:
        print("File not found:", filename)
    except Exception as e:
        print("Error importing contacts:", e)

def print_contact(unique_id):
    print(f"Identifier: {unique_id}")
    for key, value in contacts[unique_id].items():
        print(f"{key}: {value}")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            edit_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            search_contact()
        elif choice == '5':
            display_all_contacts()
        elif choice == '6':
            export_contacts()
        elif choice == '7':
            import_contacts()
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")

if __name__ == "__main__":
    main()