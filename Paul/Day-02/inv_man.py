
def get_input(file):
    input = open(file)
    test = [x.strip() for x in input]
    input.close()
    return test


def two_or_three_letters(list):
    letters = {}
    for l in list:
        if l in letters:
            letters[l] += 1
        else:
            letters[l] = 1
    return 2 in letters.values(), 3 in letters.values()


boxes = get_input("input.txt")
two_letter_boxes, three_letter_boxes = 0, 0

for box in boxes:
    is_two, is_three = two_or_three_letters(box)
    two_letter_boxes += is_two
    three_letter_boxes += is_three

print("The boxes return {} two letter, {} three letter, for a checkum of {}".format(two_letter_boxes, three_letter_boxes, 
        two_letter_boxes * three_letter_boxes ))