from flask import Flask, escape, request, render_template
from os import listdir
from os.path import isfile, join, splitext

app = Flask(__name__)

IMAGES_PATH = 'static'

@app.route('/')
def gallery():
    images = [splitext(f) for f in listdir(IMAGES_PATH) if isfile(
        join(IMAGES_PATH, f)
    )]
    print(images)
    return render_template('gallery.html.j2', images=images)
