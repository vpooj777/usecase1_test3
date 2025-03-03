import json
from datetime import datetime, timedelta

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.transactions = []
    
    # Book Management
    def add_book(self):
        book_id = input("Enter book ID: ")
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        copies = int(input("Enter number of copies: "))
        self.books.append({"id": book_id, "title": title, "author": author, "copies": copies})
        print("Book added successfully!")
    
    def remove_book(self):
        book_id = input("Enter book ID to remove: ")
        self.books = [book for book in self.books if book["id"] != book_id]
        print("Book removed successfully!")
    
    def list_books(self):
        print("Available Books:")
        for book in self.books:
            print(f"{book['id']} - {book['title']} by {book['author']} ({book['copies']} copies)")
    
    def search_book(self):
        title = input("Enter book title to search: ")
        results = [book for book in self.books if title.lower() in book['title'].lower()]
        if results:
            for book in results:
                print(f"Found: {book['id']} - {book['title']} by {book['author']} ({book['copies']} copies)")
        else:
            print("No books found.")
    
    def update_book(self):
        book_id = input("Enter book ID to update: ")
        for book in self.books:
            if book["id"] == book_id:
                book['title'] = input("Enter new title: ") or book['title']
                book['author'] = input("Enter new author: ") or book['author']
                book['copies'] = int(input("Enter new number of copies: ") or book['copies'])
                print("Book updated successfully!")
                return
        print("Book not found!")
    
    # User Management
    def add_user(self):
        user_id = input("Enter user ID: ")
        name = input("Enter user name: ")
        self.users.append({"id": user_id, "name": name})
        print("User added successfully!")
    
    def remove_user(self):
        user_id = input("Enter user ID to remove: ")
        self.users = [user for user in self.users if user["id"] != user_id]
        print("User removed successfully!")
    
    def list_users(self):
        print("Registered Users:")
        for user in self.users:
            print(f"{user['id']} - {user['name']}")
    
    def update_user(self):
        user_id = input("Enter user ID to update: ")
        for user in self.users:
            if user["id"] == user_id:
                user['name'] = input("Enter new name: ") or user['name']
                print("User updated successfully!")
                return
        print("User not found!")
    
    # Borrow & Return Management
    def borrow_book(self):
        user_id = input("Enter user ID: ")
        book_id = input("Enter book ID: ")
        for book in self.books:
            if book["id"] == book_id and book["copies"] > 0:
                book["copies"] -= 1
                due_date = datetime.now() + timedelta(days=14)
                self.transactions.append({"user_id": user_id, "book_id": book_id, "date": str(datetime.now()), "due_date": str(due_date), "type": "borrow"})
                print(f"Book borrowed successfully! Due date: {due_date}")
                return
        print("Book not available!")
    
    def return_book(self):
        user_id = input("Enter user ID: ")
        book_id = input("Enter book ID: ")
        for book in self.books:
            if book["id"] == book_id:
                book["copies"] += 1
                self.transactions.append({"user_id": user_id, "book_id": book_id, "date": str(datetime.now()), "type": "return"})
                print("Book returned successfully!")
                return
        print("Invalid book ID!")
    
    # Reports
    def borrowed_books_report(self):
        print("Borrowed Books Report:")
        for t in self.transactions:
            if t['type'] == 'borrow':
                print(f"User {t['user_id']} borrowed Book {t['book_id']} on {t['date']}, Due: {t['due_date']}")
    
    def returned_books_report(self):
        print("Returned Books Report:")
        for t in self.transactions:
            if t['type'] == 'return':
                print(f"User {t['user_id']} returned Book {t['book_id']} on {t['date']}")
    
    # File Operations
    def save_data(self):
        with open("library_data.json", "w") as file:
            json.dump({"books": self.books, "users": self.users, "transactions": self.transactions}, file)
        print("Library data saved!")
    
    def load_data(self):
        try:
            with open("library_data.json", "r") as file:
                data = json.load(file)
                self.books = data["books"]
                self.users = data["users"]
                self.transactions = data["transactions"]
                print("Library data loaded!")
        except FileNotFoundError:
            print("No saved data found.")
    
    # Menu
    def main_menu(self):
        while True:
            print("\nLibrary Management System")
            print("1. Add Book")
            print("2. Remove Book")
            print("3. List Books")
            print("4. Search Book")
            print("5. Update Book")
            print("6. Add User")
            print("7. Remove User")
            print("8. List Users")
            print("9. Update User")
            print("10. Borrow Book")
            print("11. Return Book")
            print("12. Borrowed Books Report")
            print("13. Returned Books Report")
            print("14. Save Data")
            print("15. Load Data")
            print("16. Exit")
            choice = input("Enter your choice: ")
            
            menu_options = {
                "1": self.add_book,
                "2": self.remove_book,
                "3": self.list_books,
                "4": self.search_book,
                "5": self.update_book,
                "6": self.add_user,
                "7": self.remove_user,
                "8": self.list_users,
                "9": self.update_user,
                "10": self.borrow_book,
                "11": self.return_book,
                "12": self.borrowed_books_report,
                "13": self.returned_books_report,
                "14": self.save_data,
                "15": self.load_data,
                "16": exit
            }
            
            action = menu_options.get(choice)
            if action:
                action()
            else:
                print("Invalid choice. Try again!")

if __name__ == "__main__":
    library = Library()
    library.main_menu()
