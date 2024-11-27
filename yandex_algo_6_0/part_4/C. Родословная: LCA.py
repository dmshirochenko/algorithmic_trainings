import sys

sys.setrecursionlimit(100000)

with open("input.txt") as file:
    n = int(file.readline())
    parents = []
    set_of_possible_parents = set()
    for i in range(n - 1):
        child, parent = file.readline().split()
        parents.append((child, parent))
        set_of_possible_parents.add(parent)

    # read end of file
    requests_lst = []
    for line in file:
        node_1, node_2 = line.split()
        requests_lst.append((node_1, node_2))


class Node:
    def __init__(self, name, parent=None):
        self.name = name
        self.level = 0
        self.parent = parent
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def add_parent(self, parent):
        self.parent = parent

    def set_level(self, level):
        self.level = level

    def __str__(self):
        return f"{self.name} {self.level} parent {self.parent.name if self.parent else None}"


def build_tree(parents, set_of_possible_parents):
    nodes = {}
    for child, parent in parents:
        set_of_possible_parents.discard(child)
        if child not in nodes:
            nodes[child] = Node(child)
        if parent not in nodes:
            nodes[parent] = Node(parent)
        nodes[child].add_parent(nodes[parent])
        nodes[parent].add_child(nodes[child])

    root_parent_name = set_of_possible_parents.pop()
    return nodes, root_parent_name


def set_levels_from_root(node, level):
    node.set_level(level)
    for child in node.children:
        set_levels_from_root(child, level + 1)


def find_lca(nodes_trees, node_1, node_2):
    if node_1.level < node_2.level:
        node_1, node_2 = node_2, node_1
    while node_1.level > node_2.level:
        node_1 = node_1.parent
    while node_1 != node_2:
        node_1 = node_1.parent
        node_2 = node_2.parent
    return node_1


def print_tree_structure(node, level):
    print(" " * level, node)
    for child in node.children:
        print_tree_structure(child, level + 1)


nodes_trees, root_parent_name = build_tree(parents, set_of_possible_parents)
print_tree_structure(nodes_trees[root_parent_name], 0)
set_levels_from_root(nodes_trees[root_parent_name], 0)

ans = []
for node_1_name, node_2_name in requests_lst:
    node_1 = nodes_trees[node_1_name]
    node_2 = nodes_trees[node_2_name]
    lca = find_lca(nodes_trees, node_1, node_2)
    ans.append(lca.name)

with open("output.txt", "w") as file:
    for name in ans:
        file.write(f"{name}\n")
