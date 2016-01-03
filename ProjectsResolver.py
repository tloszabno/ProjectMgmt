import Config
import ProjectsDAO


def get_project_path(module_name):
    try:
        projects = ProjectsDAO.get_projects()
        return projects[module_name]['path']  # Config.projects_paths[module_name]
    except KeyError:
        msg = "Path not found for project [%s]" % module_name
        raise Exception(msg)
