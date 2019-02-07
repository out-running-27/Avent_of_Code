from sortedcontainers import SortedSet

class BST:
    def __init__(self, val=None):
        self.left_node = None
        self.right_node = None
        self.val = val
    
    def __str__(self):
        return "[%s, %s, %s]" % (self.left_node, str(self.val), self.right_node)

    def search_insert(self, val):
        if self.val == val:
            return val
        elif self.val == None:
            self.val = val
        elif self.val > val:
            if self.left_node is None:
                self.left_node = BST(val)
            else:
                match = self.left_node.search_insert(val)
                return match
        else:
            if self.right_node is None:
                self.right_node = BST(val)
            else:
                match = self.right_node.search_insert(val)
                return match


input = open("input.txt")
test = [int(x.strip()) for x in input]
input.close()

run_tot = 0
i = 0
freq = None
items = SortedSet()

while freq is None:
    for j in test:
        run_tot += j
        if run_tot in items:
            print("THERE'S A HIT!!")
            freq = run_tot
            break
        items.add(run_tot)
        # freq = tree.search_insert(run_tot)
        # print(run_tot)
    i += 1

print("The frequency {} appears twice first after {} iterations".format(freq, i))
