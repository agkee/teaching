from flask import Flask, request, json, send_file, make_response
from PIL import Image
import base64
from io import BytesIO
from flask_cors import CORS
from convert import convert

# create an instance of a Flask class
# First argument is the name of the application's module or package
app = Flask(__name__)
CORS(app)


@app.route('/test', methods=['GET', 'POST'])
# Set router for the url
def hello_world():
    a = {}
    a["ha"] = "huh"
    a["ha2"] = "huh2"

    # resp = flask.Response("")
    # response = json.dumps(a)

    return a


@app.route('/upload', methods=['POST', 'OPTIONS'])
def upload():
    f = request.files['file']
    img = Image.open(f)

    img = convert(img)

    img_io = BytesIO()
    img.save(img_io, 'jpeg')
    img_io.seek(0)

    # response = make_response(send_file(img_io, mimetype='image/jpeg'))
    response = make_response(send_file(img_io, mimetype='image/jpeg'))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response
