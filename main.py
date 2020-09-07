import os
from os.path import isfile, join, splitext
from flask import Flask, escape, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
UPLOAD_FOLDER = os.environ['UPLOAD_FOLDER']


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def gallery():
    images = [splitext(f) for f in os.listdir(UPLOAD_FOLDER) if isfile(
        join(UPLOAD_FOLDER, f)
    )]
    return render_template('gallery.html.j2', images=images)


@app.route('/pic', methods=['POST'])
def pic():
    if 'file' not in request.files:
        #flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        #flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('gallery'))
