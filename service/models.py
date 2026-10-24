from service import db


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    address = db.Column(db.String(200), nullable=True)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email,
                "address": self.address}
