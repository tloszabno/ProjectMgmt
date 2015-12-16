import subprocess
import Projects
import CommandsResolver


def process_commands(commands, logs_file_path):
    map(process_command, commands, logs_file_path)


def process_command(command, logs_file_path):
    action_cmd = CommandsResolver.resolve_final_bash_command(command)
    module_path = Projects.projects_path[command.target_module]

    process = subprocess.Popen([action_cmd], cwd=module_path, stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT, shell=True)

    log_msg = "Started command %s on module %s (%s) - pid: %d" % (action_cmd, command.target_module,
                                                                  module_path, process.pid)
    print log_msg
    out2 = ""
    with open(logs_file_path, 'w') as f:
        f.write(log_msg + "\n\n")
        while True:
            line = process.stdout.readline()
            if line == '':
                break
            f.write(line.rstrip() + "\n")
            out2 += line.rstrip() + "\n"

    out, _ = process.communicate()  # wait
    if process.returncode != 0:
        print "\t[FAIL]"
        print out2
        exit(1)

    print "\t[OK]"
