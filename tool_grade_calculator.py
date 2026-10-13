def ask_for_grades():
    """
    Ask for the grades (out of 20). Stop if empty
    """
    grades = []
    grade = input("Enter a grade (empty to stop): ")
    while grade != "":
        if int(grade) >= 0 and int(grade) <= 20:
            grades.append(grade)
        grade = input("Enter a grade (empty to stop): ")
    return grades
if __name__ == '__main__':
    print(ask_for_grades())