from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from service import db
from service.models import Account

accounts = Blueprint("accounts", __name__, url_prefix="/accounts")


@accounts.get("")
def list_accounts():
    return jsonify([a.to_dict() for a in Account.query.all()])


@accounts.post("")
def create_account():
    data = request.get_json(silent=True) or {}
    if not data.get("name") or not data.get("email"):
        return jsonify(error="name and email are required"), 400
    account = Account(name=data["name"], email=data["email"],
                      address=data.get("address"))
    db.session.add(account)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify(error="email already exists"), 409
    return jsonify(account.to_dict()), 201


@accounts.get("/<int:account_id>")
def read_account(account_id):
    account = db.session.get(Account, account_id)
    return jsonify(account.to_dict()) if account else (jsonify(error="not found"), 404)


@accounts.put("/<int:account_id>")
def update_account(account_id):
    account = db.session.get(Account, account_id)
    if not account:
        return jsonify(error="not found"), 404
    data = request.get_json(silent=True) or {}
    for field in ("name", "email", "address"):
        if field in data:
            setattr(account, field, data[field])
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify(error="email already exists"), 409
    return jsonify(account.to_dict())


@accounts.delete("/<int:account_id>")
def delete_account(account_id):
    account = db.session.get(Account, account_id)
    if not account:
        return jsonify(error="not found"), 404
    db.session.delete(account)
    db.session.commit()
    return "", 204
