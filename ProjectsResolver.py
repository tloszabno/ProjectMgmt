import Config
import ProjectsDAO


def get_project_path_and_type(module_name):
    try:
        projects = ProjectsDAO.get_projects()
        return projects[module_name]['path'], projects[module_name]['type']
    except KeyError:
        msg = "Path not found for project [%s]" % module_name
        raise Exception(msg)
