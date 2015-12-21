import os
import Config


def scan_folder(folder_to_scan):
    servers = scan_for_servers_runnable_files(folder_to_scan, server_runnable_files=Config.server_runnable_files,
                                              folders_to_skip=Config.folders_to_skip)
    mvn_projects = scan_for_mvn_projects(folder_to_scan, Config.folders_to_skip)

    result = {}
    for mvn_project in mvn_projects:
        project_key = __resolve_project_key__(mvn_project, result)
        result[project_key] = {'path': mvn_project, 'type': 'mvn_project'}

    for server in servers:
        server_key = __resolve_server_key__(server, result)
        result[server_key] = {'path': server, 'type': 'server'}


def scan_for_mvn_projects(folder_to_scan, folders_to_skip=[]):
    possible_locations = []

    for dir_path, sub_folders, file_list in os.walk(folder_to_scan):
        if len(filter(lambda not_allowed_dir: dir_path.endswith(not_allowed_dir), folders_to_skip)) > 0:
            continue
        if 'pom.xml' in file_list:
            project_path = os.path.abspath(dir_path)
            possible_locations.append(project_path)
            if __is_project_multi_module__(project_path):
                folders_to_skip += (map(lambda sub_folder: os.path.join(dir_path, sub_folder), sub_folders))

    return possible_locations


def __is_project_multi_module__(project_path):
    with open(os.path.join(project_path, "pom.xml")) as pom:
        return "<modules>" in pom.read()


def scan_for_servers_runnable_files(folder_to_scan, server_runnable_files=Config.server_runnable_files,
                                    folders_to_skip=[]):
    found = []
    for dir_path, sub_folders, file_list in os.walk(folder_to_scan):
        if len(filter(lambda not_allowed_dir: dir_path.endswith(not_allowed_dir), folders_to_skip)) > 0:
            continue
        runnable_server_file_in_folder = list(set(file_list).intersection(server_runnable_files))
        if len(runnable_server_file_in_folder) > 0:
            found.append(os.path.join(dir_path, runnable_server_file_in_folder[0]))
    return found


def __resolve_project_key__(mvn_project_path, current_state):
    potential_name = os.path.basename(mvn_project_path)

    if potential_name in current_state.keys():
        conflicted_path = current_state[potential_name]
        del current_state[potential_name]

        print "During the scan found project with same key as project added. So please provide keys for both project:"
        conflicted_project_key = raw_input("Provide name for project in path %s" % conflicted_path)
        current_state[conflicted_project_key] = conflicted_path
        potential_name = raw_input("Provide name for project in path %s" % mvn_project_path)

    return potential_name


def __resolve_server_key__(server_path, current_state):
    potential_name = os.path.basename(server_path)

    if potential_name in current_state.keys():
        conflicted_path = current_state[potential_name]
        del current_state[potential_name]

        print "During the scan found server with same key as project added. So please provide keys for both servers:"
        conflicted_server_key = raw_input("Provide name for server in path %s" % conflicted_path)
        current_state[conflicted_server_key] = conflicted_path
        potential_name = raw_input("Provide name for server in path %s" % server_path)

    return potential_name
