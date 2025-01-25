def calculate_total(marks):
    """
        Calculate total marks.
    """
    return sum(marks)

def calculate_percentage(total_marks, max_marks = 500):
    """
        Calculate percentage based on total marks
    """
    return (total_marks / max_marks) * 100

def determine_grade(percentage):
    """
        Determine grade based on percentage
    """
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "Fail"

def get_marks():
    """
        Get marks for 5 subjects with input validation
    """
    marks = []
    for i in range(1, 6):
        while True:
            try:
                mark = float(input(f"Enter marks for subject {i} (0-100): "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Please enter a valid mark between 0 and 100.")
            except ValueError:
                print("Invalid input! Please enter a valid number.")
    return marks

def display_result(name, total_marks, percentage, grade):
    """
        Display student result including name, total, percentage, and grade.
    """
    print(f"\nStudent Name: {name}")
    print(f"Total Marks: {total_marks}/500")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

def main():
    name = input("Enter student's name: ").strip()
    marks = get_marks()
    
    total_marks = calculate_total(marks)
    percentage = calculate_percentage(total_marks)
    grade = determine_grade(percentage)
    
    display_result(name, total_marks, percentage, grade)


main()