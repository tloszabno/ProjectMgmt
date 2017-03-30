import argparse
import Config
import BuildInFunctionRunner
from common import Action
from common import CustomAction
import ProjectsDAO


class ActionsParser(object):
    def __init__(self):
        self.arg_parser = argparse.ArgumentParser()
        self.__configure_parser__()
        self.parsed = None

    def __configure_parser__(self):
        for command_key in Config.actions.keys():
            self.arg_parser.add_argument('-' + Config.actions[command_key][0], '--' + command_key,
                                         nargs='*', dest=command_key, action=CustomAction)
        BuildInFunctionRunner.append_buildins_commands(self.arg_parser)

    def parse(self, args):
        self.parsed = self.arg_parser.parse_args(args)

    def get_actions(self):
        actions = []
        last_used_mods = []
        if 'ordered_args' not in dir(self.parsed):
            self.arg_parser.parse_args(['-h'])
            return
        for (action_key, modules) in self.parsed.ordered_args:
            arguments = map(lambda arg: arg[1:], filter(lambda arg: arg[0] == '@', modules))
            action_modules = filter(lambda mod: mod[0] != '@', modules)
            if len(action_modules) == 0:
                if len(last_used_mods) == 0:
                    raise Exception("None module pressed")
                action_modules = last_used_mods
            else:
                if "all" in action_modules:
                    action_modules = [x[0] for x in ProjectsDAO.get_projects().items() if x[1]['type'] == 'mvn_project']
                last_used_mods = action_modules

            for module in action_modules:
                actions.append(Action(target_module=module, action=action_key, arguments=arguments))
        return actions

    def try_invoke_buildins(self):
        return BuildInFunctionRunner.run(self.parsed)
