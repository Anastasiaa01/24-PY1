# TODO решите задачу
import json


FILENAME = "input.json"

def task() -> float:
    with open(FILENAME) as f:
        data = json.load(f)
        return round(sum([elem["score"] * elem["weight"] for elem in data]), 3)


print(task())
