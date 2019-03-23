"""
    Explain problem.
    Provide a description of what this does
    Call out dependencies (if no requirements.txt is provided)

    TODO: write unit tests
"""

import numpy as np
import unittest
from ast import literal_eval
import logging

"""
    Claim represent a matrix that an elf has made a claim on
    TODO: add more details on each variable
"""
class Claim:
    def __init__(self, start_pos_x, start_pos_y, size_width, size_height):
        self.start_pos_x = start_pos_x
        self.start_pos_y = start_pos_y
        self.size_width = size_width
        self.size_height = size_height


"""
    read an input file amd returns the content
"""
def get_input(file):
    # TODO: Other types of validation
    if file is None:
        raise("File Not Found")
    input = open(file)
    test = [x.strip() for x in input]
    input.close()
    return test


"""
    Generic function for handling errors
"""
def handle_error(x):
    log.error(x)

    # we can do more cleanup here if needed

"""
    Increment each index in the given matrix based on claim.
    TODO: Describe the variable
"""
def process_claim(claim, matrix):
    log.info("Start processing Claim")

    log.info("Finished processing Claim")


"""
        # TODO: Other types of validationSet up logging and anything else
"""
def initialize(args):
    # set up a global variable for logging
    # use globals sparingly - please
    global log

    # Set logging
    FORMAT = '%(asctime) - %(level)s - %(message)s'
    logging.basicConfig(format=FORMAT, setLevel="INFO")
    log = logging.getLogger('root')


"""
    Set up command line arguments and return
"""
def parse_args():
    # TODO: read in command-line arguments and return them

"""
    Main method where all the action happens
"""
def main(args):
    # get claims data
    claims = get_input("input.txt")

    # build an array of zeros
    n = np.zeros((1200, 1200), dtype=int)

    # add one to array for every claim
    # find starting point
    # add one to each height and width position of the rectangle
    for claim in claims:
        x = claim.split()
        pos = literal_eval(x[2].replace(':', ''))
        size = literal_eval(x[3].replace('x', ','))
        
        my_claim = Claim(pos[0],pos[1), size[1],size[0])
        
        process_claim(my_claim)


        # Move this to the other method
        # looping through each index
        for w in range(size[1]):
            for h in range(size[0]):
                n[pos[0]+h][pos[1]+w] += 1

    # print(n)

    # count number of overlapping claims
    print("the number of overlapping claims are {}.".format((n >= 2).sum()))

if __name__ == "main":
    args = parse_args()
    initalize(args)
    try:
        main(args)
    except Exception e:
        handle_error(e)
