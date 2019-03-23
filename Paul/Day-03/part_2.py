import numpy as np
from ast import literal_eval


# gets input data from text file and returns it as a list
def get_input(file):
    input = open(file)
    test = [x.strip() for x in input]
    input.close()
    return test


# save input as list
claims = get_input('input.txt')

# create nxn matrix, 1200 is large enough for this problem
cloth = np.zeros((1200,1200), dtype=int)

# create empty list to record ids which do not have conflicts
claims_without_conflict = []

# for each claim parse input to get id, starting position, and size of rectangle
for claim in claims:
    # split string into claim info
    x = claim.split()
    # get id
    claim_id = int(x[0].replace('#', ''))
    # get starting position, @ 3,2: means 3 from left, 2 from top
    position_from_left, position_from_top = literal_eval(x[2].replace(':', ''))
    # get width and height from "5x4"
    width, height = literal_eval(x[3].replace('x', ','))

    # create set to store conflicts
    conflicts = set()

    # for each claim, record the id of the claim in the corresponding matrix
    # and add the claim to list of no conflicts
    claims_without_conflict.append(claim_id)

    for w in range(width):
        for h in range(height):
            # if claim has already been used, record claim to be deleted and continue checking for
            # more empty squares
            if cloth[position_from_top + h][position_from_left + w] == 0:
                cloth[position_from_top + h][position_from_left + w] = claim_id
            else:
                conflicts.add(cloth[position_from_top + h][position_from_left + w])
                conflicts.add(claim_id)

# delete claims from list which have conflicts
    for conflict in conflicts:
        if conflict in claims_without_conflict:
            claims_without_conflict.remove(conflict)

# print(cloth)
# print the one claim which does not have a conflict
print(claims_without_conflict)

