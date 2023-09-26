"""
Task 5: Lists and Dictionaries

    Create a list in Replit of your favorite books, including book titles and authors.
    Use list slicing to print the first three books in the list.
    Create a dictionary that represents a basic student database, including student names and their corresponding student IDs.
    Implement pytest test cases to verify the correctness of your code for each data structure.
"""

__author__ = "Nachiket Devendra Kamod"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Nachiket Devendra Kamod"
__email__ = "nkamod@uccs.edu"

# list of favourite books
favourite_books = [{
    "title": "Shreeman Yogi",
    "author": "Ranjeet Desai"
}, {
    "title": "Chava",
    "author": "Shivaji Sawant"
}, {
    "title": "Rau",
    "author": "Nagnath S. Inamdar",
}, {
    "title": "Panipat",
    "author": "Vishwas Patil"
}]


def print_favourite_books() -> None:
  #Function to print first 3 books
  print("List of favourite books:")
  for book in favourite_books[:3]: # List sliced to 3 items
    print(f'\nTitle: {book["title"]}\nAuthor: {book["author"]}')

# Student database
student_database = {
  "John Doe": 485,
  "Joe Public": 486,
  "Richard Miles": 487
}



