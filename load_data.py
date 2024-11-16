import requests 
import json
def load_data():
    try: 
        with open("quiz.json", "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        raise FileNotFoundError("File not found")  
load = load_data()