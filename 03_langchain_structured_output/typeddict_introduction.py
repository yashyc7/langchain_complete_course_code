from typing import TypedDict


class Person(TypedDict):
    name: str
    age: int
    gender: str


new_person: Person = {"name": "nitish", "age": 13, "gender": 35}


other_person: Person = {"name": "nitish", "age": "13", "gender": 35}
print(new_person)
print(other_person)
