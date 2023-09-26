import task_8

__author__ = "Nachiket Devendra Kamod"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Nachiket Devendra Kamod"
__email__ = "nkamod@uccs.edu"

test_students_data = [{
    "student_id": 1,
    "name": "John Doe",
    "age": 15
}, {
    "student_id": 2,
    "name": "John Smith",
    "age": 16
}, {
    "student_id": 3,
    "name": "Joe Carl",
    "age": 20
}]


def test_insert_student_data() -> None:
  # Test to insert student data into database
  for student in test_students_data:
    assert task_8.insert_student_data(student["name"],
                                      student["age"])  # returns boolean


def test_get_student_records() -> None:
  # Test to check if records in the database matches with the test cases
  for record in task_8.get_student_records():
    data_exists = any(
        student["student_id"] == record[0] and student["name"] == record[1]
        and student["age"] == record[2] for student in test_students_data)
    assert data_exists


def test_query_student_record() -> None:
  # Test to query database for perticular student by name
  record = task_8.query_student_record("John Smith")
  assert record == (2, "John Smith", 16)
