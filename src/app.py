from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)
now = datetime.datetime.now()

@app.route('/api/v1/details')


def details():
    return jsonify ({
        'message': ' hello world how are   you all :) Yo',
        'time': now,
        'hostname': socket.gethostname()
    }

    )



@app.route('/api/v1/healthz')

def health():
    return jsonify ({
        'status': 'UP'
    }
    ), 200

if __name__ == '__main__':

    app.run(host="0.0.0.0")


