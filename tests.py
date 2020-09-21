import requests
import inspect


class testc:
    SUCCESS = '\033[0;32m'
    FAILURE = '\033[91m'
    CLEAR = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def test_import_pictures():
    file = {'file': open('test_samples/tux.jpg', 'rb')}
    response = requests.post('http://localhost:5000/memories', files=file)
    assert response.status_code == 200
    print(testc.SUCCESS + inspect.stack()[0][3] + testc.FAILURE)


def test_error_on_empty_import():
    response = requests.post('http://localhost:5000/memories')
    assert response.status_code == 400
    assert 'Missing content' in response.text
    print(testc.SUCCESS + inspect.stack()[0][3] + testc.FAILURE)


def test_error_on_import_unsupported_mime_type():
    file = {'file': open('test_samples/payload.png', 'rb')}
    response = requests.post('http://localhost:5000/memories', files=file)
    assert response.status_code == 415
    assert 'MIME type not supported' in response.text
    print(testc.SUCCESS + inspect.stack()[0][3] + testc.FAILURE)


test_import_pictures()
test_error_on_empty_import()
test_error_on_import_unsupported_mime_type()
