"""
    Advent of Code Day 6 challenge:

    Part 1:
        Given a list of coordinates of the form (x, y) where
            x is the number of units from the left
            y is the number of units from the top

        Determine the area around each coordinate by finding the number of (x, y) locations that are closest
        to that coordinate, by using the Manhattan Distance

        The goal is to find the largest area that is fully contained by other points

"""

from ast import literal_eval
import numpy as np
import argparse
import math


class Coordinate:
    """
        Coordinate class
            input tuple containing x, y value of coordinate
                ie. (1,2)
            x -> position from left of matrix, positive integers only, columns
            y -> position from the top of the matrix, positive integers only, rows
    """
    def __init__(self, position):
        self.x = position[0]
        self.y = position[1]

    def compute_distance(self, new_coordinate):
        """
        Compute Manhattan Distance between two coordinates
        This is evaluated by taking difference in x values + the difference in y values
        (1, 3) and (3, 5) has a Manhattan Distance of 4 because:
            |1-3| + |3 - 5| = 4
        """
        return abs(self.x - new_coordinate.x) + abs(self.y - new_coordinate.y)

    def is_edge_point(self, num_rows, num_cols):
        """
            determine if the coordinate is an edge point
            num_rows -> bottom most row in matrix
            num_cols -> right most column in matrix
        """
        return self.x == 0 or self.x == num_cols - 1 or self.y == 0 or self.y == num_rows - 1

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name", help="input file listing coordinates for analysis")
    args = parser.parse_args()
    return args.file_name


def read_input(file):
    """
        read in input text file, which is a string of coordinates in the following format:
            1, 1
            1, 6
            8, 3

        file -> input text file
        returns dict of coordinate objects
    """
    # if file is None:
    #     raise Exception("File Not Found")
    input_file = open(file, "r")
    return {id: Coordinate(literal_eval(position.strip())) for id, position in enumerate(input_file, 1)}


def find_matrix_size(coordinates):
    """
        This finds the maximum x and y values from the list of coordinates

        coordinates -> dict of coordinate objects
        returns max x and y values, plus 1 added space because of 0 indexing
    """
    max_x = 0
    max_y = 0
    for key, coordinate in coordinates.items():
        if coordinate.x > max_x:
            max_x = coordinate.x
        if coordinate.y > max_y:
            max_y = coordinate.y
    return max_y+1, max_x+1


def populate_matrix(matrix, coordinate_dict):
    """
        loops through each position on matrix, and calculates the closed coordinate from input coordinates
        modifies the matrix in place with the ID if the closed input coordinate.
        if two points are of equal distance, 0 is recorded for that position

        the function also determines the ids of points which are located on the edge of the matrix
        these are considered to have infinite areas and need to be discarded from future analysis

        matrix -> NxM np.array being modified with the closest points
        coordinate_dict -> dict of input coordinates
        returns set of edge points
    """
    # get matrix size
    rows, columns = matrix.shape

    # create set of edge points
    edge_points = set()

    for row in range(rows):
        for column in range(columns):
            # generate new coordinate, x=column, y=row
            my_coordinate = Coordinate((column, row))

            # create variable to keep track of closest point, and if another point is of equal distance
            closest_distance = math.inf
            unique_point = 0

            # compute Manhattan Distinct between each input point, record closest point
            for key, coordinate in coordinate_dict.items():
                distance = my_coordinate.compute_distance(coordinate)
                if distance < closest_distance:
                    closest_distance = distance
                    unique_point = key
                elif distance == closest_distance:
                    unique_point = 0

            matrix[row][column] = unique_point

            if unique_point != 0 and my_coordinate.is_edge_point():
                edge_points.add(unique_point)

    return edge_points


def calculate_area(matrix, coordinate_dict, edge_list):
    """
    Finds the largest area of a fully enclosed coordinate

    matrix -> NxM np.array which lists the ids of coordinates closest to the input coordinates
    coordinate_dict -> dict of input coordinates
    edge_list -> set containing elements
    returns the maximum area of input coordinate not listed in the edge_list
    """
    max_key, max_area = 0, 0
    for key in coordinate_dict:
        if key not in edge_list:
            area = np.count_nonzero(matrix == key)
            if area > max_area:
                max_area = area
                max_key = key
    return max_area, max_key


def main(file):
    """
        The magic happens here
    """

    # read in input and calculate the size of matrix needed
    coordinates = read_input(file)
    rows, columns = find_matrix_size(coordinates)

    # create 2 dimensional matrix for coordinates
    matrix = np.zeros((rows, columns), dtype=int)

    # loop through each position on matrix, and record id of nearest point
    # returns a set of ids which have "infinite areas"
    edges = populate_matrix(matrix, coordinates)

    print(matrix)
    print(edges)

    # calculate the area of each fully enclosed coordinate
    max_area, max_key = calculate_area(matrix, coordinates, edges)

    print("the largest area which is not infinite is {} and belongs to point {}.".format(max_area, max_key))


if __name__ == "__main__":
    arg_file_name = parse_args()
    try:
        main(arg_file_name)
    except FileNotFoundError:
        print("the file does not exist")
