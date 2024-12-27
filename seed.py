from faker import Faker
from sqlalchemy.orm import Session
from models import Student, Group, Teacher, Subject, Grade
from database import engine, Base

faker = Faker()

def seed_data():
    Base.metadata.create_all(bind=engine)
    with Session(engine) as session:
        # Створення груп
        groups = [Group(name=faker.word()) for _ in range(3)]
        session.add_all(groups)
        session.commit()

        # Створення студентів
        students = [Student(name=faker.name(), group_id=faker.random.choice(groups).id) for _ in range(50)]
        session.add_all(students)
        session.commit()

        # Створення викладачів
        teachers = [Teacher(name=faker.name()) for _ in range(5)]
        session.add_all(teachers)
        session.commit()

        # Створення предметів
        subjects = [Subject(name=faker.word(), teacher_id=faker.random.choice(teachers).id) for _ in range(8)]
        session.add_all(subjects)
        session.commit()

        # Створення оцінок
        grades = [
            Grade(
                student_id=faker.random.choice(students).id,
                subject_id=faker.random.choice(subjects).id,
                grade=faker.random.randint(1, 5),
                date_received=faker.date_this_year(),
            )
            for _ in range(1000)
        ]
        session.add_all(grades)
        session.commit()

if __name__ == "__main__":
    seed_data()
