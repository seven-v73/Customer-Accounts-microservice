# Customer Accounts Microservice

[![CI Build](../../actions/workflows/ci-build.yaml/badge.svg)](../../actions/workflows/ci-build.yaml)

REST API for creating, listing, reading, updating, and deleting customer accounts.

## Run locally

```bash
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
python run.py
```

The service listens on `http://localhost:8080`.

## API

`POST /accounts`, `GET /accounts`, `GET /accounts/<id>`, `PUT /accounts/<id>`, and `DELETE /accounts/<id>`.

## Test

```bash
pytest -q
```

