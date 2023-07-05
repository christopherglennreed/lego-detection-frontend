from flask import Flask, render_template, request, jsonify
import requests
import base64
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api', methods=['POST'])
def send_image():
    data = request.get_json()
    image_data = data['image']

    # Convert to base64
    decoded_image = base64.b64decode(image_data)

    # Your API endpoint
    MY_ROUTE = 'http://object-detection-rest-legodetect.apps.cp4i-dtc2-3.sadtc.tdsynnex.com/predictions'

    headers = {'Content-Type': 'application/json'}
    data = {"image": image_data}

    response = requests.post(MY_ROUTE, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        api_data = response.json()
    else:
        api_data = None

    return jsonify({'status': 'image sent', 'api_data': api_data}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
