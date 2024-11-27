with open("input.txt") as file:
    # read end of file
    requests_lst = []
    for line in file:
        if line.strip() == "PRINTTREE":
            requests_lst.append(("PRINTTREE", None))
        else:
            node_1, node_2 = line.strip().split()
            requests_lst.append((node_1, int(node_2)))


class BinaryNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.key}"


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, key):
        if self.root is None:
            self.root = BinaryNode(key)
            return "DONE"
        else:
            # check if key is already in tree
            if not self.find(key):
                self._add(key, self.root)
                return "DONE"
            else:
                return "ALREADY"

    def _add(self, key, node):
        if key < node.key:
            if node.left is not None:
                self._add(key, node.left)
            else:
                node.left = BinaryNode(key)
        else:
            if node.right is not None:
                self._add(key, node.right)
            else:
                node.right = BinaryNode(key)

    def find(self, key):
        return self._find(key, self.root)

    def _find(self, key, node):
        if node is None:
            return False
        if key == node.key:
            return True
        if key < node.key:
            return self._find(key, node.left)
        else:
            return self._find(key, node.right)

    def print_tree(self):
        return self._print_tree(self.root)

    def _print_tree(self, node, level=0):
        result = ""
        if node is not None:
            result += self._print_tree(node.left, level + 1)
            result += "." * level + str(node.key) + "\n"
            result += self._print_tree(node.right, level + 1)
        return result


def build_tree(requests_lst):
    result = ""
    tree = BinaryTree()
    for node_1, node_2 in requests_lst:
        if node_1 == "PRINTTREE":
            result += tree.print_tree()
        elif node_1 == "ADD":
            result += tree.add(node_2) + "\n"
        elif node_1 == "SEARCH":
            result += "YES" + "\n" if tree.find(node_2) else "NO" + "\n"
        else:
            raise ValueError("Unknown request")
    return result


ans = build_tree(requests_lst)

with open("output.txt", "w") as file:
    file.write(str(ans))
