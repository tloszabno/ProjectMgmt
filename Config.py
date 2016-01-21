def get_datetime_prefix():
    import datetime
    return datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')


logs_file_name_prefix = "/home/tomek/logs/logs_" + get_datetime_prefix() + "_"
logs_file_append_pid = True

projects_db_path = '/home/tomek/workspace/project_db.json'

# autoscan
autoscan_server_runnable_files = ['app_server.sh', 'standalone.sh']
autoscan_folders_to_skip = ['target', 'tests', 'standalone', 'glassfish', 'ACA']

actions = {
    'clean-build': ('cb', 'mvn clean install'),
    'clean-build2': ('cb2', 'mvn2 clean install'),
    'clean-build3': ('cb3', 'mvn3 clean install'),
    'mvn': ('m', 'mvn {0} install', ['']),
    'get-new-code': ('gc', 'git reset --hard && git checkout {0} && git fetch && git reset --hard origin/{0}',
                     ['master']),
    'run': ('r', '{0}', []),
    'deploy-core-full': ('dcf', '{0} undeploy && {0} stop && {0} clean && {0} deploy', [])
}

continue_on_fail = False
