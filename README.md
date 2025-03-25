# Flask User Profiles

A simple Flask web application that displays user profiles, including usernames, user IDs, and profile pictures. It supports database interactions using SQLAlchemy and automatically generates sample user data using Faker.

## Project Structure
```
flask_user_profiles/
├── app
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── templates
│   │   ├── users.html
│   │   └── user_detail.html
│   └── static
│       └── profile_pics
│           └── default.png
├── tests
│   └── test_app.py
├── query.py
├── requirements.txt
└── run.py
```

## Features
- Flask web application structured using blueprints
- SQLAlchemy ORM for database management
- Automatic user generation with Faker
- Individual user profile viewing via UID routing
- Unit testing using pytest

## Installation

Install dependencies using:
```bash
pip install -r requirements.txt
```

## Usage

### Run Application
```bash
python run.py
```
Access the app at [http://localhost:5000](http://localhost:5000).

### Initialize and Seed Database
Generate random user data:
```bash
python query.py
```

### Testing
Run tests using pytest:
```bash
pytest tests/test_app.py
```

## Dependencies
- Flask
- Flask-SQLAlchemy
- Faker
- pytest

## Routes
- `/`: View all users
- `/uid/<uid_number>/`: View individual user details by UID

## Author

Your Name Here

## License

This project is licensed under the MIT License.