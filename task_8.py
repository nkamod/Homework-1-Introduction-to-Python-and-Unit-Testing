"""
Task 8: PostgreSQL Database Access in Replit
Create a PostgreSQL database using Replit's built-in database functionality. Define a table called "students" with columns for student ID, name, and age.
Write a Python script in Replit that connects to the PostgreSQL database, inserts a new student record, and queries the database to retrieve student information.
Use pytest test cases to validate the functionality of your PostgreSQL interactions.
"""

import sqlite3

# connection object representing database
con = sqlite3.connect("task_8.db")
cur = con.cursor()

# Drop table students if already exists
cur.execute("DROP TABLE IF EXISTS students")
con.commit()

# Create a fresh students table
cur.execute(
    "CREATE TABLE IF NOT EXISTS students (student_id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(255) NOT NULL UNIQUE, age INTEGER NOT NULL);"
)


def insert_student_data(name, age) -> bool:
  """
  Function to insert student record into the database table

  Parameters:
  name: string
    Name of the student

  age: int
    Age of the student

  Returns:
  bool
    If insertion successful then true else false
  """

  try:
    cur.execute("INSERT INTO students (name, age) VALUES (?, ?)", (name, age))
    con.commit()
  except sqlite3.IntegrityError as _:
    return False

  return True


def get_student_records():
  # Function to fetch all the student records
  res = cur.execute("SELECT * FROM students")
  return res.fetchall()


def query_student_record(name):
  """
  Function to query student record by name

  Parameters:
  name: string
    Name of the student

  return:
    student record or None
  """
  cur.execute("SELECT * FROM students WHERE name=?", (name, ))
  res = cur.fetchone()
  return res if res else None
