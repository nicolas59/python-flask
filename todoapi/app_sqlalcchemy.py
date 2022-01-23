import logging

import flask
from flask import Flask, jsonify, abort, request, make_response, render_template
from todoapi.database import db_session, init_db
from models import Todo

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

init_db()

@app.teardown_appcontext
def shutdown_session(exception=None):
    logging.info("closing the current session")
    db_session.remove()

@app.route("/api/todos")
def find_all():
    results = [\
        {"id":item.id, "title":item.title,\
         "description":item.description} for item in Todo.query.all()]
    logging.info(f"number of todos : {len(results)}")
    return jsonify(results)

@app.route("/api/todos/<int:id>")
def find_todo_by_id(id):
    try:
        todo = Todo.query.filter(Todo.id == id).one()
        return jsonify({"id": todo.id, "title": todo.title, "description": todo.description})
    except:
        abort(404)


@app.route("/api/todos", methods=["POST"])
def create_todo():
    if request.is_json:
        data = request.get_json()
        if "title" in data and "description" in data:
            todo = Todo(data["title"], data["description"])
            db_session().add(todo)
            db_session().commit()
            return flask.Response(headers = {"Location": f"/api/todos/{todo.id}"}, status=201)
        else:
            abort(400, "title or description must be not blank")
    else:
        abort(400, "content type must be application/json")

@app.route("/")
def home():
    todos = Todo.query.all()
    return render_template("todo.html", todos=todos)

app.run(port=8091, debug=True)
