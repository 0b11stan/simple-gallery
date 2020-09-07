import requests
import inspect

class testc:
    SUCCESS = '\033[0;32m'
    FAILURE = '\033[91m'
    CLEAR = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def test_import_pictures():
    print(testc.SUCCESS + inspect.stack()[0][3] + testc.CLEAR)
    file = {'file': open('tux.jpg', 'rb')}
    response = requests.post('http://localhost:5000/pic', files=file)
    assert response.status_code == 200

test_import_pictures()
