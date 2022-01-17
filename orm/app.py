from config import SessionFactory
from sqlalchemy import select, or_, not_
from entity import Todo

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