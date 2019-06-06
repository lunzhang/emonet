from flask import Flask, render_template, request, jsonify
from net import analysis

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
    app.run(debug=True, host='0.0.0.0')
