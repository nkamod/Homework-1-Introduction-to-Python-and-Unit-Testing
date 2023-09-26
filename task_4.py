"""
Task 4: Functions and Duck Typing

    Duck typing is the functionality of a language where “if it looks like a duck and quacks like a duck, you might as well treat it like a duck.” This is quite common in interpreted languages.
    Create a Python function in Replit named calculate_discount that calculates the final price of a product after applying a given discount percentage. The function should accept any numeric type for price and discount.
    Write pytest test cases to test the calculate_discount function with various types (integers, floats) for price and discount.
"""

from typing import Union

__author__ = "Nachiket Devendra Kamod"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Nachiket Devendra Kamod"
__email__ = "nkamod@uccs.edu"

def calculate_discount(price, discount) -> Union[int, float]:
  # Function to calculate final price after applying discount
  
  # Handle if given paramaters are not numbers
  if not isinstance(price, (int, float)) or not isinstance(discount, (int, float)):
    raise TypeError("One of the given parameter is not a number")

  # calculate final price after discount
  return (price * (100 - discount)) / 100