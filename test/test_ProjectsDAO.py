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
            'project1': '/home/test/project1',
            'project2': '/home/test/project2',
            'project3': '/home/test/project3'
        }

    def test_saveJson(self):
        ProjectsDAO.save_projects(self.create_projects_obj(), db_path=test_db)
        with open(test_db, "r") as db:
            obj = json.load(db)
            self.assertEquals(obj["project1"], '/home/test/project1')
            self.assertEquals(obj["project2"], '/home/test/project2')
            self.assertEquals(obj["project3"], '/home/test/project3')

    def test_load(self):
        ProjectsDAO.save_projects(self.create_projects_obj(), db_path=test_db)
        read = ProjectsDAO.get_projects(db_path=test_db)
        self.assertEquals(read["project1"], '/home/test/project1')
        self.assertEquals(read["project2"], '/home/test/project2')
        self.assertEquals(read["project3"], '/home/test/project3')