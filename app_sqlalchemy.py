from sqlalchemy import create_engine, text

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)


with engine.connect() as conn:
    conn.execute(text("""
    create table if not exists todo (
        id integer primary key autoincrement,
        title varchar(50) not null,
        description  varchar(255)
    )
    """))
    conn.commit()

todos = [
    {"title": "TODO 1", "description": "Prepartion cours Java"},
    {"title": "TODO 2", "description": "Prepartion cours Python"},
    {"title": "TODO 3", "description": "Faire une pause"}
]
with engine.connect() as conn:
    # Intialisation des données.
    conn.execute(text("insert into todo(title, description)values(:title, :description)"), todos)
    conn.commit()

with engine.connect() as conn:
    result = conn.execute(text("select id, title, description from todo"))
    for row in result:
        print(f"id : {row.id}, title : {row.title}, description:{row.description}", row)

with engine.connect() as conn:
    result = conn.execute(text("select id, title, description from todo"))
    for row in result:
        print(f"id : {row.id}, title : {row.title}, description:{row.description}", row)

with engine.connect() as conn:
    result = conn.execute(text("select id, title, description from todo"))
    for row in result:
        print(f"id : {row[0]}, title : {row[1]}, description:{row[2]}", row)

with engine.connect() as conn:
    result = conn.execute(text("select id, title, description from todo"))
    for id, title, description  in result:
        print(f"id : {id}, title : {title}, description:{description}", row)

with engine.connect() as conn:
    result = conn.execute(text("select id, title, description from todo"))
    for dict_row  in result.mappings():
        print(f"id : {dict_row['id']}, title : {dict_row['title']}, description:{dict_row['description']}", row)