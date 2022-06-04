import json
from http.client import ImproperConnectionState
from operator import imod


def read_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def write_json(data, filename, indent=4):
    with open(filename, 'w') as f:
        return json.dump(data, f, indent=indent)
