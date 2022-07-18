from flask import Flask, jsonify, request
from flaskr.profile_service import get_profile, save_profile

def add_profile_routes(app: Flask):
    @app.get('/profile')
    def get_profiles():
        profiles = get_profile()
        return jsonify(profiles)

    @app.post('/profile')
    def post_profile():
        body = request.json
        return save_profile(body)
