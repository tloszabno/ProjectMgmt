import argparse
import Config
import argcomplete


class Action(object):
    acceptable_keys_list = ['target_module', 'action', 'arguments']

    def __init__(self, **kwargs):
        for k in kwargs.keys():
            if k in Action.acceptable_keys_list:
                self.__setattr__(k, kwargs[k])
            else:
                raise Exception('Action object does not support ' + k + ' argument')

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __str__(self):
        return "@Action=[%s]" % str(self.__dict__)


class CustomAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if 'ordered_args' not in namespace:
            setattr(namespace, 'ordered_args', [])
        previous = namespace.ordered_args
        previous.append((self.dest, values))
        setattr(namespace, 'ordered_args', previous)


class ActionsParser(object):
    def __init__(self):
        self.arg_parser = argparse.ArgumentParser()
        argcomplete.autocomplete(self.arg_parser)
        self.__configure_parser__()

    def __configure_parser__(self):
        for command_key in Config.actions.keys():
            self.arg_parser.add_argument('-' + Config.actions[command_key][0], '--' + command_key,
                                         nargs='*', dest=command_key, action=CustomAction)

    def get_commands(self, args):
        parsed = self.arg_parser.parse_args(args)
        actions = []
        last_used_mods = []
        for (action_key, modules) in parsed.ordered_args:
            arguments = map(lambda arg: arg[1:], filter(lambda arg: arg[0] == '@', modules))
            action_modules = filter(lambda mod: mod[0] != '@', modules)
            if len(action_modules) == 0:
                if len(last_used_mods) == 0:
                    raise Exception("None module pressed")
                action_modules = last_used_mods
            else:
                last_used_mods = action_modules

            for module in action_modules:
                actions.append(Action(target_module=module, action=action_key, arguments=arguments))
        return actions

