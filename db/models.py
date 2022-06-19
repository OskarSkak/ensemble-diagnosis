from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Boolean, Column, Integer, String, Date, Float, ForeignKey, Text
from sqlalchemy.orm import relationship
from .conf import DATABASE_URI
from PIL import Image

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


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    sex = Column(String)
    age = Column(Integer)


class Diagnosis(Base):
    __tablename__ = 'diagnosis'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)
    recommended_action = Column(Text)
    concern = Column(String)
    code = Column(Integer)


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
# session = create_engine(DATABASE_URI)

def get_session():
    Session = sessionmaker(bind=engine)
    s = Session()
    return s


def save_report(report: Report):
    s = get_session()
    s.add(report)
    s.commit()


def save_image(img, name):
    loc = Image.open(img)
    path = f'./images/{name}.jpg'
    loc.save(path)
    return path

def get_all_reports(dataset = 'ISIC'):
    s = get_session()
    return s.query(Report).filter(Report.dataset == dataset).all()


def get_user(id: int):
    s = get_session()
    return s.query(User).filter(User.id == id).first()


def save_initial_report(request):
    name = request['name'],
    age = request['age'],
    sex = request['sex'],
    patient_message = request['patient_message'],
    class_code = request['identified_class'],
    aut_desc = request['aut_desc'],
    aut_course_action = request['aut_course_action'],
    aut_concern = request['aut_concern'],
    img_path = request['img_path']
    dataset = request['dataset']
    xai_image = request['xai_image']

    s = get_session()
    
    report = Report()
    user = s.query(User).filter(User.name == name).first()
    if user is None:
        user = User()
        user.age = age
        user.name = name
        user.sex = sex
        s.add(user)
    
    report.user_id = user.id
    report.age = age
    report.aut_concern = aut_concern
    report.request_text = patient_message
    report.aut_diagnosis = str(class_code)
    report.aut_description = aut_desc
    report.request_image = img_path
    report.dataset = dataset
    report.xai_image = xai_image
    s.add(report)

    s.commit()


def save_finalized_report(request):
    cust_evaluated = request['cust_evaluated']
    cust_diagnosis = request['cust_diagnosis']
    cust_concern = request['cust_concern']
    cust_inspection = request['cust_inspection']
    cust_description = request['cust_description']
    name = request['name']
    request_id = request['request_id']
    user_id = request['user_id']

    s = get_session()
    report: Report = s.query(Report).filter(Report.id == request_id).one()
    report.cust_evaluated = cust_evaluated
    report.cust_diagnosis = cust_diagnosis
    report.cust_concern = cust_concern
    report.cust_inspection = cust_inspection
    report.cust_description = cust_description
    report.user_id = user_id

    s.commit()


def save_finalized_report_rad(request):
    cust_evaluated = request['cust_evaluated']
    cust_diagnosis = request['cust_diagnosis']
    request_id = request['request_id']
    user_id = request['user_id']

    s = get_session()
    report: Report = s.query(Report).filter(Report.id == request_id).one()
    report.cust_evaluated = cust_evaluated
    report.cust_diagnosis = cust_diagnosis
    report.user_id = user_id

    s.commit()
