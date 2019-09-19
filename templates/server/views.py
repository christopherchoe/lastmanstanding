#!/usr/bin/env python3
from flask import render_template, Blueprint


lms_blueprint = Blueprint('lms', __name__)

@app.route('/')
def index():
    return render_template('index.html')
