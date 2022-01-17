from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

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


SessionFactory = sessionmaker(bind=engine)

Base = declarative_base()

"""
def session_factory():
    Base.metadata.create_all(engine)
    return _SessionFactory()
"""