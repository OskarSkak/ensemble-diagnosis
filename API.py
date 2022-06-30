import json

from flask import Flask, jsonify, request, send_file
from classifier import Classifier

from db.models import get_all_reports, save_finalized_report, save_finalized_report_rad, save_image, save_initial_report

from flask_cors import CORS, cross_origin

from diagnosis_helper import get_class_ISIC, get_class_rad, get_description_ISIC, get_level_of_concern_ISIC, get_recommended_course_of_action_ISIC

import PIL.Image

app = Flask(__name__)

classifier = Classifier()

CORS(app, origins=['*'])


@app.route("/report/ISIC/generate", methods=["POST"])
@cross_origin()
def generate_report():
    image = request.files['image']
    if image is None:
        return jsonify('ERROR: NO IMAGE PROVIDED')
    
    name = request.args.get('name')
    age = request.args.get('age')
    sex = request.args.get('sex')
    patient_message = request.args.get('patient_message')
    

    identified_class, probability = classifier.classify_ISIC(image)
    identified_class = int(identified_class)
    probability = float(probability)
    path = save_image(image, name)
    # lime_path = classifier.lime(image, name)

    inspection = 'No' if get_level_of_concern_ISIC(identified_class) == 'low' else 'Yes'

    report = {
        'name': name,
        'age': age,
        'sex': sex,
        'patient_message': patient_message,
        'class_code': identified_class,
        'aut_desc': get_description_ISIC(identified_class),
        'aut_course_action': get_recommended_course_of_action_ISIC(identified_class),
        'aut_concern': get_level_of_concern_ISIC(identified_class),
        'img_path': path,
        'identified_class': identified_class,
        'dataset': 'ISIC',
        'aut_diagnosis': get_class_ISIC(identified_class),
        'confidence': probability,
        'aut_inspection': inspection,
        # 'xai_image': lime_path
    }

    save_initial_report(report)

    return jsonify(report)


@app.route("/report/ISIC", methods=["POST"])
@cross_origin()
def save_final():
    args = {
        'cust_evaluated': request.args.get('cust_evaluated'),
        'cust_diagnosis': request.args.get('cust_diagnosis'),
        'cust_concern': request.args.get('cust_concern'),
        'cust_inspection': request.args.get('cust_inspection'),
        'cust_description': request.args.get('cust_description'),
        'name': request.args.get('name'),
        'request_id': request.args.get('request_id'),
        'user_id': request.args.get('user_id'),
        'cust_course_of_action': request.args.get('cust_course_of_action')
    }

    save_finalized_report(args)
    return 'OK'


@app.route("/report/rad", methods=["POST"])
@cross_origin()
def save_final_rad():
    args = {
        'cust_evaluated': request.args.get('cust_evaluated'),
        'cust_diagnosis': request.args.get('cust_diagnosis'),
        'request_id': request.args.get('request_id'),
        'user_id': request.args.get('user_id')
    }
    save_finalized_report_rad(args)
    return 'OK'


@app.route("/report/", methods=["GET"])
@cross_origin()
def get_reports():
    dataset = request.args.get('dataset')
    all = get_all_reports(dataset)
    return jsonify(all)


@app.route("/report/rad/generate", methods=["POST"])
@cross_origin()
def generate_rad_report():
    image = request.files['image']
    if image is None:
        return jsonify('ERROR: NO IMAGE PROVIDED')
    
    name = request.args.get('name')
    age = request.args.get('age')
    sex = request.args.get('sex')
    patient_message = request.args.get('patient_message')

    identified_class, prob = classifier.classify_rad(image)

    identified_class = int(identified_class)
    prob = float(prob)

    path = save_image(image, name)

    report = {
        'name': name,
        'age': age,
        'sex': sex,
        'patient_message': patient_message,
        'class_code': identified_class,
        'aut_desc': '',
        'aut_course_action': '',
        'aut_concern': '',
        'img_path': path,
        'identified_class': identified_class,
        'dataset': 'rad',
        'xai_image': './',
        'confidence': prob,
        'inspection': '',
        'aut_diagnosis': get_class_rad(identified_class),
        'aut_inspection': None
    }

    save_initial_report(report)

    return jsonify(report)


@app.route("/image", methods=["GET"])
@cross_origin()
def get_image():
    path = request.args.get('path')
    img = PIL.Image.open(path)
    return send_file(path)


if __name__ == '__main__':
    app.run()
  