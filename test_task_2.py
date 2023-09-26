import task_2

__author__ = "Nachiket Devendra Kamod"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Nachiket Devendra Kamod"
__email__ = "nkamod@uccs.edu"

def test_intger() -> None:
  # Test to check if data type of variable `integer` is int
  assert type(task_2.integer) == int

def test_floating() -> None:
  # Test to check if data type of variable `floating` is float
  assert type(task_2.floating) == float

def test_string() -> None:
  # Test to check if data type of variable `string` is str
  assert type(task_2.string) == str

def test_boolean() -> None:
  # Test to check if data type of variable `boolean` is bool
  assert type(task_2.boolean) == bool