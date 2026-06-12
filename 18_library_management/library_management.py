import os
import sys
import datetime

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


books = {
    1: {"title": "Harry Potter", "author": "J.K. Rowling", "volume": 1, "status": "available"},
    2: {"title": "Harry Potter", "author": "J.K. Rowling", "volume": 2, "status": "available"},
    3: {"title": "Harry Potter", "author": "J.K. Rowling", "volume": 3, "status": "available"},
    4: {"title": "Clean Code", "author": "Robert C. Martin", "volume": None, "status": "available"},
    5: {"title": "The Pragmatic Programmer", "author": "Andy Hunt", "volume": None, "status": "available"},
}


users = {
    "john": {"display_name": "John", "blocked": False},
    "alice": {"display_name": "Alice", "blocked": False},
}

# borrow_records = {
#     record_id (int): {
#         "book_ids": list of int,
#         "title": str,
#         "user_name": str,
#         "receive_date": datetime.date,
#         "return_date": datetime.date or None
#     }
# }
borrow_records = {}
next_record_id = 1


def print_header(title):
    print(f"\n--- {title} ---")


def print_message(success, message):
    if success:
        print(f"SUCCESS: {message}")
    else:
        print(f"ERROR: {message}")


def get_books_in_collection(book_id):
    """
    Returns all book IDs belonging to the same collection as book_id.
    A collection is defined as books sharing the same Title (case-insensitive).
    """
    if book_id not in books:
        return []
    target_title = books[book_id]["title"].lower().strip()
    matching_ids = [bid for bid, b in books.items() if b["title"].lower().strip() == target_title]
    return sorted(matching_ids)


def parse_date(date_str):
    """Parses a date string in DD-MM-YYYY format."""
    try:
        return datetime.datetime.strptime(date_str.strip(), "%d-%m-%Y").date()
    except ValueError:
        return None



# ADMIN FUNCTIONS


def add_book(book_id, title, author, volume=None):
    # Check if book ID already exists
    if book_id in books:
        return False, f"Book ID {book_id} already exists."
    
    # Check sequential numbering requirement
    max_id = max(books.keys()) if books else 0
    if book_id > max_id + 1:
        next_expected = max_id + 1
        return False, f"Cannot skip book numbers. The next sequential Book ID must be {next_expected} (or less, to fill gaps)."
        
    if book_id < 1:
        return False, "Book ID must be 1 or greater."
        
    books[book_id] = {
        "title": title,
        "author": author,
        "volume": volume,
        "status": "available"
    }
    return True, f"Book '{title}' (Vol: {volume if volume else 'N/A'}) with ID {book_id} has been added."


def remove_book(book_id):
    if book_id not in books:
        return False, f"Book ID {book_id} does not exist."
        
    # Check if book is currently issued
    if books[book_id]["status"] == "issued":
        return False, f"Book ID {book_id} is currently issued and cannot be removed."
        
    title = books[book_id]["title"]
    vol = books[book_id]["volume"]
    vol_str = f" (Vol: {vol})" if vol else ""
    del books[book_id]
    return True, f"Book ID {book_id}: '{title}'{vol_str} has been removed from the catalog."


def clear_entry_for_book(book_id):
    if book_id not in books:
        return False, f"Book ID {book_id} does not exist."
        
    # Find active borrow record containing this book_id
    found_rec_id = None
    for rec_id, rec in borrow_records.items():
        if rec["return_date"] is None and book_id in rec["book_ids"]:
            found_rec_id = rec_id
            break
            
    if found_rec_id is not None:
        rec = borrow_records[found_rec_id]
        # Mark all books in this collection/record as available
        for bid in rec["book_ids"]:
            if bid in books:
                books[bid]["status"] = "available"
        # Set return date to equal receive date (clearing it without penalty)
        rec["return_date"] = rec["receive_date"]
        return True, f"Cleared active borrowing record for '{rec['title']}' (Record ID: {found_rec_id}). Books are now available."
    else:
        # If the book status is somehow "issued" but there is no active borrow record
        if books[book_id]["status"] == "issued":
            books[book_id]["status"] = "available"
            return True, f"Reset status of Book ID {book_id} to 'available'."
        return False, f"Book ID {book_id} is not currently issued and has no active borrowing records."


