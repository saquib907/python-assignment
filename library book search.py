books = ["java", "python", "networking", "c++"]
search_book = input("Enter book name: ")

if search_book in books:
    print("Book is available on Shelf 1.")
else:
    print("Book is not available.")