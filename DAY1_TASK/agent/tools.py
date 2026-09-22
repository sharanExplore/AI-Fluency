import json


def get_student_data():
    """Read and return the student's private placement data."""

    with open("data/student_data.json", "r") as file:
        data = json.load(file)

    return data