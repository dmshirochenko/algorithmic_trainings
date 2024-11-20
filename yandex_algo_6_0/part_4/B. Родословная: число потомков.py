import sys

sys.setrecursionlimit(100000)

with open('input.txt') as file:
    n = int(file.readline())
    parents = []
    set_of_possible_parents = set()
    for i in range(n-1):
        child, parent = file.readline().split()
        parents.append((child, parent))
        set_of_possible_parents.add(parent)

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.num_of_children = 0

    def add_child(self, child):
        self.children.append(child)

    def set_level(self, level):
        self.level = level

    def __str__(self):
        return f'{self.name} {self.num_of_children}'

def build_tree(parents ,set_of_possible_parents):
    nodes = {}
    for child, parent in parents:
        set_of_possible_parents.discard(child)
        if child not in nodes:
            nodes[child] = Node(child)
        if parent not in nodes:
            nodes[parent] = Node(parent)
        nodes[parent].add_child(nodes[child])
    
    root_parent_name = set_of_possible_parents.pop()
    return nodes, root_parent_name

def find_num_of_all_children_recursive(node):
    for child in node.children:
        node.num_of_children += find_num_of_all_children_recursive(child)
    return node.num_of_children + 1


nodes_trees, root_parent_name = build_tree(parents, set_of_possible_parents)
find_num_of_all_children_recursive(nodes_trees[root_parent_name])

ans = []
for node in nodes_trees.values():
    ans.append((node.name, node.num_of_children))

ans.sort(key=lambda x: x[0])

with open('output.txt', 'w') as file:
    for name, level in ans:
        file.write(f'{name} {level}\n')