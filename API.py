from flask import Flask, jsonify, request

from db.models import get_all_reports
# from flask_swagger_ui import get_swaggerui_blueprint

# import uuid

# from apispec import APISpec
# from apispec.ext.marshmallow import MarshmallowPlugin
# from apispec_webframeworks.flask import FlaskPlugin
# from marshmallow import Schema, fields
# from flask_apispec.extension import FlaskApiSpec


# # Create an APISpec
# spec = APISpec(
#     title="Ensemble Diagnosis API",
#     version="1.0.0",
#     openapi_version="3.0.2",
#     plugins=[FlaskPlugin(), MarshmallowPlugin()]
# )

# # Optional marshmallow support
# class CategorySchema(Schema):
#     id = fields.Int()
#     name = fields.Str(required=True)


# class PetSchema(Schema):
#     categories = fields.List(fields.Nested(CategorySchema))
#     name = fields.Str()


# # Optional security scheme support
# api_key_scheme = {"type": "apiKey", "in": "header", "name": "X-API-Key"}
# spec.components.security_scheme("ApiKeyAuth", api_key_scheme)


# # Optional Flask support
app = Flask(__name__)

# app.config.update({
#   'APISPEC_SPEC': spec,
#   'APISPEC_SWAGGER_URL': '/swagger/'
# })

# docs = FlaskApiSpec(app)

@app.route("/report/generate", methods=["POST", 'GET'])
def generate_report():
    # """Cat view.
    # ---
    # post:
    #   parameters:
    #   - in: path
    #     schema: CategorySchema
    #   responses:
    #     200:
    #       content:
    #         application/json:
    #           schema: CategorySchema
    # """
    if request.method == 'POST':
        posted_data = request.get_json()
        data = posted_data['data']
        return jsonify(str('class x'))
    if request.method == 'GET':
      return jsonify({'title': 'Ensemble diagnosis', 'method': 'generate report'})


@app.route("/report/", methods=["GET"])
def get_reports():
    if request.method == 'GET':
        return jsonify({'reports': get_all_reports()})


if __name__ == '__main__':
    app.run(debug=True)
  