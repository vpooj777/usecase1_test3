import json
from datetime import datetime, timedelta
 
class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.transactions = []
        self.load_data()  # Ensure data is loaded at the start
   
    # Book Management
    def add_book(self):
        book_id = input("Enter book ID: ").strip()
        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()
        copies = input("Enter number of copies: ").strip()
       
        # Ensure valid number of copies
        if not copies.isdigit():
            print("Invalid number of copies. Please enter a number.")
            return
       
        copies = int(copies)
       
        # Check if the book already exists
        for book in self.books:
            if book["id"] == book_id:
                print("Book ID already exists! Try updating instead.")
                return
 
        self.books.append({"id": book_id, "title": title, "author": author, "copies": copies})
        print("Book added successfully!")
        self.save_data()  # Save data immediately
 
    def remove_book(self):
        book_id = input("Enter book ID to remove: ").strip()
        original_length = len(self.books)
        self.books = [book for book in self.books if book["id"] != book_id]
 
        if len(self.books) < original_length:
            print("Book removed successfully!")
            self.save_data()  # Save changes
        else:
            print("Book not found!")
 
    def list_books(self):
        if not self.books:
            print("No books available.")
            return
        print("\nAvailable Books:")
        for book in self.books:
            print(f"{book['id']} - {book['title']} by {book['author']} ({book['copies']} copies)")
 
    def search_book(self):
        title = input("Enter book title to search: ").strip().lower()
        results = [book for book in self.books if title in book['title'].lower()]
        if results:
            for book in results:
                print(f"Found: {book['id']} - {book['title']} by {book['author']} ({book['copies']} copies)")
        else:
            print("No books found.")
 
    def update_book(self):
        book_id = input("Enter book ID to update: ").strip()
        for book in self.books:
            if book["id"] == book_id:
                new_title = input("Enter new title (press Enter to keep current): ").strip()
                new_author = input("Enter new author (press Enter to keep current): ").strip()
                new_copies = input("Enter new number of copies (press Enter to keep current): ").strip()
               
                book['title'] = new_title if new_title else book['title']
                book['author'] = new_author if new_author else book['author']
               
                if new_copies.isdigit():
                    book['copies'] = int(new_copies)
 
                print("Book updated successfully!")
                self.save_data()
                return
       
        print("Book not found!")
 
    # User Management
    def add_user(self):
        user_id = input("Enter user ID: ").strip()
        name = input("Enter user name: ").strip()
        self.users.append({"id": user_id, "name": name})
        print("User added successfully!")
        self.save_data()
 
    def remove_user(self):
        user_id = input("Enter user ID to remove: ").strip()
        original_length = len(self.users)
        self.users = [user for user in self.users if user["id"] != user_id]
 
        if len(self.users) < original_length:
            print("User removed successfully!")
            self.save_data()
        else:
            print("User not found!")
 
    def list_users(self):
        if not self.users:
            print("No users registered.")
            return
        print("\nRegistered Users:")
        for user in self.users:
            print(f"{user['id']} - {user['name']}")
 
    def update_user(self):
        user_id = input("Enter user ID to update: ").strip()
        for user in self.users:
            if user["id"] == user_id:
                new_name = input("Enter new name (press Enter to keep current): ").strip()
                user['name'] = new_name if new_name else user['name']
                print("User updated successfully!")
                self.save_data()
                return
        print("User not found!")
 
    # Borrow & Return Management
    def borrow_book(self):
        user_id = input("Enter user ID: ").strip()
        book_id = input("Enter book ID: ").strip()
       
        for book in self.books:
            if book["id"] == book_id and book["copies"] > 0:
                book["copies"] -= 1
                due_date = datetime.now() + timedelta(days=14)
                self.transactions.append({
                    "user_id": user_id, "book_id": book_id,
                    "date": str(datetime.now()), "due_date": str(due_date), "type": "borrow"
                })
                print(f"Book borrowed successfully! Due date: {due_date}")
                self.save_data()
                return
       
        print("Book not available!")
 
    def return_book(self):
        user_id = input("Enter user ID: ").strip()
        book_id = input("Enter book ID: ").strip()
       
        for book in self.books:
            if book["id"] == book_id:
                book["copies"] += 1
                self.transactions.append({
                    "user_id": user_id, "book_id": book_id,
                    "date": str(datetime.now()), "type": "return"
                })
                print("Book returned successfully!")
                self.save_data()
                return
       
        print("Invalid book ID!")
 
    # File Operations
    def save_data(self):
        with open("library_data.json", "w") as file:
            json.dump({"books": self.books, "users": self.users, "transactions": self.transactions}, file, indent=4)
        print("Library data saved!")
 
    def load_data(self):
        try:
            with open("library_data.json", "r") as file:
                data = json.load(file)
                self.books = data.get("books", [])
                self.users = data.get("users", [])
                self.transactions = data.get("transactions", [])
                print("Library data loaded!")
        except (FileNotFoundError, json.JSONDecodeError):
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
            print("12. Save Data")
            print("13. Load Data")
            print("14. Exit")
           
            choice = input("Enter your choice: ").strip()
            menu_options = {
                "1": self.add_book, "2": self.remove_book, "3": self.list_books,
                "4": self.search_book, "5": self.update_book, "6": self.add_user,
                "7": self.remove_user, "8": self.list_users, "9": self.update_user,
                "10": self.borrow_book, "11": self.return_book,
                "12": self.save_data, "13": self.load_data, "14": exit
            }
 
            action = menu_options.get(choice)
            if action:
                action()
            else:
                print("Invalid choice. Try again!")
 
if __name__ == "__main__":
    library = Library()
    library.main_menu()
