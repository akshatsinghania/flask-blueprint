from flask import Blueprint,jsonify

admin = Blueprint("admin",__name__)

@admin.route("/")
def index():
    return jsonify({
        "name":"akshat"
    })
