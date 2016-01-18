import ProjectsDAO


def validate_modules_exists(commands):
    projects = ProjectsDAO.get_projects()

    wrong_modules_names = filter(lambda command: command.target_module not in projects.keys(), commands)
    if len(wrong_modules_names):
        msg = "Unknown modules keys=%s" % str(map(lambda cmd: cmd.target_module, wrong_modules_names))
        raise Exception(msg)
