from flask import Flask, request, jsonify

from hsck.crypto_compare_ea.adapter import Adapter
from hsck.ports import CRYPTO_COMPARE_EXTERNAL_ADAPTER_PORT

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
    adapter = Adapter(data)
    return jsonify(adapter.result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=CRYPTO_COMPARE_EXTERNAL_ADAPTER_PORT, threaded=True)
