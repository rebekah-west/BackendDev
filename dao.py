from db import db, Course, User, Assignment

# your methods here
def get_all_users():
    return [u.serialize() for u in User.query.all()]

def create_user(name, netid):
    new_user = User(
        name = name,
        netid = netid
    )

    db.session.add(new_user)
    db.session.commit()
    return new_user.serialize()

def get_user_by_id(user_id):
    user=User.query.filter_by(id=user_id).first()
    if user is None:
        return None
    return user


#COURSES

def get_all_courses():
    return [c.serialize() for c in Course.query.all()]

def create_course(code, name):
    new_course = Course(
        code = code,
        name = name
    )

    db.session.add(new_course)
    db.session.commit()
    return new_course.serialize()

def get_course_by_id(course_id):
    course=Course.query.filter_by(id=course_id).first()
    if course is None:
        return None
    return course

def delete_course_by_id(course_id):
    course=Course.query.filter_by(id=course_id).first()
    if course is None:
        return None
    db.session.delete(course)
    db.session.commit()
    return course.serialize()

def add_user(course_id, user_id, type):
    course = get_course_by_id(course_id)
    user = get_user_by_id(user_id)
    if course is None or user is None:
        return None
    if type == "student":
        course.students.append(user)
        user.courses_stud.append(course)
        db.session.commit()
        return course.serialize()
    if type == 'instructor':
        course.instructors.append(user)
        user.courses_inst.append(course)
        db.session.commit()
        return course.serialize()
    return None

def add_assignment(course_id,title,due_date):
    new_assignment = Assignment(
        title = title,
        due_date = due_date,
        course=course_id
    )
    course = get_course_by_id(course_id)
    if course is None:
        return None
    course.assignments.append(new_assignment)
    db.session.commit()
    return new_assignment
