import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/sum', methods=['POST'])
def sum_numbers():
    data = request.json
    numbers = data.get('numbers', [])
    result = sum(numbers)
    return jsonify({'result': result})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
