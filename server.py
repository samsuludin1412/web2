from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

API_URL = 'https://explorer.theqrl.org/api/miningstats'

@app.route('/api/miningstats', methods=['GET'])
def mining_stats():
    try:
        response = requests.get(API_URL)
        data = response.json()
        return jsonify(data)
    except Exception as e:
        print('Error fetching data:', e)
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)

