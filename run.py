from app import create_app
from app.utils import generate_short_code
import os

app = create_app()

if __name__ == "__main__":
    app.run()
