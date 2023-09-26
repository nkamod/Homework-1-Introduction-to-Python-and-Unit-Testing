import requests as req
"""
Task 7: Package Control in Replit
Use Replit's built-in package manager to add a Python package of your choice to your project (e.g., requests, numpy, matplotlib).
Write a Python script that demonstrates how to use the chosen package to perform a specific task or function.
Implement pytest test cases to verify the correctness of your code when using the package.
"""

__author__ = "Nachiket Devendra Kamod"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Nachiket Devendra Kamod"
__email__ = "nkamod@uccs.edu"


def get_coffies(type):
  """
  Function to get coffies from api

  Parameters:
  type: string
    type of coffee (hot, iced)

  Returns:
  int
    status code of response

  list[dict]
    json response
  """

  response = req.get(f'https://api.sampleapis.com/coffee/{type}')
  return response.status_code, response.json()
