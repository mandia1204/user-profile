from typing import List
import random
from flaskr.db import Profile
from flaskr.dtos import ProfileDto

def get_profile():
    all = Profile.objects.all()
    profiles: List[ProfileDto] = list(map(lambda profile : dict(profile), all))
    return profiles

def save_profile(profile: ProfileDto):
    newProfile = Profile(id= random.randint(10, 10000), age = profile['age'], name = profile['name'], email= profile['email'], avatarPicture = profile['avatarPicture'])
    newProfile.save()
    return dict(newProfile)
