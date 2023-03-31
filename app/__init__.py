from flask import Flask
from decouple import config

app = Flask(__name__)
app.config['SECRET_KEY'] = config("SECRET_KEY")
app.config['UPLOAD_FOLDER'] = 'media/files'

import os
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

from . import main
