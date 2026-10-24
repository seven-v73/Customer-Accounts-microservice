import pytest
from service import create_app, db


@pytest.fixture()
def client():
    app = create_app({"TESTING": True, "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"})
    with app.test_client() as client:
        with app.app_context():
            db.drop_all()
            db.create_all()
        yield client


def test_crud_account(client):
    response = client.post("/accounts", json={"name": "Ada", "email": "ada@example.com"})
    assert response.status_code == 201
    account_id = response.json["id"]
    assert client.get("/accounts").json[0]["name"] == "Ada"
    assert client.get(f"/accounts/{account_id}").status_code == 200
    updated = client.put(f"/accounts/{account_id}",
                         json={"name": "Ada Lovelace"})
    assert updated.json["name"] == "Ada Lovelace"
    assert client.delete(f"/accounts/{account_id}").status_code == 204
    assert client.get(f"/accounts/{account_id}").status_code == 404


def test_validation(client):
    assert client.post("/accounts", json={}).status_code == 400
