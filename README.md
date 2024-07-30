# Flight Status Backend

This is the backend application for the Flight Status Updates and Notifications system.

## Setup

1. Create a virtual environment:

python -m venv venv


2. Activate the virtual environment:
- On Windows: `venv\Scripts\activate`


3. Install dependencies:
pip install -r requirements.txt


4. Set up your PostgreSQL database and update the `DATABASE_URL` in the `.env` file.

5. Initialize the database:
flask db init
flask db migrate
flask db upgrade


6. Run the application:
python run.py


## API Endpoints

- GET `/api/flights`: Get all flights
- POST `/api/flight_status`: Update flight status
- POST `/api/notification_preferences`: Update notification preferences

## Kafka Integration

Make sure you have Kafka running and update the `KAFKA_BOOTSTRAP_SERVERS` in `config.py` if necessary.

## Learn More

For more information on Flask, check out the [Flask documentation](https://flask.palletsprojects.com/)