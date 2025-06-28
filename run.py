from app import create_app
from app.utils import generate_short_code

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        print("Sample generated code:", generate_short_code())

    app.run(debug=True)
