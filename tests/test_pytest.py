import pytest
import requests

pytest_plugins = ["docker_compose"]


@pytest.fixture(scope="module")
def wait_for_services(module_scoped_container_getter):
    return module_scoped_container_getter


def test_get_some_service(wait_for_services):
    some_service = wait_for_services.get("someservice")
    print(some_service.name)
    assert True


def test_get_pg_service(wait_for_services):
    pg_service = wait_for_services.get("postgres")
    print(pg_service.name)
    assert True


def test_get_google():
    response = requests.get("http://www.google.com/")
    print(response.text)
    assert response.status_code == 200
