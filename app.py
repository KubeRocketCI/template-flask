"""Example of flask main file."""
from flask import Flask
app = Flask(__name__)


@app.route('/api/hello')
def hello_world():
    """Returns Hello, World."""
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()
