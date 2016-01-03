#!/usr/bin/env python
import sys
import unittest
import logging

sys.path.append('..')
import ProjectsDAO
import json
import os
import shutil

test_dir = "tmp"
test_db = "tmp/tmp_test_project_db.json"


class TestProjectsDAO(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(stream=sys.stderr)
        self.log = logging.getLogger("TestProjectsDAO")
        if os.path.isdir(test_dir):
            shutil.rmtree(test_dir)
        os.mkdir(test_dir)

    def tearDown(self):
        if os.path.isdir(test_dir):
            shutil.rmtree(test_dir)

    def create_projects_obj(self):
        return {
            'project1': {'path': '/home/tests/project1', 'type': "mvn_project"},
            'project2': {'path': '/home/tests/project2', 'type': "mvn_project"},
            'project3': {'path': '/home/tests/project3', 'type': "mvn_project"}
        }

    def test_saveJson(self):
        ProjectsDAO.save_projects(self.create_projects_obj(), db_path=test_db)
        with open(test_db, "r") as db:
            obj = json.load(db)
            self.assertEquals(obj["project1"],  {'path': '/home/tests/project1', 'type': "mvn_project"})
            self.assertEquals(obj["project2"],  {'path': '/home/tests/project2', 'type': "mvn_project"})
            self.assertEquals(obj["project3"],  {'path': '/home/tests/project3', 'type': "mvn_project"})

    def test_load(self):
        ProjectsDAO.save_projects(self.create_projects_obj(), db_path=test_db)
        read = ProjectsDAO.get_projects(db_path=test_db)
        self.assertEquals(read["project1"],  {'path': '/home/tests/project1', 'type': "mvn_project"})
        self.assertEquals(read["project2"],  {'path': '/home/tests/project2', 'type': "mvn_project"})
        self.assertEquals(read["project3"],  {'path': '/home/tests/project3', 'type': "mvn_project"})

    def test_add(self):
        ProjectsDAO.save_projects(self.create_projects_obj(), db_path=test_db)

        ProjectsDAO.add_project('append', '/home/append', 'mvn_project', db_path=test_db)

        read = ProjectsDAO.get_projects(db_path=test_db)
        self.assertEquals(read["project1"],  {'path': '/home/tests/project1', 'type': "mvn_project"})
        self.assertEquals(read["project2"],  {'path': '/home/tests/project2', 'type': "mvn_project"})
        self.assertEquals(read["project3"],  {'path': '/home/tests/project3', 'type': "mvn_project"})
        self.assertEquals(read["append"],  {'path': '/home/append', 'type': "mvn_project"})
