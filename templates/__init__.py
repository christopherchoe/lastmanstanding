from flask import Flask


app = Flask(__name__,
    static_folder='./public',
    template_folder='./static')

from templates.server.views import lms_blueprint

app.register_blueprint(lms_blueprint)
