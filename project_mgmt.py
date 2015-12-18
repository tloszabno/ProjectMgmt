#!/usr/bin/env python2

import sys
import os

import CommandParser
import CommandExecutor
import Config


def main():
    log_file_path = Config.logs_file_name_prefix + (str(os.getpid()) if Config.logs_file_append_pid else "")
    print "Starting, logs are in file [%s]\n\n" % log_file_path
    try:
        command_parser = CommandParser.CommandParser()
        commands = command_parser.get_commands(sys.argv[1:])
        CommandExecutor.process_commands(commands, log_file_path)
    except Exception as e:
        print "ERROR: " + str(e)


if __name__ == "__main__":
    main()
