from flask import Blueprint, request, jsonify
from app.models import db, ShortURL
from app.utils import generate_short_code
from datetime import datetime, timezone

bp = Blueprint("api", __name__)

@bp.route("/shorten", methods=["POST"])
def create_short_url():
    data = request.get_json()

    if not data or "url" not in data:
        return jsonify({"error": "Missing 'url' field in request"}), 400

    url = data["url"]
    short_code = generate_short_code()

    new_url = ShortURL(
        url=url,
        short_code=short_code,
        created_at=datetime.now(timezone.utc),
        updated_at=datetime.now(timezone.utc)
    )

    db.session.add(new_url)
    db.session.commit()

    return jsonify({
        "id": new_url.id,
        "url": new_url.url,
        "shortCode": new_url.short_code,
        "createdAt": new_url.created_at.isoformat(),
        "updatedAt": new_url.updated_at.isoformat()
    }), 201


@bp.route("/shorten/<string:short_code>", methods=["GET"])
def get_original_url(short_code):
    short_url = ShortURL.query.filter_by(short_code=short_code).first()

    if not short_url:
        return jsonify({"error": "Short URL not found"}), 404

    # Optional: increment access count here if this counts as an access
    return jsonify({
        "id": short_url.id,
        "url": short_url.url,
        "shortCode": short_url.short_code,
        "createdAt": short_url.created_at.isoformat(),
        "updatedAt": short_url.updated_at.isoformat()
    }), 200

