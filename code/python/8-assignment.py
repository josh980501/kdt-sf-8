student_dict = {}

student_dict.update({"Alice": 85, "Bob": 90, "Charlie": 95})
print(student_dict)

student_dict.update({"David": 80})
print(student_dict)

student_dict["Alice"] = 88
print(student_dict)

student_dict.pop("Bob")
print(student_dict)
