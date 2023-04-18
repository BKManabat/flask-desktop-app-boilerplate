from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import webview
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(os.path.join(os.getcwd(), 'test.db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(50))

db.create_all()
window = webview.create_window('myapp', app)

@app.route('/')
def index():
    tests = Test.query.all()
    return render_template('index.html', tests=tests)

@app.route('/add_data', methods=['POST'])
def add_data():
    data = request.json['data']
    test = Test(data=data)
    db.session.add(test)
    db.session.commit()
    return jsonify({'message': 'Record added successfully!'})

if __name__ == '__main__':
    webview.start(http_server=True, http_port=3000)

# run `pyinstaller app.spec` to build
