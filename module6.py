try:
    # Taking marks input from the user (out of 100 each)
    subject1_marks = float(input("Enter marks for Subject 1: "))
    subject2_marks = float(input("Enter marks for Subject 2: "))
    subject3_marks = float(input("Enter marks for Subject 3: "))
    subject4_marks = float(input("Enter marks for Subject 4: "))
    subject5_marks = float(input("Enter marks for Subject 5: "))

    # Storing all marks in a list for easier checking
    marks_list = [
        subject1_marks,
        subject2_marks,
        subject3_marks,
        subject4_marks,
        subject5_marks
    ]

    # Checking if any mark is invalid (less than 0 or greater than 100)
    for mark in marks_list:
        if mark < 0 or mark > 100:
            raise ValueError("Marks should be between 0 and 100 only.")

    # Calculating total marks (out of 500)
    total_marks = sum(marks_list)

    # Calculating percentage
    percentage = (total_marks / 500) * 100

    # Determining grade based on percentage
    if percentage >= 90:
        grade = "A+ (Outstanding)"
    elif percentage >= 80:
        grade = "A (Excellent)"
    elif percentage >= 70:
        grade = "B (Good)"
    elif percentage >= 60:
        grade = "C (Average)"
    elif percentage >= 50:
        grade = "D (Pass)"
    else:
        grade = "F (Fail)"

    # Determining Pass/Fail result
    # Student must score at least 40 in ALL subjects
    if all(mark >= 40 for mark in marks_list):
        result = "Pass"
    else:
        result = "Fail"

    # Displaying results
    print("\n----- RESULT SUMMARY -----")
    print("Marks in each subject:", marks_list)
    print("Total Marks (out of 500):", total_marks)
    print(f"Percentage: {percentage:.2f}%")
    print("Grade:", grade)
    print("Result:", result)

# Handles non-numeric input
except ValueError as error:
    print("Invalid input!", error)

# Handles any other unexpected errors
except Exception as error:
    print("Something went wrong:", error)
