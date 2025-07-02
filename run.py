from app import create_app
from app.utils import generate_short_code

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
    app.run(host="0.0.0.0", port=10000)