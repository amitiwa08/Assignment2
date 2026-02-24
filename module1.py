student_name = "John Doe"
student_age = 20
student_course = "Python Programming"
student_college = "ABC University"
student_email = "john@example.com"

border = "╔" + "═" * 32 + "╗"
bottom_border = "╚" + "═" * 32 + "╝"

print(border)
print("║{:^32}║".format("STUDENT BIO CARD"))
print("╠" + "═" * 32 + "╣")
print("║{:<32}║".format(f"Name : {student_name}"))
print("║{:<32}║".format(f"Age : {student_age} years"))
print("║{:<32}║".format(f"Course : {student_course}"))
print("║{:<32}║".format(f"College : {student_college}"))
print("║{:<32}║".format(f"Email : {student_email}"))
print(bottom_border)
