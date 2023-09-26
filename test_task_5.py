import task_5

__author__ = "Nachiket Devendra Kamod"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Nachiket Devendra Kamod"
__email__ = "nkamod@uccs.edu"

def test_print_favourite_books(capsys) -> None:
  # Test to check if function prints first 3 favourite books

  # Calling the function to print the books to console
  task_5.print_favourite_books()

  # Read stdout during test execution
  captured = capsys.readouterr()

  assert captured.out == "List of favourite books:\n\nTitle: Shreeman Yogi\nAuthor: Ranjeet Desai\n\nTitle: Chava\nAuthor: Shivaji Sawant\n\nTitle: Rau\nAuthor: Nagnath S. Inamdar\n"

def test_student_database() -> None:
  # Test to check student database
  
  assert "John Doe" in task_5.student_database
  assert task_5.student_database["Joe Public"] == 486