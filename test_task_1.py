import task_1

__author__ = "Nachiket Devendra Kamod"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Nachiket Devendra Kamod"
__email__ = "nkamod@uccs.edu"

def test_console_print(capsys) -> None:
    # Test to check if function prints "Hello, Replit!"

    # Calling the function to print the string to console
    task_1.console_print()

    # Read stdout during test execution
    captured = capsys.readouterr()
    assert captured.out == "Hello, Replit!\n"
