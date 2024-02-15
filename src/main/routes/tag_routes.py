from flask import Blueprint, request, jsonify

tags_routes_bp = Blueprint("tag_routes", __name__)


@tags_routes_bp.route("/create_tag", methods=["POST"])
def create_tag():
    print(request.json)
    return jsonify({"resp": "Created tag"}), 200
