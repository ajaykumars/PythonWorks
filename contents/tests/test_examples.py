import pytest
import requests

def test_for_equals():
    a = True
    b = False
    assert a == b , "Test failed for comparision"


def test_for_response():
    response = requests.get('https://imgs.xkcd.com/comics/python.png')
    assert response.status_code == 200