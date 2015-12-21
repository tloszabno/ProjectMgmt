#!/usr/bin/env python
import sys
import unittest

sys.path.append('..')
import logging
import ProjectAutoDetector

folder_to_scan = "simple_workspace"


class TestProjectAutoDetector(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(stream=sys.stderr)
        self.log = logging.getLogger("TestProjectAutoDetector")

    def test_simple_scan_for_mvn_projects(self):
        found = ProjectAutoDetector.scan_for_mvn_projects(folder_to_scan)

        project_to_found = ['folder1/multimodule_project',
                            'folder1/project_a',
                            'folder1/project_to_skip',
                            'project_a']

        self.assertEquals(len(found), len(project_to_found), "Wrong number of project found=> %s" % str(found))

        for found_project in found:
            if len(filter(lambda ptf: found_project.endswith(ptf), project_to_found)) == 0:
                self.assertTrue(False, "expected projects not found [%s]" % found_project)

    def test_scan_with_skip(self):
        found = ProjectAutoDetector.scan_for_mvn_projects(folder_to_scan, folders_to_skip=['project_to_skip'])
        self.assertEquals(filter(lambda f: f.endswith('project_to_skip'), found), [])

    def test_found_servers(self):
        found = ProjectAutoDetector.scan_for_servers_runnable_files(folder_to_scan, ['app_server.sh'])
        self.assertEquals(len(found), 1, "Server not found")
        if not found[0].endswith('simple_workspace/folder1/multimodule_project/server/app_server.sh'):
            self.assertTrue(False, "Wrong server found, found=%s" % str(found))
