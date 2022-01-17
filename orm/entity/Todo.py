from sqlalchemy import Column, Integer, String
from orm.config import Base

class Todo(Base):
    __tablename__ = "todo"

    id = Column("id", Integer, primary_key=True)
    title = Column("title", String(50), nullable=False)
    description = Column("description", String(255), nullable=False)

    def __init__(self, title, description):
        self.id = None
        self.title = title
        self.description = description

    def __repr__(self):
        return "<Todo(id='%s', title='%s', description'%s')>" % (
            self.id, self.title, self.description)