def get_borrowed_books_list():
    borrowed = []
    for rec_id, rec in borrow_records.items():
        if rec["return_date"] is None:
            book_ids_str = ", ".join(str(bid) for bid in rec["book_ids"])
            due_date = rec["receive_date"] + datetime.timedelta(days=14)
            borrowed.append({
                "book_ids": book_ids_str,
                "title": rec["title"],
                "user": rec["user_name"],
                "issue_date": rec["receive_date"].strftime("%d-%m-%Y"),
                "due_date": due_date.strftime("%d-%m-%Y")
            })
    return borrowed



# USER FUNCTIONS


def search_books_by_title(substring):
    query = substring.lower().strip()
    results = []
    for bid, b in books.items():
        if query in b["title"].lower():
            results.append((bid, b))
    return results


def search_books_by_author(author_name):
    query = author_name.lower().strip()
    results = []
    for bid, b in books.items():
        if query in b["author"].lower():
            results.append((bid, b))
    return results


def receive_book(user_name, book_id, receive_date_str):
    global next_record_id
    
    if book_id not in books:
        return False, "Book ID not found."
        
    user_key = user_name.lower().strip()
    
    # Check if user is blocked
    if user_key in users and users[user_key]["blocked"]:
        return False, f"User '{user_name}' is currently BLOCKED due to late return and cannot issue books."
        
    # Find all books in the collection
    collection_ids = get_books_in_collection(book_id)
    title = books[book_id]["title"]
    
    # Parse receive date
    rec_date = parse_date(receive_date_str)
    if not rec_date:
        return False, "Invalid date format. Use DD-MM-YYYY."
        
    # Check if any book in the collection is already issued
    issued_books = [bid for bid in collection_ids if books[bid]["status"] == "issued"]
    if issued_books:
        if len(collection_ids) > 1:
            return False, f"Collection '{title}' is unavailable. Book IDs {issued_books} are currently checked out."
        else:
            return False, f"Book '{title}' is already issued."
            
    # Auto-register user if not already in dictionary
    if user_key not in users:
        users[user_key] = {"display_name": user_name, "blocked": False}
        
    # Issue all books in collection/unit
    for bid in collection_ids:
        books[bid]["status"] = "issued"
        
    # Store borrow record
    borrow_records[next_record_id] = {
        "book_ids": collection_ids,
        "title": title,
        "user_name": users[user_key]["display_name"],
        "receive_date": rec_date,
        "return_date": None
    }
    next_record_id += 1
    
    if len(collection_ids) > 1:
        vols = ", ".join(f"Vol {books[bid]['volume']}" for bid in collection_ids)
        return True, f"Issued the entire collection of '{title}' ({vols}) under Book IDs: {collection_ids}."
    else:
        return True, f"Issued '{title}' (Book ID: {book_id})."


def find_active_record(query):
    """Finds an active borrow record matching the query (Book ID or Title)."""
    # 1. Check if query is an active Book ID
    try:
        book_id = int(query)
        for rec_id, rec in borrow_records.items():
            if rec["return_date"] is None and book_id in rec["book_ids"]:
                return rec_id, rec
    except ValueError:
        pass
        
    # 2. Check if query matches Title case-insensitively
    query_title = query.lower().strip()
    for rec_id, rec in borrow_records.items():
        if rec["return_date"] is None and rec["title"].lower().strip() == query_title:
            return rec_id, rec
            
    return None, None


def return_book(book_id_or_title, return_date_str):
    rec_id, rec = find_active_record(book_id_or_title)
    if rec is None:
        return False, "No active borrowing record found for this Book ID or Title."
        
    ret_date = parse_date(return_date_str)
    if not ret_date:
        return False, "Invalid date format. Use DD-MM-YYYY."
        
    receive_date = rec["receive_date"]
    if ret_date < receive_date:
        return False, f"Return date ({return_date_str}) cannot be earlier than receive date ({receive_date.strftime('%d-%m-%Y')})."
        
    # Calculate days borrowed
    days_borrowed = (ret_date - receive_date).days
    
    # Update record
    rec["return_date"] = ret_date
    
    # Mark books in record as available
    for bid in rec["book_ids"]:
        if bid in books:
            books[bid]["status"] = "available"
            
    user_name = rec["user_name"]
    user_key = user_name.lower().strip()
    
    blocked_info = ""
    # Block user if return exceeds 14 days
    if days_borrowed > 14:
        if user_key in users:
            users[user_key]["blocked"] = True
        else:
            users[user_key] = {"display_name": user_name, "blocked": True}
        blocked_info = f"\nLATE RETURN WARNING: Book returned after {days_borrowed} days (limit 14). User '{user_name}' is now BLOCKED."
        
    msg = f"Returned '{rec['title']}' borrowed by '{user_name}'. Total days borrowed: {days_borrowed}." + blocked_info
    return True, msg




