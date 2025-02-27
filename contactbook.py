class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def addcontact(self):
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        print("Contact added successfully.")

    def viewcontacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. Name: {contact.name}, Phone: {contact.phone}")

    def searchcontact(self):
        search_term = input("Enter name or phone number to search: ")
        found_contacts = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        if found_contacts:
            for contact in found_contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")
        else:
            print("No matching contacts found.")

    def updatecontact(self):
        self.viewcontacts()
        if self.contacts:
            contact_number = int(input("Enter the contact number to update: ")) - 1
            if 0 <= contact_number < len(self.contacts):
                contact = self.contacts[contact_number]
                print(f"Current details - Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")
                contact.name = input("Enter new name: ")
                contact.phone = input("Enter new phone number: ")
                contact.email = input("Enter new email: ")
                contact.address = input("Enter new address: ")
                print("Contact updated successfully.")
            else:
                print("Invalid contact number.")

    def deletecontact(self):
        self.viewcontacts()
        if self.contacts:
            contact_number = int(input("Enter the contact number to delete: ")) - 1
            if 0 <= contact_number < len(self.contacts):
                deleted_contact = self.contacts.pop(contact_number)
                print(f"Contact '{deleted_contact.name}' deleted successfully.")
            else:
                print("Invalid contact number.")

def main():
    contact_book = ContactBook()
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            contact_book.addcontact()
        elif choice == "2":
            contact_book.viewcontacts()
        elif choice == "3":
            contact_book.searchcontact()
        elif choice == "4":
            contact_book.updatecontact()
        elif choice == "5":
            contact_book.deletecontact()
        elif choice == "6":
            print("Exiting the Contact Book.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()