from sqlalchemy import String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

DATABASE_URL = "sqlite:///" + "db.sqlite3"
engine = create_engine(DATABASE_URL, echo=True)

class Base(DeclarativeBase):
    pass

class Users(Base):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(12))
    password: Mapped[str] = mapped_column(String(12))
    create_at: Mapped[str] = mapped_column(String(30))

    def __repr__(self) -> str:
        
        return f"Users(id={self.id!r}, username={self.username!r}, password={self.password!r}, create_at={self.create_at!r})"

class Persons(Base):

    __tablename__ = "persons"

    id: Mapped[int] = mapped_column(primary_key=True)
    dni: Mapped[str] = mapped_column(String(8))
    paterno: Mapped[str] = mapped_column(String(20))
    materno: Mapped[str] = mapped_column(String(20))
    nombre: Mapped[str] = mapped_column(String(30))
    nacimiento: Mapped[str] = mapped_column(String(10))
    create_at: Mapped[str] = mapped_column(String(30))

    def __repr__(self) -> str:
                
        return f"""Persons(id={self.id!r}, dni={self.dni!r}, paterno={self.paterno!r}, materno={self.materno!r}, nombre={self.nombre!r}, nacimiento={self.nacimiento!r}, create_at={self.create_at!r})"""

Base.metadata.create_all(engine)
session = Session(engine)