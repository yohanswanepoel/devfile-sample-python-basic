from flask import Flask
from flask import render_template
import os

app = Flask(__name__)

@app.route('/')
def hello():
    message = "Hello, World"
    return render_template('index.html', 
                           message=message)

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')