import streamlit as st
import json
import os

FILE_NAME = "library.txt"

# Load and save functions
def load_library():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_library(library):
    with open(FILE_NAME, "w") as file:
        json.dump(library, file, indent=4)

# Initialize session state
if "library" not in st.session_state:
    st.session_state.library = load_library()

# Header
st.title("📚 Personal Library Manager")

# Menu
menu = ["Add a Book", "Remove a Book", "Search a Book", "Display All Books", "Statistics"]
choice = st.sidebar.radio("Select an Option", menu)

# Add a Book
if choice == "Add a Book":
    st.subheader("➕ Add a New Book")
    title = st.text_input("Book Title")
    author = st.text_input("Author")
    year = st.number_input("Publication Year", min_value=0, step=1)
    genre = st.text_input("Genre")
    read = st.radio("Have you read this book?", ("Yes", "No"))

    if st.button("Add Book"):
        new_book = {
            "title": title,
            "author": author,
            "year": int(year),
            "genre": genre,
            "read": True if read == "Yes" else False
        }
        st.session_state.library.append(new_book)
        save_library(st.session_state.library)
        st.success("Book added successfully!")

# Remove a Book
elif choice == "Remove a Book":
    st.subheader("❌ Remove a Book")
    titles = [book["title"] for book in st.session_state.library]
    if titles:
        selected_title = st.selectbox("Select a book to remove", titles)
        if st.button("Remove Book"):
            st.session_state.library = [book for book in st.session_state.library if book["title"] != selected_title]
            save_library(st.session_state.library)
            st.success("Book removed successfully!")
    else:
        st.info("No books in the library.")

# Search a Book
elif choice == "Search a Book":
    st.subheader("🔍 Search for a Book")
    search_by = st.radio("Search by", ["Title", "Author"])
    query = st.text_input("Enter search text")
    if st.button("Search"):
        results = []
        if search_by == "Title":
            results = [book for book in st.session_state.library if query.lower() in book["title"].lower()]
        else:
            results = [book for book in st.session_state.library if query.lower() in book["author"].lower()]

        if results:
            st.write("### Matching Books:")
            for i, book in enumerate(results, 1):
                status = "Read" if book["read"] else "Unread"
                st.write(f"{i}. **{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - {status}")
        else:
            st.warning("No matching books found.")

# Display All Books
elif choice == "Display All Books":
    st.subheader("📖 Your Library")
    if st.session_state.library:
        for i, book in enumerate(st.session_state.library, 1):
            status = "Read" if book["read"] else "Unread"
            st.write(f"{i}. **{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        st.info("No books in your library yet.")

# Statistics
elif choice == "Statistics":
    st.subheader("📊 Library Statistics")
    total = len(st.session_state.library)
    read_books = sum(1 for book in st.session_state.library if book["read"])
    if total > 0:
        percentage = (read_books / total) * 100
        st.write(f"**Total Books:** {total}")
        st.write(f"**Books Read:** {read_books}")
        st.write(f"**Percentage Read:** {percentage:.1f}%")
    else:
        st.info("Your library is empty.")
