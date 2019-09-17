from flask import Flask


app = Flask(__name__,
    static_folder='./static',
    template_folder='./public')

import templates.server.views

