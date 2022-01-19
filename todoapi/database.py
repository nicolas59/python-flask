from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite+pysqlite:///test.db',  echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import models
    ## Chargement du fichier d'initialisation de la bdd
    with open("../database/init.sql") as data:
        scripts = "".join(data.readlines())
        with engine.connect() as conn:
            conn.execute(text(scripts))

    with open("../database/data.sql") as data:
        with engine.connect() as conn:
            for query in data:
                conn.execute(text(query))
