class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)

    def view_contact_list(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}")

    def search_contact(self, query):
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query.lower() in contact.phone.lower():
                print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")

    def update_contact(self, name, phone, email, address):
        for contact in self.contacts:
            if contact.name == name:
                contact.phone = phone
                contact.email = email
                contact.address = address
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                return
        print("Contact not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\n1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            email = input("Enter contact email: ")
            address = input("Enter contact address: ")
            contact_book.add_contact(name, phone, email, address)
