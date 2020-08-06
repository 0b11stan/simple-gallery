from flask import Flask, escape, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
from os import listdir
from os.path import isfile, join, splitext

IMAGES_PATH = 'static'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = IMAGES_PATH


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def gallery():
    if request.method == 'GET':
        images = [splitext(f) for f in listdir(IMAGES_PATH) if isfile(
            join(IMAGES_PATH, f)
        )]
        print(images)
        return render_template('gallery.html.j2', images=images)
    elif request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('gallery'))
