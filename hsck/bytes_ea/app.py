from flask import Flask, request, jsonify

from hsck.ports import BYTES_EXTERNAL_ADAPTER_PORT

app = Flask(__name__)


@app.before_request
def log_request_info():
    app.logger.debug('Headers: %s', request.headers)
    app.logger.debug('Body: %s', request.get_data())


@app.route('/', methods=['POST'])
def call_adapter():
    data = request.get_json()
    if data == '':
        data = {}

    result = {'hex_number': '0x12345678ABCDEF'}
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=BYTES_EXTERNAL_ADAPTER_PORT, threaded=True)
