"""
This module takes care of starting the API Server, loading the DB, and adding the endpoints.
"""

import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure

# from models import Person  # Uncomment if using a Person model from models.py

app = Flask(__name__)  # Initializes the Flask application
app.url_map.strict_slashes = False  # Allows URLs without trailing slashes
CORS(app)  # Enables Cross-Origin Resource Sharing


# Create the Jackson family object using the FamilyStructure class
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors as JSON objects
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    # Returns the error as a JSON object with an appropriate status code
    return jsonify(error.to_dict()), error.status_code


# Generate a sitemap of all API endpoints
@app.route("/")
def sitemap():
    return generate_sitemap(app)


# Endpoint to get all family members
@app.route("/members", methods=["GET"])
def handle_hello():
    # Retrieves all members from the FamilyStructure
    members = jackson_family.get_all_members()
    # Constructs the response body containing all members
    response_body = {"hello": "world", "family": members}
    # Returns all members as JSON with status code 200 (OK)
    return jsonify(members), 200


# Endpoint to create a new family member
@app.route("/members", methods=["POST"])
def create_member():
    # Retrieves JSON data from the request
    data = request.get_json()
    # Adds the new member to the FamilyStructure
    jackson_family.add_member(data)
    # Returns the added member data as JSON with status code 200 (OK)
    return jsonify(data), 200


# Endpoint to get a specific member by ID
@app.route("/members/<int:id>", methods=["GET"])
def get_member(id):
    # Finds the member with the given ID
    member = jackson_family.get_member(id)
    # Returns the member as JSON with status code 200 (OK)
    return jsonify(member), 200


# Endpoint to delete a specific member by ID
@app.route("/members/<int:id>", methods=["DELETE"])
def delete_member(id):
    # Deletes the member with the given ID from the FamilyStructure
    jackson_family.delete_member(id)
    # Returns a success message as JSON with status code 200 (OK)
    return jsonify({"done": True}), 200


# Runs the app if this file is executed directly
if __name__ == "__main__":
    # Gets the port from environment variables, or defaults to 3000
    PORT = int(os.environ.get("PORT", 3000))
    # Runs the app with debugging enabled and on all network interfaces
    app.run(host="0.0.0.0", port=PORT, debug=True)


# /: Generates a sitemap of all endpoints.
# /members (GET): Returns a JSON list of all family members.
# /member (POST): Adds a new family member from JSON request data and returns the added member.
# /member/<int:id> (GET): Returns a specific member by their ID.
# /member/<int:id> (DELETE): Deletes a specific member by their ID and confirms deletion.

