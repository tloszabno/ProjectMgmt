#!/usr/bin/env python
import sys
import unittest

sys.path.append('..')
import ActionsParser
import logging


class TestParserForCommands(unittest.TestCase):
    def setUp(self):
        self.parser = ActionsParser.ActionsParser()
        logging.basicConfig(stream=sys.stderr)
        self.log = logging.getLogger("test_CommandParser")

    def test_init(self):
        self.assertIsNotNone(self.parser)

    def test_one_command_few_projects(self):
        test_args = '-gc module1 module2'.split()
        result_should_be = [ActionsParser.Action(action='get-new-code', target_module=module_name, arguments=[])
                            for module_name in ['module1', 'module2']]
        obtained_commands = self.parser.get_commands(test_args)
        self.assertEquals(obtained_commands, result_should_be)

    def test_one_command_few_projects_and_attribute(self):
        test_args = '-gc module1 module2 @-U'.split()
        result_should_be = [ActionsParser.Action(action='get-new-code', target_module=module_name, arguments=['-U'])
                            for module_name in ['module1', 'module2']]
        obtained_commands = self.parser.get_commands(test_args)
        self.assertEquals(obtained_commands, result_should_be)

        test_args = '-gc module1 module2 @-U @-X'.split()
        result_should_be = [ActionsParser.Action(action='get-new-code',
                            target_module=module_name, arguments=['-U', '-X'])
                            for module_name in ['module1', 'module2']]
        obtained_commands = self.parser.get_commands(test_args)
        self.assertEquals(obtained_commands, result_should_be)

    def test_two_command_few_projects_once_declared(self):
        test_args = '-gc module1 module2 -cb'.split()
        result_should_be = [ActionsParser.Action(action='get-new-code', target_module=module_name, arguments=[])
                            for module_name in ['module1', 'module2']] + \
                           [ActionsParser.Action(action='clean-build', target_module=module_name, arguments=[])
                            for module_name in ['module1', 'module2']]

        obtained_commands = self.parser.get_commands(test_args)
        self.assertEquals(obtained_commands, result_should_be)

    def test_two_command_none_project_declared(self):
        test_args = '-gc -cb'.split()
        with self.assertRaises(Exception):
            self.parser.get_commands(test_args)

    def test_two_command_project_declared_too_late(self):
        test_args = '-gc -cb mod1 mod2'.split()
        with self.assertRaises(Exception):
            self.parser.get_commands(test_args)


if __name__ == '__main__':
    unittest.main()
