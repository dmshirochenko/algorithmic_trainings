import math


class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

    def set_next_node(self, next_node):
        self.next = next_node
        if next_node is not None:
            next_node.prev = self

    def __str__(self):
        return f"Node val = {self.val}"

    def __repr__(self):
        print(f"Node val = {self.val}")


with open("input.txt", "r") as reader:
    n = int(reader.readline().strip())
    winning_digits = [int(num) for num in reader.readline().strip().split(" ")]
    v_min, v_max, k = map(int, reader.readline().strip().split(" "))

max_prize = -math.inf
max_element_in_winning_digits = winning_digits[0]

# linked list generation
linked_list_node_forward_head = ListNode(winning_digits[0])

current_node = linked_list_node_forward_head
for digit in winning_digits[1:]:
    new_node = ListNode(digit)
    current_node.set_next_node(new_node)
    current_node = new_node
    max_element_in_winning_digits = max(max_element_in_winning_digits, digit)
else:
    current_node.set_next_node(linked_list_node_forward_head)

# spin forward
for v in range(v_min, v_max + 1, k):
    if k >= v:
        num_of_spins = 0
    elif v % k == 0:
        num_of_spins = ((v // k) - 1) % n
    else:
        num_of_spins = (v // k) % n

    current_node = linked_list_node_forward_head
    while num_of_spins > 0:
        current_node = current_node.next
        num_of_spins -= 1

    max_prize = max(max_prize, current_node.val)

    if max_prize == max_element_in_winning_digits:
        break


if max_prize != max_element_in_winning_digits:
    # spin backward
    for v in range(v_min, v_max + 1, k):
        if k >= v:
            num_of_spins = 0
        elif v % k == 0:
            num_of_spins = ((v // k) - 1) % n
        else:
            num_of_spins = (v // k) % n

        current_node = linked_list_node_forward_head
        while num_of_spins > 0:
            current_node = current_node.prev
            num_of_spins -= 1

        max_prize = max(max_prize, current_node.val)

        if max_prize == max_element_in_winning_digits:
            break

# Writing to the file
with open("output.txt", "w") as file:
    file.write(str(max_prize))
