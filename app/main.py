from . import app
from flask import render_template, request, send_from_directory
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename
import os
from datetime import datetime


class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[DataRequired(), ])
    submit = SubmitField("Upload File")


@app.route('/', methods=["GET", "POST"])
def index():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        filename = secure_filename(file.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        print(path)
        start_time = datetime.now()
        file.save(path)
        elpased_time = (datetime.now() - start_time).total_seconds()
        return render_template('uploaded.html', filename=filename, elpased_time=elpased_time)
    return render_template('index.html', form=form)


@app.route('/file/<filename>')
def download(filename):
    return send_from_directory(directory=app.config['UPLOAD_FOLDER'], path=filename)
