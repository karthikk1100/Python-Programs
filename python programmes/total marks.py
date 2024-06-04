def calculate_grade(percentage):
    if percentage >= 90:
        return 'A'
    elif 80 <= percentage < 90:
        return 'B'
    elif 70 <= percentage < 80:
        return 'C'
    elif 60 <= percentage < 70:
        return 'D'
    elif 50 <= percentage < 60:
        return 'E'
    else:
        return 'F'

def main():
    try:
        num_subjects = int(input("Enter the number of subjects: "))
        total_marks = 0
        for i in range(num_subjects):
            marks = float(input(f"Enter marks obtained in subject {i+1}: "))
            total_marks += marks
        
        percentage = (total_marks / (num_subjects * 100)) * 100
        grade = calculate_grade(percentage)
        
        print(f"Total marks: {total_marks}")
        print(f"Percentage: {percentage:.2f}%")
        print("Grade:", grade)
    except ValueError:
        print("Please enter valid marks as numbers.")

if __name__ == "__main__":
    main()
