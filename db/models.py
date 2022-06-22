from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Boolean, Column, Integer, String, Date, Float, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from .conf import DATABASE_URI
from PIL import Image
import datetime

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
    aut_course_of_action = Column(String)
    aut_class_code = Column(Integer)
    cust_class_code = Column(Integer)

    cust_evaluated = Column(Boolean)
    cust_diagnosis = Column(String)
    cust_concern = Column(String)
    cust_inspection = Column(String)
    cust_description = Column(String)
    cust_course_of_action = Column(String)

    dataset = Column(String)
    created = Column(String)
    resolved = Column(String)

    user_name = Column(String)

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


def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))
    return d


def get_all_reports(dataset = 'ISIC'):
    s = get_session()
    all = s.query(Report).filter(Report.dataset == dataset).all()
    result = [row2dict(row) for row in all]

    return result


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
    # xai_image = request['xai_image']

    aut_diagnosis = request['aut_diagnosis']
    confidence = request['confidence']
    aut_inspection = request['aut_inspection']

    s = get_session()
    
    report = Report()
    user = s.query(User).filter(User.name == name).first()
    if user is None:
        user = User()
        user.age = age
        user.name = name
        user.sex = sex
        s.add(user)
        s.commit()
    
    # report.user_id = user.id
    # report.age = age
    # report.aut_concern = aut_concern
    # report.request_text = patient_message
    # report.aut_diagnosis = str(class_code)
    # report.aut_description = aut_desc
    # report.request_image = img_path
    # report.dataset = dataset
    # report.historic_confidence = 91.07
    # report.xai_image = xai_image

    report.request_text = patient_message
    report.request_image = img_path
    report.xai_image = ''
    report.sex = sex
    report.age = age
    report.aut_diagnosis = aut_diagnosis
    report.confidence = confidence
    report.historic_confidence = 91.07
    report.aut_concern = aut_concern
    report.aut_inspection = aut_inspection
    report.generated = True
    report.aut_description = aut_desc
    report.aut_course_of_action = aut_course_action
    report.cust_evaluated = False
    report.cust_diagnosis = aut_diagnosis
    report.cust_concern = aut_concern
    report.cust_inspection = aut_inspection
    report.cust_description = aut_desc
    report.cust_course_of_action = aut_course_action
    report.dataset = dataset
    today = datetime.datetime.now()
    report.created = today.strftime('%Y/%m/%d')
    report.resolved = 'y' if confidence > 82 else 'n'
    report.user_name = name
    report.user_id = user.id
    report.aut_class_code = class_code
    report.cust_class_code = class_code

    s.add(report)

    s.commit()


def save_finalized_report(request):
    cust_evaluated = True
    cust_diagnosis = request['cust_diagnosis']
    cust_concern = request['cust_concern']
    cust_inspection = request['cust_inspection']
    cust_description = request['cust_description']
    name = request['name']
    request_id = request['request_id']
    user_id = request['user_id']
    cust_course_of_action = request['cust_course_of_action']

    s = get_session()
    report: Report = s.query(Report).filter(Report.id == request_id).one()
    report.cust_evaluated = cust_evaluated
    report.cust_diagnosis = cust_diagnosis
    report.cust_concern = cust_concern
    report.cust_inspection = cust_inspection
    report.cust_description = cust_description
    report.user_id = user_id
    today = datetime.datetime.now()
    report.resolved = today.strftime('%Y/%m/%d')
    report.cust_course_of_action = cust_course_of_action

    s.commit()


def save_finalized_report_rad(request):
    cust_evaluated = True
    cust_diagnosis = request['cust_diagnosis']
    request_id = request['request_id']
    user_id = request['user_id']

    s = get_session()
    report: Report = s.query(Report).filter(Report.id == request_id).one()
    report.cust_evaluated = cust_evaluated
    report.cust_diagnosis = cust_diagnosis
    report.user_id = user_id
    today = datetime.datetime.now()
    report.resolved = today.strftime('%Y/%m/%d')

    s.commit()


if __name__ == '__main__':
    recreate_db()