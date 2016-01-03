import argparse
import ProjectsDAO
import ProjectAutoDetector

class BuildInFunctionRunner(object):
    def __init__(self):
        self.arg_parser = argparse.ArgumentParser()
        self.__configure_parser__()

    def __configure_parser__(self):
        self.arg_parser.add_argument('--autoscan', )
