contacts=()
def add_contact(name, phone, email):
    contact = f"{name} - {phone} - {email}"
    contacts.append(contact)

def view_contacts():
    print("\nAll Contacts:")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact}")
    print()

def search_contact(keyword):
    for contact in contacts:
        if keyword.lower() in contact.lower():
            print("Found Contact:")
            print(contact)
            return
    print("Contact not found.")

def delete_contact(keyword):
    for contact in contacts:
        if keyword.lower() in contact.lower():
            contacts.remove(contact)
            print("Contact deleted:", contact)
            return
    print("Contact not found.")