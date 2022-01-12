from flask import Flask
from flask import json
import logging

app = Flask(__name__)

FORMAT = '%(asctime)s %(message)s'
logging.basicConfig(
    level=logging.DEBUG,
    filename='app.log',
    format=FORMAT
)


@app.route('/status')
def status():
    logging.debug('status endpoint was reached')
    response = app.response_class(
        response=json.dumps({"result": "OK - healthy"}),
        status=200,
        mimetype='application/json'
    )

    app.logger.info('Status request successfull')
    return response


@app.route('/metrics')
def metrics():
    logging.debug('metrics endpoint was reached')
    response = app.response_class(
        response=json.dumps({"status": "success", "code": 0, "data": {"UserCount": 140, "UserCountActive": 23}}),
        status=200,
        mimetype='application/json'
    )

    app.logger.info('Metrics request successfull')
    return response


@app.route("/")
def hello():
    logging.debug('root endpoint was reached')
    app.logger.info('Main request successfull')

    return "Hello World!"


if __name__ == "__main__":
    ## stream logs to a file
    logging.basicConfig(filename='app.log', level=logging.DEBUG)

    app.run(host='0.0.0.0')
