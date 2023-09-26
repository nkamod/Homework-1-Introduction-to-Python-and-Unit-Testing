import task_3

__author__ = "Nachiket Devendra Kamod"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Nachiket Devendra Kamod"
__email__ = "nkamod@uccs.edu"

def test_polarity() -> None:
  # Test to check if given number is positive, negative or zero
  
  assert task_3.polarity(5) == "POSITIVE"
  assert task_3.polarity(-5) == "NEGATIVE"
  assert task_3.polarity(0) == "ZERO"

def test_print_prime(capsys) -> None:
  # Test to check if function prints first 10 prime numbers

  # Calling the function to calculate and print the prime numbers to console
  task_3.print_prime()

  # Read stdout during test execution
  captured = capsys.readouterr()

  """
  First 10 prime numbers:
  2
  3
  5
  7
  11
  13
  17
  19
  23
  29
  Where, \n is new line
  """
  assert captured.out == "2\n3\n5\n7\n11\n13\n17\n19\n23\n29\n"

def summation_till_100() -> None:
  # Test to check if function returns summation of 1 to 100 using while loop
  
  n = 100

  # Summation of 1 to n, is (n * (n+1)) / 2
  assert task_3.summation_till_100() == (n * (n+1)) / 2 

