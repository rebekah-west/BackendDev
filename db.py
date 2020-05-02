from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import dao


db = SQLAlchemy()

# many to many

instructor_asso = db.Table("instructor_asso", db.Model.metadata,
    db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
    db.Column("course_id", db.Integer, db.ForeignKey("courses.id"))
)

student_asso = db.Table("student_asso", db.Model.metadata,
    db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
    db.Column("course_id", db.Integer, db.ForeignKey("courses.id"))
)

class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    assignments = db.relationship("Assignment", cascade="delete")
    instructors = db.relationship('User', secondary = instructor_asso, back_populates='courses_inst')
    students = db.relationship('User', secondary = student_asso, back_populates='courses_stud')

    def __init__(self, **kwargs):
        self.code = kwargs.get('code','')
        self.name = kwargs.get('name','')
        self.assignments = []
        self.instructors = []
        self.students = []

    def serialize(self):
        return {
            "id": self.id,
            "code": self.code,
            "name": self.name,
            "assignments": [a.serialize() for a in self.assignments],
            "instructors": [i.serialize() for i in self.instructors],
            "students": [s.serialize() for s in self.students]
        }

    def serialized(self):
        return {
            "id": self.id,
            "code": self.code,
            "name": self.name
        }

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    netid = db.Column(db.String, nullable=False)
    courses_stud = db.relationship('Course', secondary = student_asso, back_populates = 'students')
    courses_inst = db.relationship('Course', secondary = instructor_asso, back_populates='instructors')

    def __init__(self, **kwargs):
        self.name = kwargs.get('name','')
        self.netid = kwargs.get('netid','')
        self.courses_stud = []
        self.courses_inst = []

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "netid": self.netid,
        }

    def serialized(self):
        courses = []
        for c in self.courses_inst:
            courses.append(c.serialize())
        for i in self.courses_stud:
            courses.append(i.serialize())

        return {
            "id": self.id,
            "name": self.name,
            "netid": self.netid,
            "courses": courses
        }

class Assignment(db.Model):
    __tablename__ = 'assignments'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    due_date = db.Column(db.Integer, nullable=False)
    course = db.Column(db.Integer, db.ForeignKey("courses.id"), nullable=False)

    def __init__(self, **kwargs):
        self.title = kwargs.get('title','')
        self.due_date = kwargs.get('due_date','')
        self.course = kwargs.get('course', '')

    def serialize(self):
        course_ser = dao.get_course_by_id(self.course).serialized()
        return {
            "id": self.id,
            "title": self.title,
            "due_date": self.due_date,
            "course": course_ser
        }
