
class BST:
    def __init__(self, val=None):
        self.left_node = None
        self.right_node = None
        self.val = val

    def __str__(self):
        return "[%s, %s, %s]" % (self.left_node, str(self.val), self.right_node)

    def is_empty(self):
        return (self.left_node == self.right_node == self.val) is None

    def insert_search(self, val):
        if self.is_empty():
            self.val = val
        elif val == self.val:
            return val
        elif val < self.val:
            if self.left_node is None:
                self.left_node = BST(val)
            else:
                match = self.left_node.insert_search(val)
                return match
        else:
            if self.right_node is None:
                self.right_node = BST(val)
            else:
                match = self.right_node.insert_search(val)
                return match


input = open("test_2.txt")

input.close()

a = BST(4)
test = None
i = 0
vals = [2, 3, 7, 5, 2, 4]

while test is None:
    test = a.insert_search(vals[i])
    print(a)
    i += 1

print(test)
