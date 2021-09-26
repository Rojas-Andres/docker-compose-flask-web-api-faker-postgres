from flask import Flask, render_template, request, redirect, url_for
import requests
import json
app = Flask(__name__)


@app.route('/')
def hola():
    url = 'http://api-service/'
    response = requests.get(url)
    response_json = json.loads(response.text)
    print(response_json)
    return render_template('index.html', reciba=response_json)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80, debug=True)
