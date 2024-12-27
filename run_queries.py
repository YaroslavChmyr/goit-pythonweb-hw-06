from sqlalchemy.orm import Session
from database import engine
from my_select import (
    select_1,
    select_2,
    select_3,
    select_4,
    select_5,
    select_6,
    select_7,
    select_8,
    select_9,
    select_10
)

def run_queries():
    with Session(engine) as session:
        print("\n1. Top 5 students by average grade:")
        top_students = select_1(session)
        for student, avg_grade in top_students:
            print(f"{student}: {avg_grade:.2f}")

        print("\n2. Student with the highest average grade in a specific subject:")
        subject_id = 1
        best_student_subject = select_2(session, subject_id)
        if best_student_subject:
            print(f"{best_student_subject[0]}: {best_student_subject[1]:.2f}")
        else:
            print("No data available.")

        print("\n3. Average grade for groups in a specific subject:")
        group_grades = select_3(session, subject_id)
        for group, avg_grade in group_grades:
            print(f"{group}: {avg_grade:.2f}")

        print("\n4. Average grade across the entire flow:")
        flow_avg_grade = select_4(session)
        print(f"{flow_avg_grade:.2f}")

        print("\n5. Courses taught by a specific teacher:")
        teacher_id = 1
        courses = select_5(session, teacher_id)
        for course in courses:
            print(course[0])

        print("\n6. List of students in a specific group:")
        group_id = 1
        students = select_6(session, group_id)
        for student in students:
            print(student[0])

        print("\n7. Grades of students in a specific group for a specific subject:")
        grades = select_7(session, group_id, subject_id)
        for student, grade, date in grades:
            print(f"{student}: {grade} (Date: {date})")

        print("\n8. Average grade given by a specific teacher:")
        teacher_avg_grade = select_8(session, teacher_id)
        print(f"{teacher_avg_grade:.2f}")

        print("\n9. Courses attended by a specific student:")
        student_id = 1
        student_courses = select_9(session, student_id)
        for course in student_courses:
            print(course[0])

        print("\n10. Courses taught by a specific teacher to a specific student:")
        teacher_student_courses = select_10(session, student_id, teacher_id)
        for course in teacher_student_courses:
            print(course[0])

if __name__ == "__main__":
    run_queries()

