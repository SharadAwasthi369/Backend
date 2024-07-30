from flask import Blueprint, jsonify, request
from app.models.flight import Flight
from app import db
from app.services.kafka_service import produce_flight_status_update

flights_bp = Blueprint('flights', __name__)

@flights_bp.route('/api/flights', methods=['GET'])
def get_flights():
    flights = Flight.query.all()
    return jsonify([flight.to_dict() for flight in flights])

@flights_bp.route('/api/flight_status', methods=['POST'])
def update_flight_status():
    data = request.json
    flight = Flight.query.get(data['flightId'])
    if not flight:
        return jsonify({'error': 'Flight not found'}), 404
    
    flight.update_status(data['status'], data.get('delay'))
    db.session.commit()
    
    # Try to send Kafka message, but continue even if it fails
    produce_flight_status_update(flight.to_dict())
    
    return jsonify(flight.to_dict())