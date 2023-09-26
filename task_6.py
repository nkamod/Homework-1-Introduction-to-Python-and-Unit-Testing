"""
Task 6: File Handling and Metaprogramming

    Write a Python program in Replit that reads a text file (you can create a sample text file) and counts the number of words in it.
    Implement metaprogramming techniques to dynamically generate function names for your pytest test cases based on the filenames of the text files.
    Include pytest test cases that verify the word count for each text file.
"""

__author__ = "Nachiket Devendra Kamod"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Nachiket Devendra Kamod"
__email__ = "nkamod@uccs.edu"


def count_words_in_text_file(file_name) -> int:
  """
  Function to count the number of words in a text file

  Parameters:
  file_name: str
    name of a file whose words counts needs to be counted

  Returns:
  int
    number of words in contents of a text file
  """

  # Read file
  with open(file_name, "r") as file:

    # Read lines in text file
    lines = file.readlines()

    # Remove new line characters and empty strings from the lines
    lines = [line.strip() for line in lines if line.strip()]

    # Join all the lines with space separation and split the string on space and store all the words in array
    words = " ".join(lines).split(" ")

  # return length of array
  return len(words)
