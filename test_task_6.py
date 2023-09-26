import task_6

__author__ = "Nachiket Devendra Kamod"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Nachiket Devendra Kamod"
__email__ = "nkamod@uccs.edu"

test_files = [{
    "file_name": "task_6_inp_1.txt",
    "expected_output": 200
}, {
    "file_name": "task_6_inp_2.txt",
    "expected_output": 252
}]


# Command: pytest -k test_count_words_{file_name_without_extension}
def generate_test_cases(file):
  # Function to generate pytest test cases for each text file
  def test_count_words_in_text_file():
    assert task_6.count_words_in_text_file(
        file["file_name"]) == file["expected_output"]

  # Assign function name for each test case dynamically
  test_count_words_in_text_file.__name__ = f'test_count_words_{file["file_name"].split(".")[0]}'

  return test_count_words_in_text_file


# Generate pytest test cases for each text file
for file in test_files:
  globals()[generate_test_cases(file).__name__] = generate_test_cases(file)
