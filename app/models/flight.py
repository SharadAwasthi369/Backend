from app import db
from datetime import datetime

class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(10), unique=True, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    delay = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Flight {self.number}>'

    def to_dict(self):
        return {
            'id': self.id,
            'number': self.number,
            'status': self.status,
            'delay': self.delay,
            'updated_at': self.updated_at.isoformat()
        }

    def update_status(self, status, delay=None):
        self.status = status
        self.delay = delay
        self.updated_at = datetime.utcnow()
        db.session.commit()