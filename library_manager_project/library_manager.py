import os
import json

# File to save the library
FILE_NAME = "library.txt"

# Load the library from file if it exists
def load_library():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save the library to file
def save_library(library):
    with open(FILE_NAME, "w") as file:
        json.dump(library, file, indent=4)

# Display the main menu
def display_menu():
    print("\nWelcome to your Personal Library Manager!")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")

# Add a new book
def add_book(library):
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read_input = input("Have you read this book? (yes/no): ").strip().lower()
    read = True if read_input == "yes" else False

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }
    library.append(book)
    print("Book added successfully!")

# Remove a book by title
def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip()
    removed = False
    for book in library[:]:
        if book["title"].lower() == title.lower():
            library.remove(book)
            removed = True
            print("Book removed successfully!")
            break
    if not removed:
        print("Book not found.")

# Search for a book
def search_book(library):
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter the title: ").strip().lower()
        matches = [book for book in library if title in book["title"].lower()]
    elif choice == "2":
        author = input("Enter the author: ").strip().lower()
        matches = [book for book in library if author in book["author"].lower()]
    else:
        print("Invalid choice.")
        return

    if matches:
        print("Matching Books:")
        for i, book in enumerate(matches, 1):
            status = "Read" if book["read"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("No matching books found.")

# Display all books
def display_all_books(library):
    if not library:
        print("Your library is empty.")
    else:
        print("Your Library:")
        for i, book in enumerate(library, 1):
            status = "Read" if book["read"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

# Display statistics
def display_statistics(library):
    total = len(library)
    if total == 0:
        print("No books in library.")
        return
    read_books = sum(1 for book in library if book["read"])
    percent = (read_books / total) * 100
    print(f"Total books: {total}")
    print(f"Percentage read: {percent:.1f}%")

# Main program loop
def main():
    library = load_library()

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_all_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
