#!/usr/bin/env python2

import sys
import os
import ActionsParser
import CommandExecutor
import Config
import traceback
import Validation


def main():
    log_file_path = Config.logs_file_name_prefix + (str(os.getpid()) if Config.logs_file_append_pid else "")
    print "Starting, logs are in file [%s]\n\n" % log_file_path

    action_parser = ActionsParser.ActionsParser()
    try:
        action_parser.parse(sys.argv[1:])
        if action_parser.try_invoke_buildins():
            return

        commands = action_parser.get_actions()
        Validation.validate_modules_exists(commands)
        CommandExecutor.process_commands(commands, log_file_path)

    except Exception as e:
        print "ERROR: " + str(e)


if __name__ == "__main__":
    main()
