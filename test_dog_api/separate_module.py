"""
 Separate module to test addoption
"""
import requests


def test_status_code(base_url, status_code):
    r = requests.get(base_url)
    assert r.status_code == int(status_code)
