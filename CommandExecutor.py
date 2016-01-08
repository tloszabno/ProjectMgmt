import subprocess
import ProjectsResolver
import CommandsResolver
import os


def process_commands(commands, logs_file_path):
    map(lambda cmd: process_command(cmd, logs_file_path),
        commands)


def __resolve_working_dir__(path):
    return path if os.path.isdir(path) else os.path.dirname(path)


def process_command(command, logs_file_path):
    module_path, module_type = ProjectsResolver.get_project_path_and_type(command.target_module)
    if module_type == 'script':
        command.arguments = [module_path]

    action_cmd = CommandsResolver.resolve_final_bash_command(command)

    cwd = __resolve_working_dir__(module_path)

    process = subprocess.Popen([action_cmd], cwd=cwd, stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT, shell=True)

    log_msg = "Started command [%s] on module [%s] (%s) - pid: %d\n" % (action_cmd,
                                                                        command.target_module, module_path, process.pid)
    print log_msg
    out2 = ""
    with open(logs_file_path, 'a') as f:
        f.write(log_msg + "\n\n")
        while True:
            line = process.stdout.readline()
            if line == '':
                break
            f.write(line.rstrip() + "\n")
            f.flush()
            out2 += line.rstrip() + "\n"

    process.wait()
    if process.returncode != 0:
        print "\t[FAIL]"
        print out2
        exit(1)

    print "\t[OK]"
