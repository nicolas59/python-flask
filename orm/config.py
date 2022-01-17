from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

## Chargement du fichier d'initialisation de la bdd
with open("../database/init.sql") as data:
    scripts = "".join(data.readlines())
    with engine.connect() as conn:
        conn.execute(text(scripts))
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