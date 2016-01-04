import argparse


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
