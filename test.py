import pytest
import requests

BASE_URL = "http://127.0.0.1:8000"


@pytest.fixture(autouse=True)
def reset_system():
    response = requests.post(f"{BASE_URL}/reset/")
    assert response.status_code == 200


@pytest.fixture
def setup_movies():
    response = requests.post(f"{BASE_URL}/movies/", json={"name": "Inception"})
    movie_id1 = response.json()["movie_id"]

    response = requests.post(f"{BASE_URL}/movies/", json={"name": "The Matrix"})
    movie_id2 = response.json()["movie_id"]

    return movie_id1, movie_id2


@pytest.fixture
def setup_users():
    response = requests.post(f"{BASE_URL}/users/", json={"name": "Alice"})
    user_id1 = response.json()["user_id"]

    response = requests.post(f"{BASE_URL}/users/", json={"name": "Bob"})
    user_id2 = response.json()["user_id"]

    return user_id1, user_id2


def test_add_movie():
    response = requests.post(f"{BASE_URL}/movies/", json={"name": "Inception"})
    assert response.status_code == 200
    movie_id1 = response.json()["movie_id"]

    response = requests.post(f"{BASE_URL}/movies/", json={"name": "The Matrix"})
    assert response.status_code == 200
    movie_id2 = response.json()["movie_id"]

    assert movie_id1 == 1
    assert movie_id2 == 2


def test_show_all_movies(setup_movies):
    movie_id1, movie_id2 = setup_movies
    response = requests.get(f"{BASE_URL}/movies/")
    assert response.status_code == 200
    movies = response.json()["movies"]
    movies = {int(k): v for k, v in movies.items()}
    assert movies == {movie_id1: "Inception", movie_id2: "The Matrix"}


def test_add_user():
    response = requests.post(f"{BASE_URL}/users/", json={"name": "Alice"})
    assert response.status_code == 200
    user_id1 = response.json()["user_id"]

    response = requests.post(f"{BASE_URL}/users/", json={"name": "Bob"})
    assert response.status_code == 200
    user_id2 = response.json()["user_id"]

    assert user_id1 == 1
    assert user_id2 == 2


def test_buy_ticket(setup_movies, setup_users):
    movie_id1, movie_id2 = setup_movies
    user_id1, user_id2 = setup_users

    response = requests.post(
        f"{BASE_URL}/tickets/", json={"user_id": user_id1, "movie_id": movie_id1}
    )
    assert response.status_code == 200
    ticket_id1 = response.json()["ticket_id"]

    response = requests.post(
        f"{BASE_URL}/tickets/", json={"user_id": user_id2, "movie_id": movie_id2}
    )
    assert response.status_code == 200
    ticket_id2 = response.json()["ticket_id"]

    assert ticket_id1 == 1
    assert ticket_id2 == 2


def test_cancel_ticket(setup_movies, setup_users):
    movie_id1, movie_id2 = setup_movies
    user_id1, user_id2 = setup_users

    response = requests.post(
        f"{BASE_URL}/tickets/", json={"user_id": user_id1, "movie_id": movie_id1}
    )
    ticket_id1 = response.json()["ticket_id"]

    response = requests.delete(f"{BASE_URL}/tickets/{ticket_id1}")
    assert response.status_code == 200

    response = requests.delete(f"{BASE_URL}/tickets/999")
    assert response.status_code == 404
