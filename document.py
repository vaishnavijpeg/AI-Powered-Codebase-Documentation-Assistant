from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True)
    file_path = Column(String)
    content = Column(Text)
