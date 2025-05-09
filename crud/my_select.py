from sqlalchemy import func, desc
from database.connect import session
from models.public import Student, Grade, Subject, Group


def select_1():
    result = (
        session.query(Student.first_name, Student.last_name, func.round(func.avg(Grade.grade), 2).label('average_grade'))
        .join(Grade)
        .group_by(Student.id)
        .order_by(desc('average_grade'))
        .limit(5)
        .all()
    )
    return result


def select_2(subject_id: int):
    result = (
        session.query(Student.first_name, Student.last_name, func.round(func.avg(Grade.grade), 2).label('average_grade'))
        .join(Grade)
        .filter(Grade.subject_id == subject_id)
        .group_by(Student.id)
        .order_by(desc('average_grade'))
        .first()
    )
    return result


def select_3(subject_id: int):
    result = (
        session.query(Group.name, func.round(func.avg(Grade.grade), 2).label('average_grade'))
        .select_from(Student)
        .join(Group, Student.group)
        .join(Grade, Grade.student_id == Student.id)
        .filter(Grade.subject_id == subject_id)
        .group_by(Group.id)
        .all()
    )
    return result


def select_4():
    result = session.query(func.round(func.avg(Grade.grade), 2)).scalar()
    return result


def select_5(teacher_id: int):
    result = (
        session.query(Subject.name)
        .filter(Subject.teacher_id == teacher_id)
        .all()
    )
    return result


def select_6(group_id: int):
    result = (
        session.query(Student.first_name, Student.last_name)
        .filter(Student.group_id == group_id)
        .all()
    )
    return result


def select_7(group_id: int, subject_id: int):
    result = (
        session.query(Student.first_name, Student.last_name, Grade.grade)
        .join(Grade)
        .filter(Student.group_id == group_id, Grade.subject_id == subject_id)
        .all()
    )
    return result


def select_8(teacher_id: int):
    result = (
        session.query(func.round(func.avg(Grade.grade), 2))
        .filter(Grade.teacher_id == teacher_id)
        .scalar()
    )
    return result


def select_9(student_id: int):
    result = (
        session.query(Subject.name)
        .join(Grade)
        .filter(Grade.student_id == student_id)
        .group_by(Subject.name)
        .all()
    )
    return result


def select_10(student_id: int, teacher_id: int):
    result = (
        session.query(Subject.name)
        .join(Grade)
        .filter(Grade.student_id == student_id, Grade.teacher_id == teacher_id)
        .group_by(Subject.name)
        .all()
    )
    return result
