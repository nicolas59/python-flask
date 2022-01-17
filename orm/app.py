from config import SessionFactory
from sqlalchemy import select, or_, not_
from entity import Todo

def displayTodos():
    with SessionFactory() as session:
        result = session.query(Todo).all()
        for item in result:
            print(item)

with SessionFactory() as session:
    result = session.query(Todo).all()
    for item in result:
        print(item)

    result = session.query(Todo).filter(Todo.title == "TODO 1").one()
    print(result)

    result = session.query(Todo).filter(Todo.description.like("%cours%")).all()
    for item in result:
        print(item)

    result = session.query(Todo)\
        .filter(or_(Todo.description.like("%cours%"), Todo.description.like("%python%")))\
        .filter(not_(Todo.id == 1))\
        .all()
    for item in result:
        print(item)

with SessionFactory() as session:
    todo = Todo("Flask - Jinja", "decrire le template JinJa2")
    print(f"id : {todo.id}, Title : {todo.title}")
    session.add(todo)
    session.commit()
    print(f"id : {todo.id}, Title : {todo.title}")

displayTodos()

with SessionFactory() as session:
    todo = session.query(Todo).order_by(Todo.id.desc()).first()
    print(todo)
    todo.title="Flask - Jinja2"
    session.commit()

displayTodos()






