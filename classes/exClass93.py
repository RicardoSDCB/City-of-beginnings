if __name__ == "__main__":
    student_score = \
        {
            "Harry": 81,
            "Ron": 78,
            "Hermione": 99,
            "Draco": 74,
            "Neville": 62,
        }

    student_grades = {}

    for key in student_score:
        if 91 <= student_score[key] <= 100:
            student_grades[key] = "Outstanding"
        elif 81 <= student_score[key] < 91:
            student_grades[key] = "Exceeds Expectations"
        elif 71 <= student_score[key] < 81:
            student_grades[key] = "Acceptable"
        elif student_score[key] <= 70:
            student_grades[key] = "Fail"

    print(student_grades)
'''
    Regra das grades:
        91-100 = Outstanding
        81-90 = Exceeds Expectations
        71-80 = Acceptable
        70 ou menor = Fail

    Regra de saida de print:
        {'Harry': 'Exceeds Expectations', .......... and so}
'''
