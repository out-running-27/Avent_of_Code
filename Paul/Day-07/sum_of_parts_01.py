"""
    Day 07 - Advent of Code:

        This challenge requires building a dependency graph

        TODO explain more
"""

import argparse
import logging
from sortedcontainers import SortedSet
import itertools


class Instruction:
    """
        An instruction is a
    """

    def __init__(self, name):
        self.name = name
        self.dependencies = set()

    def add_dependency(self, dependency):
        """
        Adds instruction to set of dependencies which must complete before current instruction

        :param dependency: instruction which precedes current instruction
        :return: None
        """
        self.dependencies.add(dependency)


def initialize(level="INFO"):
    """
        Set up logging and any other processes
    """

    # Set up a global variable for logging
    global log

    # Set logging
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
                        level=level)
    log = logging.getLogger('root')


# def handle_error(x):
#     """
#         Generic function for handling errors
#
#     :param x: error message recorded
#     :return: None
#     """
#     log.error(x)

def read_args():
    """
    The program should be run with one argument, file_name which is a text file listing dependencies of
    instructions

    :return: The name of the file
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name", help="the input file to be read")
    args = parser.parse_args()
    return args.file_name


def get_input(file):
    """
    This function parses a text file listing instructions of the following format:
        Step C must be finished before step A can begin.
        Step C must be finished before step F can begin.

    It builds a dependency list of tuples in the following format:
        [(C, A),(C, F) ... ]

    :param file: text file of instructions
    :return: list of tuples showing the dependencies of instructions
    """
    log.info("reading text file: {}".format(file))
    with open(file, "r") as input_file:
        dependency_list = []
        for i in input_file:
            j = i.split()
            dependency_list.append((j[1], j[7]))
        log.info("Completed building dependency list")
        return dependency_list


def main(file):
    dependency_list = get_input(file)

    # create set of unique instructions
    merged = SortedSet(itertools.chain(*dependency_list))


    print(merged)


if __name__ == "__main__":
    file_name = read_args()
    initialize()
    # try:
    main(file_name)
    # except Exception e:
    #     handle_error(e)
