import pytest
import requests
import random


@pytest.fixture
def random_breed():
    r = requests.get("https://dog.ceo/api/breeds/list/all")
    list_breeds = [*r.json()["message"]]
    return random.choice(list_breeds)


@pytest.fixture
def brewery_city():
    r = requests.get("https://api.openbrewerydb.org/breweries").json()
    cities = []
    for brewery in r:
        cities.append(brewery["city"])
    return random.choice(cities)


@pytest.fixture
def brewery_country():
    r = requests.get("https://api.openbrewerydb.org/breweries").json()
    countries = []
    for brewery in r:
        countries.append(brewery["country"])
    return random.choice(countries)


def random_userid():
    r = requests.get("https://jsonplaceholder.typicode.com/posts").json()
    user_ids = []
    for ids in r:
        user_ids.append(ids["userId"])
    return random.choice(user_ids)


def random_post():
    r = requests.get("https://jsonplaceholder.typicode.com/posts").json()
    posts_ids = []
    for ids in r:
        posts_ids.append(ids["id"])
    return "/" + str(random.choice(posts_ids))


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")


def pytest_addoption(parser):
    parser.addoption("--url", default="https://ya.ru", help="This is request url")

    parser.addoption("--status_code", default="200", help="response status code")
