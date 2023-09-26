"""
Task 3: Control Structures

    a) Write a Python program in Replit that includes an if statement to check if a given number is positive, negative, or zero.
    b) Implement a for loop to print the first 10 prime numbers (you may need to research how to calculate prime numbers).
    c) Use a while loop to find the sum of all numbers from 1 to 100.
    Write pytest test cases to verify the correctness of your code for each control structure.
"""

__author__ = "Nachiket Devendra Kamod"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Nachiket Devendra Kamod"
__email__ = "nkamod@uccs.edu"

def polarity(num) -> str:
  """
  a) Function which returns polarity of a number

  Parameters:
  num: number

  Returns:
  str
    Polarity of parameter.

  TypeError
    If provided parameter is other than number.
  """

  # Handle if paramater is not a number
  if not isinstance(num, (int, float)):
    raise TypeError("Given parameter is not a number")
  
  if num < 0:
    return "NEGATIVE"
  if num > 0:
    return "POSITIVE"

  return "ZERO"

def print_prime() -> None:
  """
  b) Function to print first 10 prime numbers

  Returns:
  list[int]
    first 10 prime numbers
  """
  count = 0
  # Since 0 and 1 are not prime numbers we start from 2
  n = 2

  # Loop till we get 10 prime numbers
  while count < 10:

    # Assuming current number is prime
    is_prime = True

    # Check for factors of n by iterating from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
      # If n is divisible by i, it's not prime
      if n % i == 0:
        is_prime = False
        break

    # If is_prime is still True after the loop, n is prime
    if is_prime:
      count += 1
      print(n)
    
    # Move to the next number to check for primality
    n += 1

def summation_till_100() -> int:
  """
  c) Function to return summation of 1 to 100

  Returns:
  int
    summation of 1 to 100
  """
  # Initialize a variable to store the sum
  summation = 0
  
  # Initialize a counter variable to start from 1
  i = 1
  
  # Use a while loop to iterate from 1 to 100
  while i <= 100:
      # Add the current value of i to the sum
      summation += i
      
      # Increment i to move to the next number
      i += 1
  
  # Return the final sum after the loop is finished
  return summation