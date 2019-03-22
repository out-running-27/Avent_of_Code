
def get_input(file):
    input = open(file)
    test = [x.strip() for x in input]
    input.close()
    return test

items = get_input('test.txt')

print(items)
