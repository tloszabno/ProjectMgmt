logs_file_name_prefix = "/home/tomek/tmp/logs_"
logs_file_append_pid = True

projects_db_path = '/home/tomek/tmp/project_db.json'

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
    'util-parent': '/home/tomek/workspace/UTILS/util-parent',
    'nav': '/home/tomek/workspace/CORE/nav',
    'smart-core': '/home/tomek/workspace/SmartCORE/smart-core',
    'audit': '/home/tomek/workspace/CORE/audit',
    'acft': '/home/tomek/workspace/CORE/acft',
    'flight': '/home/tomek/workspace/CORE/flight',
    'svcreg': '/home/tomek/workspace/CORE/svcreg',

    'cdm-core': '/home/tomek/workspace/SmartDOC/cdm-core',
    'cdm-web': '/home/tomek/workspace/SmartDOC/cdm-web',
    'cdm-iface': '/home/tomek/workspace/SmartDOC/cdm-iface',
    'smart-doc': '/home/tomek/workspace/SmartDOC/smart-doc',
    'smart-doc-ear': '/home/tomek/workspace/SmartDOC/smart-doc-ear',
    'smart-doc-war': '/home/tomek/workspace/SmartDOC/smart-doc-war',
    'smart-doc-services-war': '/home/tomek/workspace/SmartDOC/smart-doc-war',
    'smart-doc-settings': '/home/tomek/workspace/SmartDOC/smart-doc-settings',
    'smart-doc-theme': '/home/tomek/workspace/SmartDOC/smart-doc-theme',

    'airline': '/home/tomek/workspace/CORE/airline',

    'ezy-portal-ear': '/home/tomek/workspace/EZY/ezy-portal-ear',
    'ezy-doc-ear': '/home/tomek/workspace/EZY/ezy-doc-ear',
    'ezy-portal-settings': '/home/tomek/workspace/EZY/ezy-portal-settings',
    'ezy-doc-settings': '/home/tomek/workspace/EZY/ezy-doc-settings',
    'ezy-core-ear': '/home/tomek/workspace/EZY/ezy-core-ear',

    'pax': '/home/tomek/workspace/CORE/pax',
    'bootstrap': '/home/tomek/workspace/BOOTSTRAPS/bootstrap',


    'smart-um': '/home/tomek/workspace/UM/smart-um',

    'crew': '/home/tomek/workspace/CORE/crew'

}
