from app import app
from flask import render_template
import json

@app.route('/')
def index():
    filepath = 'app/laptop.json'
    with open(filepath) as f:
        datas = json.loads(f.read())

    return render_template('pages/index.html', title='ECatalog', datas=datas)


@app.route('/detail/<id>')
def detail(id):
    filepath = 'app/laptop.json'
    with open(filepath) as f:
        datas = json.loads(f.read())
        data = datas[int(id)]

    return render_template('pages/detail.html', title='Product Information', data=data, datas=datas)