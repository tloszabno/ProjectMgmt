import ConfigUtils



projects_db_path = '/home/tomek/workspace/project_db.json'

logs_file_name_prefix = "/home/tomek/logs/logs_" + ConfigUtils.get_datetime_prefix() + "_"
logs_file_append_pid = True

# autoscan
autoscan_server_runnable_files = ['app_server.sh', 'standalone.sh']
autoscan_folders_to_skip = ['target', 'tests', 'standalone', 'glassfish', 'ACA']

actions = {
    'clean-build': ('cb', 'mvn clean install'),
    'clean-build2': ('cb2', 'mvn2 clean install'),
    'clean-build3': ('cb3', 'mvn3 clean install'),
    'mvn': ('m', 'mvn {0} install', ['']),

    'reset-hard': ('rh', 'git reset --hard && git checkout {0} && git fetch && git reset --hard origin/{0}',
                   ['master']),

    'apply-new-code': ('anc', 'git add -A && git stash && git fetch && git reset --hard origin/{0} && git stash apply',
                       ['master']),

    'run': ('r', '{0}', []),
    'deploy-full': ('dep', '{0} undeploy && {0} stop && {0} clean && {0} deploy', []),
    'deploy-full-debug': ('depd', '{0} undeploy && {0} stop && {0} clean && DEBUG=1 {0} deploy', [])

}

continue_on_fail = False
