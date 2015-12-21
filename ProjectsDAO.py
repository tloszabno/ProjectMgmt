import json
import Config


def get_projects(db_path=Config.projects_db_path):
    with open(db_path, "r") as db:
        return json.load(db)


def save_projects(projects_json, db_path=Config.projects_db_path):
    json_str = json.dumps(projects_json)
    with open(db_path, "w") as db:
        db.write(json_str)