def display_books_catalog():
    print_header("Books Catalog")
    if not books:
        print("No books in the library catalog.")
        return
        
    print(f"{'ID':<6}{'Title':<30}{'Author':<20}{'Vol':<6}{'Status':<12}")
    print("-" * 75)
    
    titles = [b["title"].lower().strip() for b in books.values()]
    
    for bid in sorted(books.keys()):
        b = books[bid]
        title = b["title"]
        author = b["author"]
        vol = str(b["volume"]) if b["volume"] else "-"
        
        is_collection = titles.count(title.lower().strip()) > 1
        status_str = "Available" if b["status"] == "available" else "Issued"
        
        vol_display = f"{vol}"
        if is_collection:
            vol_display += " (Col)"
            
        print(f"{bid:<6}{title:<30}{author:<20}{vol_display:<16}{status_str:<12}")
    print("-" * 75)


def display_users():
    print_header("Library Members")
    if not users:
        print("No registered library members.")
        return
        
    print(f"{'Username':<20}{'Status':<15}")
    print("-" * 35)
    for ukey, u in users.items():
        status = "Blocked" if u["blocked"] else "Active"
        print(f"{u['display_name']:<20}{status:<15}")
    print("-" * 35)


def menu_admin():
    while True:
        print_header("Admin Control Panel")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Clear Entry for Book")
        print("4. View Borrowed Books")
        print("5. View Library Members")
        print("6. Unblock User (Extra)")
        print("0. Back to Main Menu")
        
        choice = input("\nSelect option: ").strip()
        if choice == "1":
            print_header("Add New Book")
            try:
                bid_str = input("Enter Book ID: ").strip()
                if not bid_str:
                    print_message(False, "Book ID is required.")
                    input("\nPress Enter to continue...")
                    continue
                bid = int(bid_str)
            except ValueError:
                print_message(False, "Book ID must be an integer.")
                input("\nPress Enter to continue...")
                continue
                
            title = input("Enter Book Title: ").strip()
            if not title:
                print_message(False, "Book Title cannot be empty.")
                input("\nPress Enter to continue...")
                continue
                
            author = input("Enter Author: ").strip()
            if not author:
                print_message(False, "Author cannot be empty.")
                input("\nPress Enter to continue...")
                continue
                
            vol_str = input("Enter Volume Number (leave blank if none): ").strip()
            volume = None
            if vol_str:
                try:
                    volume = int(vol_str)
                except ValueError:
                    print_message(False, "Volume Number must be an integer.")
                    input("\nPress Enter to continue...")
                    continue
                    
            success, msg = add_book(bid, title, author, volume)
            print_message(success, msg)
            input("\nPress Enter to continue...")
            
        elif choice == "2":
            print_header("Remove Book")
            try:
                bid = int(input("Enter Book ID to remove: ").strip())
                success, msg = remove_book(bid)
                print_message(success, msg)
            except ValueError:
                print_message(False, "Book ID must be an integer.")
            input("\nPress Enter to continue...")
            
        elif choice == "3":
            print_header("Clear Entry for Book")
            try:
                bid = int(input("Enter Book ID to clear record: ").strip())
                success, msg = clear_entry_for_book(bid)
                print_message(success, msg)
            except ValueError:
                print_message(False, "Book ID must be an integer.")
            input("\nPress Enter to continue...")
            
        elif choice == "4":
            print_header("Currently Borrowed Books")
            borrowed = get_borrowed_books_list()
            if not borrowed:
                print("No books are currently borrowed.")
            else:
                print(f"{'Book ID':<15}{'Title':<25}{'User':<12}{'Issue Date':<12}{'Due Date':<12}")
                print("-" * 80)
                for b in borrowed:
                    print(f"{b['book_ids']:<15}{b['title']:<25}{b['user']:<12}{b['issue_date']:<12}{b['due_date']:<12}")
                print("-" * 80)
            input("\nPress Enter to continue...")
            
        elif choice == "5":
            display_users()
            input("\nPress Enter to continue...")
            
        elif choice == "6":
            print_header("Unblock User")
            user_name = input("Enter Username to unblock: ").strip()
            user_key = user_name.lower()
            if user_key in users:
                if users[user_key]["blocked"]:
                    users[user_key]["blocked"] = False
                    print_message(True, f"User '{users[user_key]['display_name']}' has been unblocked.")
                else:
                    print_message(False, f"User '{users[user_key]['display_name']}' is not blocked.")
            else:
                print_message(False, f"User '{user_name}' does not exist.")
            input("\nPress Enter to continue...")
            
        elif choice == "0":
            break


