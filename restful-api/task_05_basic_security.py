#!/usr/bin/python3
"""
A Flask API implementing Basic and JWT Authentication with Role-Based Access.
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

app = Flask(__name__)

# JWT Configuration
app.config['JWT_SECRET_KEY'] = 'your-super-secret-key-12345'
jwt = JWTManager(app)
auth = HTTPBasicAuth()

# In-memory user data
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# --- Basic Authentication ---
@auth.verify_password
def verify_password(username, password):
    """Verifies username and password for Basic Auth."""
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return username
    return None


@auth.error_handler
def auth_error():
    """Handles Basic Auth unauthorized access."""
    return jsonify({"error": "Unauthorized access"}), 401


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """Endpoint protected by Basic Auth."""
    return "Basic Auth: Access Granted"


# --- JWT Authentication ---
@app.route("/login", methods=["POST"])
def login():
    """Authenticates a user and returns a JWT token."""
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Missing credentials"}), 400

    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        # Embed the role inside the token payload
        identity = {"username": username, "role": user["role"]}
        access_token = create_access_token(identity=identity)
        return jsonify({"access_token": access_token}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """Endpoint protected by JWT token."""
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """Endpoint protected by JWT token and Role-Based access (Admin)."""
    current_user = get_jwt_identity()
    if current_user.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


# --- Custom JWT Error Handlers ---
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
