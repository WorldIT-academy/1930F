import json,os

def read(file_name):
    file_path = os.path.abspath(__file__+"/../../../static/"+file_name) 
    with open(file_path, "r", encoding = "utf-8") as file:
        return json.load(file)
