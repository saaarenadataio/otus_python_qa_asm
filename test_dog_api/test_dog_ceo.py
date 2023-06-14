"""
Test https://dog.ceo/api site's API
"""

import pytest
import requests
from jsonschema import validate

# vars
test_url = "https://dog.ceo/api"
breed_path = "/breed/"
random_image_path = "/breeds/image/random"
random_breed_image_path = "/images/random"
url_templ_1 = "https://images.dog.ceo/breeds/"
url_templ_2 = ".jpg"
action_images = "/images"
action_list = "/list"
action_list_all = "/breeds/list/all"


@pytest.mark.parametrize(
    "breed",
    ["eskimo", "terrier", "birman", "basset"],
    ids=["no_child_breeds", "with_child_breeds", "no_such_breed", "child_breed"],
)
def test_sub_breeds(breed):
    r = requests.get(test_url + breed_path + breed + action_list)
    schema = {
        "type": "object",
        "properties": {"message": {"type": "array"}, "status": {"type": "string"}},
        "required": ["message", "status"],
    }
    if breed in ["birman", "basset"]:
        assert r.status_code == 404, f"Wrong status code {r.status_code}, expected 404"
        assert (
            r.json()["status"] == "error"
        ), f'Wrong status {r.json()["status"]}, expected "error"'
        assert (
            r.json()["message"] == "Breed not found (master breed does not exist)"
        ), f'Wrong error message {r.json()["message"]}'
    else:
        assert r.status_code == 200, f"Wrong status code {r.status_code}, expected 200"
        assert (
            r.json()["status"] == "success"
        ), f'Wrong status {r.json()["status"]}, expected "success"'
        validate(instance=r.json(), schema=schema)


def test_random_image():
    r = requests.get(test_url + random_image_path)
    schema = {
        "type": "object",
        "properties": {"message": {"type": "string"}, "status": {"type": "string"}},
        "required": ["message", "status"],
    }
    assert r.status_code == 200, f"Wrong status code {r.status_code}, expected 200"
    assert (
        url_templ_1 in r.json()["message"] and url_templ_2 in r.json()["message"]
    ), f'Wrong image URL: {r.json()["message"]}'
    assert (
        r.json()["status"] == "success"
    ), f'Wrong status: {r.json()["status"]}, expected Success'
    validate(instance=r.json(), schema=schema)


@pytest.mark.parametrize(
    "breed",
    ["eskimo", "terrier", "birman", "basset"],
    ids=["no_child_breeds", "with_child_breeds", "no_such_breed", "child_breed"],
)
def test_breed_images(breed):
    r = requests.get(test_url + breed_path + breed + action_images)
    schema = {
        "type": "object",
        "properties": {"message": {"type": "array"}, "status": {"type": "string"}},
        "required": ["message", "status"],
    }
    if breed in ["birman", "basset"]:
        assert r.status_code == 404, f"Wrong status code {r.status_code}, expected 404"
        assert (
            r.json()["status"] == "error"
        ), f'Wrong status {r.json()["status"]}, expected "error"'
        assert (
            r.json()["message"] == "Breed not found (master breed does not exist)"
        ), f'Wrong error message {r.json()["message"]}'
    else:
        assert r.status_code == 200, f"Wrong status code {r.status_code}, expected 200"
        assert (
            r.json()["status"] == "success"
        ), f'Wrong status {r.json()["status"]}, expected "success"'
        validate(instance=r.json(), schema=schema)


def test_full_breeds_list():
    r = requests.get(test_url + action_list_all)
    schema = {
        "type": "object",
        "properties": {"message": {"type": "object"}, "status": {"type": "string"}},
        "required": ["message", "status"],
    }
    assert r.status_code == 200, f"Wrong status code {r.status_code}, expected 200"
    assert (
        r.json()["status"] == "success"
    ), f'Wrong status {r.json()["status"]}, expected "success"'
    validate(instance=r.json(), schema=schema)


def test_random_breed_image(random_breed):
    r = requests.get(test_url + breed_path + random_breed + random_breed_image_path)
    schema = {
        "type": "object",
        "properties": {"message": {"type": "string"}, "status": {"type": "string"}},
        "required": ["message", "status"],
    }
    assert r.status_code == 200, f"Wrong status code {r.status_code}, expected 200"
    assert (
        url_templ_1 in r.json()["message"] and url_templ_2 in r.json()["message"]
    ), f'Wrong image URL: {r.json()["message"]}'
    assert (
        r.json()["status"] == "success"
    ), f'Wrong status {r.json()["status"]}, expected "success"'
    validate(instance=r.json(), schema=schema)
