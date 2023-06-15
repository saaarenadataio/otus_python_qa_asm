"""
Test https://www.openbrewerydb.org site's API
"""

import pytest
import requests
from jsonschema import validate

from test_dog_api.conftest import brewery_city, brewery_country

test_url = "https://api.openbrewerydb.org/v1"
breweries_path = "/breweries"
meta_path = "/meta"
random_path = "/random"
search_path = "/search"

single_brewery_schema = {
    "type": "array",
    "properties": {
        "id": {"type": "string"},
        "name": {"type": "string"},
        "brewery_type": {"type": "string"},
        "street": {"type": ["string", "null"]},
        "address_1": {"type": ["string", "null"]},
        "address_2": {"type": ["string", "null"]},
        "address_3": {"type": ["string", "null"]},
        "city": {"type": ["string", "null"]},
        "state": {"type": ["string", "null"]},
        "county_province": {"type": ["string", "null"]},
        "postal_code": {"type": ["string", "null"]},
        "country": {"type": ["string", "null"]},
        "longitude": {"type": ["string", "null"]},
        "latitude": {"type": ["string", "null"]},
        "phone": {"type": ["string", "null"]},
        "website_url": {"type": ["string", "null"]},
        "updated_at": {"type": "string"},
        "created_at": {"type": "string"},
    },
    "required": ["id", "name", "brewery_type"],
}


@pytest.mark.parametrize(
    "filters", ["Austin", "United States"], ids=["city", "country"]
)
def test_brewery_search(filters):
    query = {"query": filters, "per_page": "10"}
    r = requests.get(test_url + breweries_path + search_path, params=query)
    assert (
        r.status_code == 200
    ), f"Wrong status code returned: {r.status_code}, expected 200"
    for brewery in r.json():
        validate(instance=brewery, schema=single_brewery_schema['properties'])



@pytest.mark.parametrize(
    "types", ["micro", "large", "brewpub", "closed"]
)
def test_breweries_by_type_positive(types):
    schema_breweries_meta = {
        "type": "object",
        "properties": {
            "total": {"type": "string"},
            "page": {"type": "string"},
            "per_page": {"type": "string"},
        },
        "required": ["total", "page", "per_page"],
    }
    query = {"by_type": types, "per_page": "10"}
    r = requests.get(test_url + breweries_path + meta_path, params=query)
    assert (
        r.status_code == 200
        ), f"Wrong status code returned: {r.status_code}, expected 200"
    validate(instance=r.json(), schema=schema_breweries_meta)

@pytest.mark.parametrize(
    "types", ["no_such_type"]
)
def test_breweries_by_type_negative(types):
    query = {"by_type": types, "per_page": "10"}
    r = requests.get(test_url + breweries_path + meta_path, params=query)
    assert (
            r.status_code == 400
        ), f"Wrong status code returned: {r.status_code}, expected 400"



def test_per_page():
    r = requests.get(test_url + breweries_path)
    assert (
        len(r.json()) == 50
    ), f"Wrong default number of breweries per page: {len(r.json())}, expected 50"


def test_all_breweries_info():
    r = requests.get(test_url + breweries_path)
    assert (
        r.status_code == 200
    ), f"Wrong status code returned: {r.status_code}, expected 200"


def test_random_brewery():
    r = requests.get(test_url + breweries_path + random_path)
    assert (
        r.status_code == 200
    ), f"Wrong status code returned: {r.status_code}, expected 200"
    validate(instance=r.json(), schema=single_brewery_schema)
