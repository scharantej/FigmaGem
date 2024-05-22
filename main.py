
from flask import Flask, render_template, request, jsonify
import requests
import os
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.get_json()['message']
    response = requests.post('https://api.figma.com/v1/files/FILE_ID/messages', json={'message': message}, headers={'Authorization': 'Bearer ' + os.environ['FIGMA_TOKEN']})
    return jsonify(response.json())

@app.route('/get_messages')
def get_messages():
    response = requests.get('https://api.figma.com/v1/files/FILE_ID/messages', headers={'Authorization': 'Bearer ' + os.environ['FIGMA_TOKEN']})
    return jsonify(response.json())

@app.route('/refresh_figma')
def refresh_figma():
    response = requests.get('https://api.figma.com/v1/files/FILE_ID', headers={'Authorization': 'Bearer ' + os.environ['FIGMA_TOKEN']})
    return jsonify(response.json())

@app.route('/apply_changes', methods=['POST'])
def apply_changes():
    changes = request.get_json()['changes']
    encoded_changes = base64.b64encode(changes.encode('utf-8')).decode('utf-8')
    response = requests.put('https://api.figma.com/v1/files/FILE_ID', json={'changes': encoded_changes}, headers={'Authorization': 'Bearer ' + os.environ['FIGMA_TOKEN']})
    return jsonify(response.json())

if __name__ == '__main__':
    app.run()
