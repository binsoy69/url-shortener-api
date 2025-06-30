from flask import Blueprint, request, jsonify
from app.models import db, ShortURL
from app.utils import generate_short_code
from datetime import datetime, timezone
from flask import redirect

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
    short_url.access_count += 1
    db.session.commit()

    return jsonify({
        "id": short_url.id,
        "url": short_url.url,
        "shortCode": short_url.short_code,
        "createdAt": short_url.created_at.isoformat(),
        "updatedAt": short_url.updated_at.isoformat()
    }), 200

@bp.route("/shorten/<string:short_code>", methods=["PUT"])
def update_short_url(short_code):
    data = request.get_json()

    if not data or "url" not in data:
        return jsonify({"error": "Missing 'url' field in request"}), 400

    short_url = ShortURL.query.filter_by(short_code=short_code).first()

    if not short_url:
        return jsonify({"error": "Short URL not found"}), 404

    short_url.url = data["url"]
    short_url.updated_at = datetime.now(timezone.utc)

    db.session.commit()

    return jsonify({
        "id": short_url.id,
        "url": short_url.url,
        "shortCode": short_url.short_code,
        "createdAt": short_url.created_at.isoformat(),
        "updatedAt": short_url.updated_at.isoformat()
    }), 200

@bp.route("/shorten/<string:short_code>", methods=["DELETE"])
def delete_short_url(short_code):
    short_url = ShortURL.query.filter_by(short_code=short_code).first()

    if not short_url:
        return jsonify({"error": "Short URL not found"}), 404

    db.session.delete(short_url)
    db.session.commit()

    return '', 204


@bp.route("/shorten/<string:short_code>/stats", methods=["GET"])
def get_url_stats(short_code):
    short_url = ShortURL.query.filter_by(short_code=short_code).first()

    if not short_url:
        return jsonify({"error": "Short URL not found"}), 404

    return jsonify({
        "id": short_url.id,
        "url": short_url.url,
        "accessCount": short_url.access_count
    }), 200


@bp.route("/r/<string:short_code>", methods=["GET"])
def redirect_short_url(short_code):
    short_url = ShortURL.query.filter_by(short_code=short_code).first()

    if not short_url:
        return jsonify({"error": "Short URL not found"}), 404

    short_url.access_count += 1
    db.session.commit()

    return redirect(short_url.url)
