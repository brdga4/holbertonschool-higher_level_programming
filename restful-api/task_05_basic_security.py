#!/usr/bin/python3
"""
Task 05: API Security and Authentication Techniques
Demonstrates Basic Auth, JWT Auth, and Role-Based Access Control (RBAC) in Flask.
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    get_jwt,
    get_jwt_identity,
    jwt_required,
)
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

# Configure a secret key for JWT token generation and validation
app.config["JWT_SECRET_KEY"] = "super-secret-key-change-this-in-production"

# Initialize Auth Extensions
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# In-memory user database
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin",
    },
}

# ==========================================
# 1. BASIC AUTHENTICATION SETUP
# ==========================================


@auth.verify_password
def verify_password(username, password):
    """Verify username and password for Basic Authentication."""
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """Route protected by HTTP Basic Authentication."""
    return "Basic Auth: Access Granted", 200


# ==========================================
# 2. JWT CUSTOM ERROR HANDLERS (MUST RETURN 401)
# ==========================================


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Missing Authorization Header / Token."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Signature verification failed or malformed token."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """Token has expired."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    """Token has been revoked."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    """Fresh token required."""
    return jsonify({"error": "Fresh token required"}), 401


# ==========================================
# 3. JWT AUTHENTICATION ENDPOINTS
# ==========================================


@app.route("/login", methods=["POST"])
def login():
    """Login endpoint to receive a JWT access token."""
    data = request.get_json()

    if not data or not isinstance(data, dict):
        return jsonify({"error": "Invalid request payload"}), 400

    username = data.get("username")
    password = data.get("password")

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Embed the user's role directly in the JWT payload claims
    additional_claims = {"role": user["role"]}
    access_token = create_access_token(
        identity=username, additional_claims=additional_claims
    )

    return jsonify({"access_token": access_token}), 200


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """Route protected by JWT Authentication."""
    return "JWT Auth: Access Granted", 200


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """Role-based protected route (Admin only)."""
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted", 200


if __name__ == "__main__":
    app.run()
