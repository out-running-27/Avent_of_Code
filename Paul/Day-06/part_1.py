"""
    Type up explanation of the problem
    TODO
"""


class Coordinate():
    """
        Coordinate class
            x -> position from left of matrix, positive integers only
            y -> position from the top of the matrix, positive integers only
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def compute_distance(self, new_coordinate):
        """
            Compute Manhattan Distance between two coordinates
        """
        pass

    def plot_coordinate(self, matrix):
        """
            plot coordinate on matrix
        """
        pass


def read_input(file):
    """
        read in input text file, which is a string of coordinates in the following format:
            1, 1
            1, 6
            8, 3
    """
    input = open(file, "r")
    # coordinates = [coordinate.strip() for coordinate in input]
    for i in input:


