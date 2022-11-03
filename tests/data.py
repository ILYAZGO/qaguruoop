from dataclasses import dataclass
from enum import Enum
from typing import Tuple


class Subject(Enum):
    Chemistry = 'Chemistry'
    English = 'English'
    Physics = 'Physics'


class Hobby(Enum):
    Sports = 'Sports'
    Reading = 'Reading'
    Music = 'Music'


class Gender(Enum):
    Male = 'Male'
    Female = 'Female'
    Other = 'Other'


@dataclass
class User:
    gender: Gender
    first_name: str
    last_name: str
    email: str = 'test@mail.ru'
    mobile: str = '1234567890'
    birth_day: str = '28'
    birth_month: str = 'June'
    birth_year: str = '1987'
    subjects: Tuple[Subject] = (Subject.Physics, Subject.English)
    current_address: str = 'Ankara, main building, 2nd floor, 34'
    hobbies: Tuple[Hobby] = (Hobby.Reading, Hobby.Music)
    picture_file: str = 'kitty.jpeg'
    state: str = 'Uttar Pradesh'
    city: str = 'Agra'


kemal = User(gender= Gender.Male, first_name='Kemal', last_name='Ataturk')
