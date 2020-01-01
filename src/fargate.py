import json
from flask import Flask, request, abort, make_response, jsonify
from flask_cors import CORS

import common

app = Flask(__name__)
CORS(app)


def response(status_code=None, body=None):
    print("creating response with:", status_code, body)
    if status_code != 200:
        resp = make_response(
            json.dumps(body) or 'Unknown exception',
            status_code or 500
        )

    else:
        resp = make_response(json.dumps(body), 200)

    resp.headers['Content-Type'] = "application/json"
    return resp


@app.route('/', methods=['GET'])
def health_check():
    return make_response("OK", 200)


@app.route('/blog', methods=['GET', 'POST'])
def blogs():
    if request.method == 'GET':
        return response(*common.get_all())
    else:
        body = request.json
        return response(*common.post(body))


@app.route('/blog/<id>', methods=['GET', 'DELETE'])
def blog(id):
    if request.method == 'GET':
        return response(*common.get(id))
    else:
        return response(*common.delete(id))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)

