from sqlalchemy.orm import Session
from models import Student, Grade, Subject, Teacher, Group
from sqlalchemy import func, desc

def select_1(db: Session):
    return db.query(Student.name, func.avg(Grade.grade).label("average_grade")) \
      .join(Grade) \
      .group_by(Student.name) \
      .order_by(func.avg(Grade.grade).desc()) \
      .limit(5).all()

def select_2(session, subject_id):
    return session.query(
        Student.name,
        func.avg(Grade.grade).label("avg_grade")
    ).join(Grade).filter(Grade.subject_id == subject_id).group_by(Student.id).order_by(desc("avg_grade")).first()

def select_3(session, subject_id):
    return session.query(
        Group.name.label("group_name"),
        func.avg(Grade.grade).label("avg_grade")
    ).join(Student, Student.group_id == Group.id).join(Grade, Grade.student_id == Student.id).filter(
        Grade.subject_id == subject_id
    ).group_by(
        Group.id
    ).all()

def select_4(session):
    return session.query(func.avg(Grade.grade).label("avg_grade")).scalar()

def select_5(session, teacher_id):
    return session.query(
        Subject.name
    ).filter(Subject.teacher_id == teacher_id).all()

def select_6(session, group_id):
    return session.query(
        Student.name
    ).filter(Student.group_id == group_id).all()

def select_7(session, group_id, subject_id):
    return session.query(
        Student.name,
        Grade.grade,
        Grade.date_received
    ).join(Grade).filter(Student.group_id == group_id, Grade.subject_id == subject_id).all()

def select_8(session, teacher_id):
    return session.query(
        func.avg(Grade.grade).label("avg_grade")
    ).join(Subject).filter(Subject.teacher_id == teacher_id).scalar()

def select_9(session, student_id):
    return session.query(
        Subject.name
    ).join(Grade).filter(Grade.student_id == student_id).distinct().all()

def select_10(session, student_id, teacher_id):
    return session.query(
        Subject.name
    ).join(Grade).filter(Grade.student_id == student_id, Subject.teacher_id == teacher_id).distinct().all()
