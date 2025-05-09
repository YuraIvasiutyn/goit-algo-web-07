import faker

from database.connect import session
from models import public


def generate_and_insert_fake_data():
    NUMBER_STUDENTS = 30
    NUMBER_TEACHERS = 4
    NUMBER_GRADES = 20

    fake_data = faker.Faker()

    fake_groups = ['Група А', 'Група Б', 'Група В']
    groups = [public.Group(name=name) for name in fake_groups]
    session.add_all(groups)
    session.flush()

    teachers = [public.Teacher(first_name=fake_data.first_name(),
                               last_name=fake_data.last_name())
                for _ in range(NUMBER_TEACHERS)]
    session.add_all(teachers)
    session.flush()

    subjects = [
        public.Subject(name='Математика', teacher_id=teachers[0].id),
        public.Subject(name='Фізика', teacher_id=teachers[1].id),
        public.Subject(name='Хімія', teacher_id=teachers[2].id),
        public.Subject(name='Історія', teacher_id=teachers[3].id),
        public.Subject(name='Біологія', teacher_id=teachers[0].id),
        public.Subject(name='Література', teacher_id=teachers[1].id),
    ]
    session.add_all(subjects)
    session.flush()

    students = [
        public.Student(
            first_name=fake_data.first_name(),
            last_name=fake_data.last_name(),
            group_id=fake_data.random_element(elements=[g.id for g in groups])
        )
        for _ in range(NUMBER_STUDENTS)
    ]
    session.add_all(students)
    session.flush()

    grades = []
    for student in students:
        for _ in range(NUMBER_GRADES):
            grades.append(
                public.Grade(
                    grade=fake_data.random_int(min=1, max=12),
                    student_id=student.id,
                    subject_id=fake_data.random_element(elements=[s.id for s in subjects]),
                    teacher_id=fake_data.random_element(elements=[t.id for t in teachers]),
                )
            )
    session.add_all(grades)

    session.commit()
    print("Дані додано до таблиць")