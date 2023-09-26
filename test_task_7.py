import task_7

__author__ = "Nachiket Devendra Kamod"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Nachiket Devendra Kamod"
__email__ = "nkamod@uccs.edu"


def test_get_coffies() -> None:
  # Test to fetch different types of coffies and validate the response

  status_code, response = task_7.get_coffies("hot")
  assert status_code == 200
  assert response[0]["title"] == "Black"

  status_code, response = task_7.get_coffies("iced")
  assert status_code == 200
  assert response[1]["title"] == "Iced Espresso"

  # api only provides hot and iced coffies
  status_code, response = task_7.get_coffies("cold")
  assert status_code == 500
