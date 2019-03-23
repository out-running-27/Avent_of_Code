
import numpy as np
from ast import literal_eval


def get_input(file):
    input = open(file)
    test = [x.strip() for x in input]
    input.close()
    return test

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

    for w in range(size[1]):
        for h in range(size[0]):
            n[pos[0]+h][pos[1]+w] += 1

# print(n)

# count number of overlapping claims
print("the number of overlapping claims are {}.".format((n >= 2).sum()))


