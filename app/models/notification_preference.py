from app import db

class NotificationPreference(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120))
    phone = db.Column(db.String(20))
    notification_method = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f'<NotificationPreference {self.user_id}>'

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'email': self.email,
            'phone': self.phone,
            'notification_method': self.notification_method
        }