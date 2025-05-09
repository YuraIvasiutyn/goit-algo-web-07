from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    group_id = Column(Integer, ForeignKey('groups.id'))
    created_at = Column(DateTime, default=datetime.now())

    group = relationship("Group", back_populates='students')
    grades = relationship("Grade", back_populates='student')


class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    created_at = Column(DateTime, default=datetime.now())

    students = relationship("Student", back_populates="group")


class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    created_at = Column(DateTime, default=datetime.now())

    subjects = relationship("Subject", back_populates="teacher")
    grades = relationship("Grade", back_populates="teacher")


class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    created_at = Column(DateTime, default=datetime.now())

    teacher = relationship("Teacher", back_populates="subjects")
    grades = relationship("Grade", back_populates="subject")


class Grade(Base):
    __tablename__ = 'grades'

    id = Column(Integer, primary_key=True)
    grade = Column(Integer, nullable=False)
    student_id = Column(Integer, ForeignKey("students.id", ondelete="SET NULL"))
    subject_id = Column(Integer, ForeignKey("subjects.id", ondelete="SET NULL"))
    teacher_id = Column(Integer, ForeignKey("teachers.id", ondelete="SET NULL"))
    created_at = Column(DateTime, default=datetime.utcnow)

    student = relationship("Student", back_populates="grades")
    subject = relationship("Subject", back_populates="grades")
    teacher = relationship("Teacher", back_populates="grades")

