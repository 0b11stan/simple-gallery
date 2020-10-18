import os
from sys import exit
from hashlib import md5
from mimetypes import guess_extension
from flask import Flask, request
from magic import Magic

ALLOWED_MIME = {'image/png', 'image/jpeg', 'image/gif'}

getmime = Magic(mime=True)

application = Flask(__name__, instance_relative_config=True)
application.config['UPLOAD_FOLDER'] = os.environ['UPLOAD_FOLDER']

if not os.access(application.config['UPLOAD_FOLDER'], os.W_OK):
    exit(1)

@application.route('/pictures', methods=['POST'])
def file():
    if 'file' not in request.files:
        return 'Missing content', 400
    file = request.files['file']
    mimetype = getmime.from_buffer(file.stream.read(2048))
    if not mimetype in ALLOWED_MIME:
        return 'MIME type not supported (allowed: png, jpeg and gif)', 415
    if file:
        file.stream.seek(0)
        filename = md5(file.stream.read()).hexdigest()
        filename = filename + guess_extension(mimetype)
        file.stream.seek(0)
        file.save(os.path.join(application.config['UPLOAD_FOLDER'], filename))
        return filename, 200
