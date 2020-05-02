from flask import Flask, request
import dao
import json
from db import db

app = Flask(__name__)
db_filename = "cms.db"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)
with app.app_context():
    db.create_all()

@app.route("/")
def hello_world():
    return "Hello world!"

def success_response(data, code=200):
    return json.dumps({"success": True, "data": data}), code

def failure_response(message, code=404):
    return json.dumps({"success": False, "error": message}), code

@app.route("/api/courses/", methods=['GET'])
def get_courses():
    return success_response(dao.get_all_courses())

@app.route("/api/courses/", methods=['POST'])
def make_course():
    body = json.loads(request.data)
    code = body["code"]
    name = body["name"]
    course = dao.create_course(code, name)
    return success_response(course)

@app.route("/api/courses/<int:course_id>/", methods=['GET'])
def get_course_by_id(course_id):
    course = dao.get_course_by_id(course_id)
    if course is not None:
        return success_response(course.serialize())
    return failure_response("that course does not exist!")

@app.route("/api/courses/<int:course_id>/", methods=['DELETE'])
def delete_course_by_id(course_id):
    course = dao.delete_course_by_id(course_id)
    if course is not None:
        return success_response(course)
    return failure_response("that course does not exist!")

@app.route("/api/users/", methods=['POST'])
def make_user():
    body = json.loads(request.data)
    name = body["name"]
    netid = body["netid"]
    course = dao.create_user(name, netid)
    return success_response(course)

@app.route("/api/users/<int:user_id>/", methods=['GET'])
def get_user_by_id(user_id):
    user = dao.get_user_by_id(user_id)
    if user is not None:
        return success_response(user.serialized())
    return failure_response("that user does not exist!")

@app.route("/api/courses/<int:course_id>/add/", methods=['POST'])
def add_user_to_course(course_id):
    body = json.loads(request.data)
    user_id = body["user_id"]
    type = body["type"]
    user = dao.add_user(course_id,user_id,type)
    if user is not None:
        return success_response(user)
    return failure_response("that user or course does not exist!")

@app.route("/api/courses/<int:course_id>/assignment/", methods=['POST'])
def add_assignment_to_course(course_id):
    body = json.loads(request.data)
    title = body["title"]
    due_date = body["due_date"]
    assign = dao.add_assignment(course_id,title,due_date)
    if assign is not None:
        return success_response(assign.serialize())
    return failure_response("that course does not exist!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
