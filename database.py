from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import sessionmaker


url = "mysql+pymysql://root:Passwordweak@127.0.0.1:3306/college"

engine = create_engine(url)
Base = declarative_base()

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Cars(Base):
    __tablename__ = "Cars"
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    brand = Column(String(200))


Base.metadata.create_all(bind=engine)
