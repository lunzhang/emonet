from flask import Flask, render_template, request, jsonify
from net import analysis
import os

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/analysis', methods=['POST'])
def emotion():
    data = request.get_json()
    result = analysis(data)
    return jsonify(result)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 80))
    host = '0.0.0.0'
    app.run(debug=True, host, port)
