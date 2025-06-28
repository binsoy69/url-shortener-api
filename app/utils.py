import string
import random
from app.models import ShortURL, db

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits

    while True:
        short_code = ''.join(random.choices(characters, k=length))

        # Ensure uniqueness in the database
        existing = ShortURL.query.filter_by(short_code=short_code).first()
        if not existing:
            return short_code
