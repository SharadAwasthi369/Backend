from flask import Blueprint, jsonify, request
from app.models.notification_preference import NotificationPreference
from app import db

notifications_bp = Blueprint('notifications', __name__)

@notifications_bp.route('/api/notification_preferences', methods=['POST'])
def update_notification_preferences():
    data = request.json
    pref = NotificationPreference.query.filter_by(user_id=data['userId']).first()
    
    if pref:
        pref.email = data['email']
        pref.phone = data['phone']
        pref.notification_method = data['notificationMethod']
    else:
        pref = NotificationPreference(
            user_id=data['userId'],
            email=data['email'],
            phone=data['phone'],
            notification_method=data['notificationMethod']
        )
        db.session.add(pref)
    
    db.session.commit()
    return jsonify(pref.to_dict())