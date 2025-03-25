from app import create_app, db
from app.models import User
from faker import Faker
import random

app = create_app()
faker = Faker()

profile_pictures = ['default.png', 'avatar1.png', 'avatar2.png', 'avatar3.png']

with app.app_context():
    db.create_all()

    for _ in range(50):
        user = User(
            username=faker.user_name(),
            profile_picture=random.choice(profile_pictures)
        )
        db.session.add(user)

    db.session.commit()

    print("50 random users added successfully.")
