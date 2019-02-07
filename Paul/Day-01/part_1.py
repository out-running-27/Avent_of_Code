
input = open("input.txt")

test = [int(x.strip()) for x in input]

print(sum(test))

input.close()