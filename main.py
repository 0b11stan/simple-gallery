import os
from os.path import isfile, join, splitext
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
from magic import Magic

ALLOWED_MIME = {'image/png', 'image/jpeg', 'image/gif'}
UPLOAD_FOLDER = os.environ['UPLOAD_FOLDER']


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
getmime = Magic(mime=True)

if not os.path.isdir(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


def allowed_mime(file):
    return getmime.from_buffer(file.stream.read(2048)) in ALLOWED_MIME


@app.route('/')
def gallery():
    images = [splitext(f) for f in os.listdir(UPLOAD_FOLDER) if isfile(
        join(UPLOAD_FOLDER, f)
    )]
    return render_template('gallery.html.j2', images=images)


@app.route('/memories', methods=['POST'])
def file():
    if 'file' not in request.files:
        return 'Missing content', 400
    file = request.files['file']
    if not allowed_mime(file):
        return 'MIME type not supported (allowed: png, jpeg and gif)', 415
    if file:
        filename = secure_filename(file.filename)
        file.save(join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('gallery'))
