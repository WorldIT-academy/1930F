import json 
import os

def write(data, file_name):
    path = os.path.abspath(__file__ + f"/../../../static/{file_name}")
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii= False, indent=4 )

