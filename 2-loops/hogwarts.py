"""
students = ["Hermione", "Harry", "Ron"]

# method 1
for student in students:
  print(student)

# method 2
for i in range(len(students)):
  print(f"{i+1}: {students[i]}")
"""

"""
students = {
  "Hermione": "Gryffindor",
  "Harry": "Gryffindor",
  "Ron": "Gryffindor",
  "Draco": "Slytherin"
}

for student in students:
  print(student, students[student], sep=": ")
"""

students = [
  {"name": "Hermione", "house": "Gryffindor", 'patronus': 'Otter'},
  {"name": "Harry", "house": "Gryffindor", 'patronus': 'Stag'},
  {"name": "Ron", "house": "Gryffindor", 'patronus': 'Jack Russell'},
  {"name": "Draco", "house": "Slytherin", 'patronus': None}
]

for i in range(len(students)):
  print(f"{students[i]['name']} is in {students[i]['house']}")

#  or

for student in students:
  print(f"{student['name']} is in {student['house']}")
