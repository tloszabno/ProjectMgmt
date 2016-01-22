import ProjectsDAO
from common import CustomAction
import os


def append_buildins_commands(arg_parser):
    arg_parser.add_argument('-asc', '--autoscan', nargs='*', dest='autoscan', action=CustomAction)
    arg_parser.add_argument('-amp', '--add-mvn-project', nargs='*', dest='add-mvn-project', action=CustomAction)
    arg_parser.add_argument('-asp', '--add-script', nargs='*', dest='add-script', action=CustomAction)
    arg_parser.add_argument('-rmp', '--remove-project', nargs='*', dest='remove-project', action=CustomAction)
    arg_parser.add_argument('-show', '--show-projects', nargs='?', dest='show-projects', action=CustomAction)
    arg_parser.add_argument('-search', '--search-projects', nargs='*', dest='search-projects', action=CustomAction)


def __get_entry_for_argument__(parsed_args, arg_name):
    return filter(lambda e: e[0] == arg_name, parsed_args.ordered_args)[0]


def __check_args_available__(entry, args_names):
    if len(entry) < 2 or len(entry[1]) < len(args_names):
        msg = '%s needs arguments: %s' % (entry[0], str(args_names))
        raise Exception(msg)
    for i in xrange(len(args_names)):
        if len(entry[1][i]) < 1:
            msg = '%s needs arguments: %s' % (entry[0], str(args_names))
            raise Exception(msg)


def __get_full_path__(path):
    return os.path.abspath(path)


def run(parsed_args):
    # print parsed_args

    if 'ordered_args' not in dir(parsed_args):
        return False

    provided_special_cmds = [x[0] for x in parsed_args.ordered_args]

    if 'show-projects' in provided_special_cmds:
        ProjectsDAO.print_available_projects()
        return True

    if 'search-projects' in provided_special_cmds:
        entry = __get_entry_for_argument__(parsed_args,'search-projects')
        __check_args_available__(entry, ['project_key'])
        key = entry[1][0]
        for (p_key, p_path, p_type)  in ProjectsDAO.search_matching_projects(key):
            print "%25s [%s]" % ("[" + p_key + "](" + p_type + ")", p_path)
        return True

    if 'autoscan' in provided_special_cmds:
        entry = __get_entry_for_argument__(parsed_args,'autoscan')
        __check_args_available__(entry, ['path'])
        ProjectsDAO.autodetect_and_save_projects(__get_full_path__(entry[1][0]))
        return True

    if 'add-mvn-project' in provided_special_cmds:
        entry = __get_entry_for_argument__(parsed_args, 'add-mvn-project')
        __check_args_available__(entry, ['project_key', 'path'])
        ProjectsDAO.add_mvn_project(project_key=entry[1][0], project_path=__get_full_path__(entry[1][1]))
        return True

    if 'add-script' in provided_special_cmds:
        entry = __get_entry_for_argument__(parsed_args, 'add-script')
        __check_args_available__(entry, ['project_key', 'path_to_exec'])
        ProjectsDAO.add_script(project_key=entry[1][0], project_path=__get_full_path__(entry[1][1]))
        return True

    if 'remove-project' in provided_special_cmds:
        entry = __get_entry_for_argument__(parsed_args, 'remove-project')
        __check_args_available__(entry, ['project_key'])
        ProjectsDAO.remove_project(project_key=entry[1][0])
        return True

    return False
