def ask_for_grades():
    """
    Ask for the grades (out of 20). Stop if empty
    """
    grades = []
    grade = input("Enter a grade (empty to stop): ")
    while grade != "":
        if int(grade) >= 0 and int(grade) <= 20:
            grades.append(int(grade))
        grade = input("Enter a grade (empty to stop): ")
    return grades


def stats(grades):
    """
    Calculate the number of grades, the average note, the lowest and the highest from grades
    """
    return len(grades), round(sum(grades) / len(grades), 1), min(grades), max(grades)


if __name__ == '__main__':
    grades = ask_for_grades()
    count, average, lowest, highest = stats(grades)
    print(f"{count} grades", f"average: {average}", f"lowest: {lowest}", f"highest: {highest}", sep=" - ")