def menu_user():
    while True:
        print_header("User Section")
        print("1. View Available Books")
        print("2. Search Book by Title")
        print("3. Search Book by Author")
        print("4. Receive Book (Issue)")
        print("5. Return Book")
        print("0. Back to Main Menu")
        
        choice = input("\nSelect option: ").strip()
        
        if choice == "1":
            display_books_catalog()
            input("\nPress Enter to continue...")
            
        elif choice == "2":
            print_header("Search Book by Title")
            substring = input("Enter search query: ").strip()
            if not substring:
                print_message(False, "Search query cannot be empty.")
            else:
                results = search_books_by_title(substring)
                if not results:
                    print(f"\nNo books matching title '{substring}' found.")
                else:
                    print(f"\n{'ID':<6}{'Title':<30}{'Author':<20}{'Vol':<6}{'Status':<12}")
                    print("-" * 75)
                    for bid, b in results:
                        vol = str(b["volume"]) if b["volume"] else "-"
                        status_str = "Available" if b["status"] == "available" else "Issued"
                        print(f"{bid:<6}{b['title']:<30}{b['author']:<20}{vol:<6}{status_str:<12}")
                    print("-" * 75)
            input("\nPress Enter to continue...")
            
        elif choice == "3":
            print_header("Search Book by Author")
            author = input("Enter Author name: ").strip()
            if not author:
                print_message(False, "Author name cannot be empty.")
            else:
                results = search_books_by_author(author)
                if not results:
                    print(f"\nNo books written by '{author}' found.")
                else:
                    print(f"\n{'ID':<6}{'Title':<30}{'Author':<20}{'Vol':<6}{'Status':<12}")
                    print("-" * 75)
                    for bid, b in results:
                        vol = str(b["volume"]) if b["volume"] else "-"
                        status_str = "Available" if b["status"] == "available" else "Issued"
                        print(f"{bid:<6}{b['title']:<30}{b['author']:<20}{vol:<6}{status_str:<12}")
                    print("-" * 75)
            input("\nPress Enter to continue...")
            
        elif choice == "4":
            print_header("Receive Book (Issue)")
            display_books_catalog()
            
            try:
                bid_str = input("\nEnter Book ID to issue: ").strip()
                if not bid_str:
                    print_message(False, "Book ID is required.")
                    input("\nPress Enter to continue...")
                    continue
                bid = int(bid_str)
            except ValueError:
                print_message(False, "Book ID must be an integer.")
                input("\nPress Enter to continue...")
                continue
                
            user_name = input("Enter Your Name: ").strip()
            if not user_name:
                print_message(False, "User Name cannot be empty.")
                input("\nPress Enter to continue...")
                continue
                
            today_str = datetime.date.today().strftime("%d-%m-%Y")
            receive_date_str = input(f"Enter Receive Date (DD-MM-YYYY) [Default: {today_str}]: ").strip()
            if not receive_date_str:
                receive_date_str = today_str
                
            success, msg = receive_book(user_name, bid, receive_date_str)
            print_message(success, msg)
            input("\nPress Enter to continue...")
            
        elif choice == "5":
            print_header("Return Book")
            query = input("Enter Book ID or Book Title to return: ").strip()
            if not query:
                print_message(False, "Book ID or Title is required.")
                input("\nPress Enter to continue...")
                continue
                
            today_str = datetime.date.today().strftime("%d-%m-%Y")
            return_date_str = input(f"Enter Return Date (DD-MM-YYYY) [Default: {today_str}]: ").strip()
            if not return_date_str:
                return_date_str = today_str
                
            success, msg = return_book(query, return_date_str)
            print_message(success, msg)
            input("\nPress Enter to continue...")
            
        elif choice == "0":
            break


def main():
    while True:
        print_header("Library Management System")
        print("Welcome to the Library System!")
        print("Please choose your role:")
        print("1. Administrator")
        print("2. User / Member")
        print("0. Exit Application")
        
        choice = input("\nSelect option: ").strip()
        if choice == "1":
            menu_admin()
        elif choice == "2":
            menu_user()
        elif choice == "0":
            print("\nThank you for using the Library Management System! Goodbye.\n")
            break


if __name__ == "__main__":
    main()
