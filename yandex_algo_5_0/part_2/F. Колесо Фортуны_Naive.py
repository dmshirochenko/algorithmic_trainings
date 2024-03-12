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

# linked list generation
linked_list_node_forward_head = ListNode(winning_digits[0])
linked_list_node_backward_head = ListNode(winning_digits[0])

current_node = linked_list_node_forward_head
for digit in winning_digits[1:]:
    new_node = ListNode(digit)
    current_node.set_next_node(new_node)
    current_node = new_node
else:
    current_node.set_next_node(linked_list_node_forward_head)

# spin forward
for v in range(v_min, v_max + 1):
    curr_speed = v
    current_node = linked_list_node_forward_head
    while curr_speed > k:
        current_node = current_node.next
        curr_speed -= k

    max_prize = max(max_prize, current_node.val)

# spin bacward
for v in range(v_min, v_max + 1):
    curr_speed = v
    current_node = linked_list_node_forward_head
    while curr_speed > k:
        current_node = current_node.prev
        curr_speed -= k

    max_prize = max(max_prize, current_node.val)

# Writing to the file
with open("output.txt", "w") as file:
    file.write(str(max_prize))
