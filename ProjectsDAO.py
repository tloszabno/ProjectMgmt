import json
import Config
import ProjectAutoDetector


def get_projects(db_path=Config.projects_db_path):
    with open(db_path, "r") as db:
        return json.load(db)


def save_projects(projects_json, db_path=Config.projects_db_path):
    json_str = json.dumps(projects_json)
    with open(db_path, "w") as db:
        db.write(json_str)


def add_project(project_key, project_path, project_type, db_path=Config.projects_db_path):
    projects = get_projects(db_path)
    projects[project_key] = {'type': project_type, 'path': project_path}
    save_projects(projects, db_path=db_path)


def add_server(project_key, project_path, db_path=Config.projects_db_path):
    add_project(project_key, project_path, 'server', db_path=db_path)


def add_mvn_project(project_key, project_path, db_path=Config.projects_db_path):
    add_project(project_key, project_path, 'mvn_project', db_path=db_path)


def print_available_projects(db_path=Config.projects_db_path):
    projects = get_projects(db_path)
    print "[project_key](type)\t\t[path_to_project]"
    for p_key in sorted(projects.keys()):
        print "[%s](%s)\t\t[%s]" % (p_key, projects[p_key]['type'], projects[p_key]['path'])


def autodetect_and_save_projects(folder_to_scan, db_path=Config.projects_db_path):
    detected = ProjectAutoDetector.scan_folder(folder_to_scan)
    save_projects(detected, db_path=db_path)
