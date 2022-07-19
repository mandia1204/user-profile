from typing import List, TypedDict

class ProfileDto(TypedDict):
    id: int
    name: str
    email: str
    age: int
    picture: str
    phone: str
    address: str
    preferences: List[str]
