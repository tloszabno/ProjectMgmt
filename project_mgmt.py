#!/usr/bin/env python2

import sys
import os
import ActionsParser
import CommandExecutor
import Config
import BuildInFunctionRunner


def main():
    log_file_path = Config.logs_file_name_prefix + (str(os.getpid()) if Config.logs_file_append_pid else "")
    print "Starting, logs are in file [%s]\n\n" % log_file_path

    # buildins_runner = BuildInFunctionRunner.BuildInFunctionRunner()
    # buildins_runner.run()

    # if buildins_runner.was_ran():
    #    return

    action_parser = ActionsParser.ActionsParser()
    #  try:
    action_parser.parse(sys.argv[1:])
    if action_parser.try_invoke_buildins():
        return

    commands = action_parser.get_actions()
    CommandExecutor.process_commands(commands, log_file_path)
#    except Exception as e:
#       print "ERROR: " + str(e)



if __name__ == "__main__":
    main()
