def get_input(file):
    input = open(file)
    test = [x.strip() for x in input]
    input.close()
    return test

def compare_strings(i, j):
    return i.lower() == j.lower() and not (i.islower() == j.islower())

polymer = list(str(get_input("input.txt"))[2:-2])
i = 0

#print(polymer)

while i < len(polymer)-1:
    # print(polymer[i], polymer[i+1])
    if compare_strings(polymer[i], polymer[i+1]):
        del(polymer[i:i+2])
        if i != 0:
            i -= 1
    else:
        i += 1
    if i % 1000 == 0:
        print(i)
    # print("index = {}, current polymer = {}".format(i, polymer))

print("the polymer has a length of {}".format(len(polymer)))
