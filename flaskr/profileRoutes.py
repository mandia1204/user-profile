from typing import List
from flask import Flask, jsonify, request
import random
from flaskr.db import Profile
from flaskr.dtos import ProfileDto

def addProfileRoutes(app: Flask):
    @app.get('/profile')
    def getProfile():
        profiles = Profile.objects.all()
        result: List[ProfileDto] = list(map(lambda profile : { "id" : profile["id"], "age": profile["age"], "email": profile["email"] } , profiles))
        return jsonify(result[0]['age'])

    @app.post('/profile')
    def postProfile():
        body = request.json
        newProfile = Profile(id= random.randint(10, 10000), age = body['age'], name = body['name'], email= body['email'], avatarPicture = body['avatarPicture'])
        newProfile.save()
        return {}
