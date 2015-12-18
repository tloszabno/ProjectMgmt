import Config


def get_project_path(module_name):
    try:
        return Config.projects_paths[module_name]
    except KeyError:
        msg = "Path not found for project [%s]" % module_name
        raise Exception(msg)
