"""
Test https://jsonplaceholder.typicode.com/ site's API
"""

import pytest
import requests
from jsonschema import validate

from test_dog_api.conftest import random_userid, random_post

test_url = "https://jsonplaceholder.typicode.com"
posts_path = "/posts"
user_path = "/posts?userId="

post_schema = {
    "type": "object",
    "properties": {
        "body": {"type": "string"},
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "userId": {"type": "integer"},
    },
}


@pytest.mark.parametrize(
    "wrong_post_id", [-100500, "null", ""], ids=["negative", "null", "empty"]
)
def test_post_incorrect_id(wrong_post_id):
    schema = {"type": "array"}
    query = {
        "query": wrong_post_id,
    }
    r = requests.get(test_url + posts_path, params=query)
    assert r.status_code == 200, f"Wrong status code: {r.status_code}, expected 200"
    validate(instance=r.json(), schema=schema)


@pytest.mark.parametrize(
    "wrong_user_id", [-100500, "null", ""], ids=["negative", "null", "empty"]
)
def test_incorrect_user_id(wrong_user_id):
    schema = {"type": "array"}
    query = {
        "query": wrong_user_id,
    }
    r = requests.get(test_url + user_path, params=query)
    assert r.status_code == 200, f"Wrong status code: {r.status_code}, expected 200"
    validate(instance=r.json(), schema=schema)


def test_filter_by_userid():
    userid = random_userid
    r = requests.get(test_url + user_path + str(userid))
    assert r.status_code == 200, f"Wrong status code: {r.status_code}, expected 200"
    for user in r.json():
        assert user["userId"] == userid


def test_posts_schema():
    r = requests.get(test_url + posts_path)
    assert r.status_code == 200, f"Wrong status code: {r.status_code}, expected 200"
    for post in r.json():
        validate(instance=post, schema=post_schema)


def test_single_post_schema():
    r = requests.get(test_url + posts_path + str(random_post()))
    assert r.status_code == 200, f"Wrong status code: {r.status_code},  expected 200"
    validate(instance=r.json(), schema=post_schema)
