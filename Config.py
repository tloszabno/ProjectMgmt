logs_file_name_prefix = "/home/tomek/tmp/logs_"
logs_file_append_pid = True

# optimize actions to one dic

actions = {
    'clean-build': ('cb', 'mvn clean install'),
    'clean-build2': ('cb2', 'mvn2 clean install'),
    'clean-build3': ('cb3', 'mvn3 clean install'),
    'mvn': ('m', 'mvn {0} install', ['']),
    'get-new-code': ('gc', 'git reset --hard && git checkout {0} && git fetch && git reset --hard origin/{0}',
                     ['master'])
}


# TODO add autoscan
projects_paths = {
    

}
