import task_4

__author__ = "Nachiket Devendra Kamod"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Nachiket Devendra Kamod"
__email__ = "nkamod@uccs.edu"

def test_calculate_discount() -> None:
  # Test the calculate_discount function with various types (integers, floats) for price and discount.
  
  assert task_4.calculate_discount(100, 30) == 70
  assert task_4.calculate_discount(45, 35) == 29.25
  assert task_4.calculate_discount(85.78, 21.3) == 67.50886