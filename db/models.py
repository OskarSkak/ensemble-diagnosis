from requests import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Boolean, Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from .conf import DATABASE_URI

Base = declarative_base()

class Report(Base):
    __tablename__ = 'report'
    id = Column(Integer, primary_key=True)
    request_text = Column(String)
    request_image = Column(String)
    xai_image = Column(String)
    sex = Column(String)
    age = Column(Integer)
    aut_diagnosis = Column(String)
    confidence = Column(Float)
    historic_confidence = Column(Float)
    aut_concern = Column(String)
    aut_inspection = Column(String)
    generated = Column(Boolean)
    aut_description = Column(String)

    cust_evaluated = Column(Boolean)
    cust_diagnosis = Column(String)
    cust_concern = Column(String)
    cust_inspection = Column(String)
    cust_description = Column(String)

    dataset = Column(String)
    created = Column(Date)
    resolved = Column(Date)

    user_id = Column(Integer, ForeignKey('report.id'))
    user = relationship("User", back_populates="reports")


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    sex = Column(String)
    age = Column(Integer)
    reports = relationship('Report')



def create_db():
    from sqlalchemy import create_engine
    engine = create_engine(DATABASE_URI)
    Base.metadata.create_all(engine)


def recreate_db():
    from sqlalchemy import create_engine
    engine = create_engine(DATABASE_URI)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(DATABASE_URI)
session = create_engine(bind=engine)

def get_session():
    s = Session()
    return s


def save_report(report: Report):
    s = get_session()
    s.add(report)
    s.commit()


def get_all_reports():
    s = get_session()
    return s.query(Report).all()


def get_user(id: int):
    s = get_session()
    return s.query(User).filter(User.id == id).first()
