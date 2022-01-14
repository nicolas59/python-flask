import flask
from flask import Flask, request, jsonify, redirect, json, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "hello"

todos = [
    {"id": 1, "titre": "TODO 1", "description": "Prepartion cours Java"},
    {"id": 2, "titre": "TODO 2", "description": "Prepartion cours Python"},
    {"id": 3, "titre": "TODO 3", "description": "Faire une pause"}
]

def printTodo(todo):
    return f"""
        <div>
            <h2>{todo['titre']}</h2>
            <p>{todo['description']}</p> 
        </div>
        """

@app.route(rule="/todos/create", methods=["GET"])
def init_form():
    return """
    <form method="POST">
        <div><label>Titre : </label><input type="text" name="title"/></div>
        <div><label>Description : </label><textarea name="description"></textarea></div>
        <input type="submit" value="Soumettre"/> 
    </form>
    """

@app.route(rule="/todos/create", methods=["POST"])
def create():
    title = request.form.get("title")
    description = request.form.get("description")
    id = sorted(todos, key=lambda it: it["id"])[-1]["id"] + 1
    todos.append({
        "id": id,
        "titre": title,
        "description": description
    })
    return redirect("/todos")

@app.route(rule="/api/todos", methods=["POST"])
def create_with_json():
    data = request.json
    id = sorted(todos, key=lambda it: it["id"])[-1]["id"] + 1
    todos.append({
        "id": id,
        "titre": data["title"],
        "description": data["description"]
    })
    return flask.Response(status=201, headers= {"Location" : f"/todos/{id}"});

@app.route("/todos")
def displayTodos():
    sort_by = request.args.get("sort_by")
    items = todos
    try:
        if sort_by:
            items = sorted(items, key=lambda it: it[sort_by])
    except:
        items = []
    return "".join([printTodo(todo) for todo in items])


@app.route("/todos/<id>")
def getTodo(id):
    result = filter(lambda it: it["id"] == id, todos)
    return "".join([printTodo(todo) for todo in result])

@app.route("/api/todos")
def getTodoApi():
   return jsonify(todos)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
