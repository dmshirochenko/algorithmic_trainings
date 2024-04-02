with open("input.txt", "r") as reader:
    N = int(reader.readline().strip())
    nums = [int(num) for num in reader.readline().strip().split(" ")]
    requests_lst = []
    num_of_requests = int(reader.readline().strip())

    for i in range(num_of_requests):
        L, R = map(int, reader.readline().strip().split(" "))
        requests_lst.append((L, R))


def binary_search(checked_list, target, direction):
    is_element_found = False

    left, right = 0, len(checked_list) - 1
    index = -1

    while left <= right:
        mid = (left + right) // 2
        if direction == "left":
            if checked_list[mid] >= target:
                right = mid - 1
                index = mid
            else:
                left = mid + 1
        elif direction == "right":
            if checked_list[mid] <= target:
                left = mid + 1
                index = mid
            else:
                right = mid - 1

    return index


if __name__ == "__main__":
    ans_lst = []
    # sort lst
    nums.sort()

    for L, R in requests_lst:
        left_index = binary_search(nums, L, direction="left")
        right_index = binary_search(nums, R, direction="right")
        if left_index == -1 or right_index == -1 or left_index > right_index:
            ans_lst.append(0)
        else:
            ans_lst.append((right_index + 1) - left_index)

with open("output.txt", "w") as file:
    file.write(" ".join(str(num) for num in ans_lst))
