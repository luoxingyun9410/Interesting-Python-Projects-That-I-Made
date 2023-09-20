import random

students = {
    "Steve": {
        "age": 23,
        "height": 170.5,
        "weight": 60
    },
    "Jack": {
        "age": 30,
        "height": 160.5,
        "weight": 38
    },
    "Louis": {
        "age": 15,
        "height": 160.5,
        "weight": 38
    }
}

info = random.choice(list(students.items()))
print(info)