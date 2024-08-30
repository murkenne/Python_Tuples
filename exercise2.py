'''
2. Python Data Structure Challenges in Real-World Scenarios
Task 1: Library System Enhancement Sharpen your skills in managing and modifying data within tuples and lists.

Problem Statement: You are maintaining a library system where each book is stored as a tuple within a list. 
Your task is to update this system by adding new books and ensuring no duplicates.

- Add functionality to insert new books into `library`. Ensure that adding a duplicate book is handled appropriately.

'''

def add_books(library, new_books):
    for book in new_books:
        if book not in library:
            library.append(book)
        else:
            print(f"The book '{book[0]}' by {book[1]} is already in the library.")


def main():
    library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
    
    # List of new books to add
    new_books = [("1984", "George Orwell"), ("To Kill a Mockingbird", "Harper Lee")]
    
    add_books(library, new_books)
    
    print("\nUpdated Library:")
    for book in library:
        print(f"'{book[0]}' by {book[1]}")

if __name__ == "__main__":
    main()
