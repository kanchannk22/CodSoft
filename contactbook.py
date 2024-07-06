import os

# File to store contacts
CONTACTS_FILE = 'contacts.txt'

# Function to load contacts from file into a list of dictionaries
def load_contacts():
    contacts = []
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as f:
            for line in f:
                name, phone, email = line.strip().split(',')
                contacts.append({'name': name, 'phone': phone, 'email': email})
    return contacts

# Function to save contacts from a list of dictionaries into the file
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as f:
        for contact in contacts:
            f.write(f"{contact['name']},{contact['phone']},{contact['email']}\n")

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email: ")
    contacts.append({'name': name, 'phone': phone, 'email': email})
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully!")

# Function to view all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("Contacts:")
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

# Function to search for a contact by name
def search_contact(contacts):
    name = input("Enter the name to search: ")
    found = False
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            found = True
    if not found:
        print(f"Contact with name '{name}' not found.")

# Function to delete a contact by name
def delete_contact(contacts):
    name = input("Enter the name to delete: ")
    found = False
    for contact in contacts[:]:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)
            found = True
    if found:
        save_contacts(contacts)
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact with name '{name}' not found.")

# Function to update contact details
def update_contact(contacts):
    name = input("Enter the name to update: ")
    found = False
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print("Enter new details (leave blank to keep unchanged):")
            new_name = input(f"New name ({contact['name']}): ").strip()
            new_phone = input(f"New phone ({contact['phone']}): ").strip()
            new_email = input(f"New email ({contact['email']}): ").strip()
            if new_name:
                contact['name'] = new_name
            if new_phone:
                contact['phone'] = new_phone
            if new_email:
                contact['email'] = new_email
            found = True
            save_contacts(contacts)
            print(f"Contact '{name}' updated successfully.")
            break
    if not found:
        print(f"Contact with name '{name}' not found.")

# Main function to run the contact book
def main():
    contacts = load_contacts()
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Update Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            update_contact(contacts)
        elif choice == '6':
            print("Exiting program. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == '__main__':
    main()
