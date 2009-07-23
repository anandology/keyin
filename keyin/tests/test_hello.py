
from keyin.webapp import app


def test_hello():
    b = app.browser()

    response = b.open('/hello/keyin')
    assert response.read() == "hello keyin"
    assert response.info().getheader('Content-Type') == 'text/plain'

