import argparse
import ProjectsDAO
import ProjectAutoDetector
from common import CustomAction


def append_buildins_commands(arg_parser):
    arg_parser.add_argument('-asc', '--autoscan', nargs='*', dest='autoscan', action=CustomAction)
    arg_parser.add_argument('-amp', '--add-mvn-project', nargs='*', dest='add-mvn-project', action=CustomAction)
    arg_parser.add_argument('-asrv', '--add-server', nargs='*', dest='add-server', action=CustomAction)
    arg_parser.add_argument('-rmp', '--remove-project', nargs='*', dest='remove-project', action=CustomAction)
    arg_parser.add_argument('-show', '--show-projects', nargs='?', dest='show-projects', action=CustomAction)


def run(parsed_args):
    #print parsed_args

    if 'ordered_args' not in dir(parsed_args):
        return False

    provided_special_cmds = [x[0] for x in parsed_args.ordered_args]

    if 'show-projects' in provided_special_cmds:
        ProjectsDAO.print_available_projects()

    if 'autoscan' in provided_special_cmds:
        entry = filter(lambda e: e[0] == 'autoscan', parsed_args.ordered_args)[0]
        print entry
        if len(entry) < 2 or len(entry[1][0]) < 1:
            raise Exception('Autoscan needs path argument')
        ProjectsDAO.autodetect_and_save_projects(entry[1][0])

    return False
