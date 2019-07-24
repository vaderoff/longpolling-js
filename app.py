from flask import render_template, Flask, json
from datetime import datetime
from time import sleep

app = Flask(__name__)


@app.route('/api')
def api():
    data = {'resp': datetime.now()}
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/t')
def test():
    sleep(5)
    return 'OK'


if __name__ == '__main__':
    app.run(port=8080)
