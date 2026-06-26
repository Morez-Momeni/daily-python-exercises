from pprint import pprint
import re

class Contact:
    def __init__(self, id, name, last_name, email, phone_number):
        self.id = id
        self.name = name.strip()
        self.last_name = last_name.strip()
        self.email = email.strip()
        self.phone_number = phone_number.strip()

    def __repr__(self):
        return f"Contact(id={self.id}, name='{self.name}', last_name='{self.last_name}', email='{self.email}', phone='{self.phone_number}')"

def is_valid_name(name):
    return bool(re.fullmatch(r"[A-Za-zآ-ی\s]+", name.strip()))

def is_valid_email(email):
    return bool(re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email.strip()))

def is_valid_phone(phone):
    return phone.strip().isdigit()

class Contactmanagement:
    def __init__(self):
        self.contacts = []

    def add_user(self):
        while True:
            try:
                users_number = int(input("number of users you want to add: "))
                if users_number > 0:
                    break
                else:
                    print("Number must be greater than zero.")
            except ValueError:
                print("Please enter a valid number.")

        for i in range(users_number):
            user_id = len(self.contacts) + 1

            while True:
                user_name = input("Enter user name: ")
                if is_valid_name(user_name):
                    break
                print("Invalid name (only letters and spaces allowed).")

            while True:
                user_lastname = input("Enter user last_name: ")
                if is_valid_name(user_lastname):
                    break
                print("Invalid last name (only letters and spaces allowed).")

            while True:
                user_email = input("Enter user email: ")
                if is_valid_email(user_email):
                    break
                print("Invalid email format (example: name@domain.com).")

            while True:
                user_phone = input("Enter user phone_number: ")
                if is_valid_phone(user_phone):
                    break
                print("Invalid phone number (only digits allowed).")

            contact = Contact(user_id, user_name, user_lastname, user_email, user_phone)
            self.contacts.append(contact)
            print("-" * 20)

    def delete_user(self):
        contact_id = int(input("Enter contact id for remove: "))
        for contact in self.contacts:
            if contact.id == contact_id:
                remove_user_index = self.contacts.index(contact)
                remove_user = self.contacts.pop(remove_user_index)
                print(f"User: {remove_user.name} removed!")
                return
        print("Contact not found.")

    def show_users(self):
        if len(self.contacts) == 0:
            print("No contacts.")
            return
        for user in self.contacts:
            print(f"{user.id}) Name: {user.name}\nlastname:{user.last_name}\nphone: {user.phone_number}")
            print("-" * 20)

    def search_users(self, query):
        query = query.strip().lower()
        if not query:
            return self.contacts
        results = []
        for user in self.contacts:
            if (query in user.name.lower() or
                query in user.last_name.lower() or
                query in user.email.lower() or
                query in user.phone_number.lower()):
                results.append(user)
        return results

def main():
    cm = Contactmanagement()
    while True:
        print("\nContact Manager")
        print("1. Add users")
        print("2. Show all users")
        print("3. Delete user")
        print("4. Search users")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            cm.add_user()
        elif choice == '2':
            cm.show_users()
        elif choice == '3':
            cm.delete_user()
        elif choice == '4':
            query = input("Enter search term: ")
            results = cm.search_users(query)
            if results:
                pprint(results)
            else:
                print("No results found.")
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

