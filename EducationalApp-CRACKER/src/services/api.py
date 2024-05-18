# services/api.py

from flask import Flask, jsonify

app = Flask(__name__)

''''''
@app.route('/api', methods=['GET'])
def get_api():
    """

    :return:
    """
    return jsonify({'message': 'Hello from API'}), 200


def run_api():
    """

    :return:
    """
    app.run(debug=True)
