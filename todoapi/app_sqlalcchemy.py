import logging

from flask import Flask, jsonify
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
def findall():
    results = [\
        {"id":item.id, "title":item.title,\
         "description":item.description} for item in Todo.query.all()]
    logging.info(f"number of todos : {len(results)}")
    return jsonify(results)

app.run(port=8090)


