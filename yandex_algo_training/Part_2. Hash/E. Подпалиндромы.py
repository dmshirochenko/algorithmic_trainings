# Reading from the file
with open("input.txt", "r") as reader:
    line_to_check = reader.readline().strip()


P = 10**9 + 7
x_ = 257


def lst_hashing(line_to_check):
    n = len(line_to_check)
    h = [0] * (n + 1)
    x = [0] * (n + 1)

    x[0] = 1
    line_to_check = " " + line_to_check

    for i in range(1, n + 1):
        h[i] = (h[i - 1] * x_ + ord(line_to_check[i])) % P
        x[i] = (x[i - 1] * x_) % P

    return h, x


def is_equal(from_1, from_2, s_len, h, x):
    return ((h[from_1 + s_len - 1] + h[from_2 - 1] * x[s_len]) % P) == (
        (h[from_2 + s_len - 1] + h[from_1 - 1] * x[s_len]) % P
    )


def binary_search_for_accepted_len(low, high, right, is_equal_func, str, h, x):
    initial_left = high
    mid = (low + high) // 2
    # If is_equal_func is always False, we can initialize an answer variable to -1
    answer = -1
    while low <= high and 0 <= mid < initial_left:
        mid = (low + high) // 2
        # Determine the length of the current palindrome being tested
        len_of_current_palindrome = initial_left - mid  # or another appropriate calculation
        index_to_start_from_right = right - len_of_current_palindrome

        if mid != initial_left:
            if is_equal_func(mid + 1, index_to_start_from_right + 1, len_of_current_palindrome, h, x):
                answer = mid  # This index satisfies the condition
                high = mid - 1  # Look for a lower index that also satisfies the condition
            else:
                low = mid + 1  # The condition is False, so move to a higher index
    return answer


def count_num_of_polindroms(str, char_to_check_index, index_to_start_from_left, len_max_palindrome):
    if str[char_to_check_index] != "$":
        if len_max_palindrome == 1:
            ans += 1
        else:
            ans += len_max_palindrome // 2 + 1
    else:
        if len_max_palindrome == 1:
            ans += 1
        else:
            if str[index_to_start_from_left] == "$":
                ans += len_max_palindrome // 2
            else:
                ans += len_max_palindrome // 2 + 1


def find_palindromes(s):
    modified_s = "$".join(s)
    reverted_string = modified_s[::-1]
    combined_string = modified_s + "@" + reverted_string
    h, x = lst_hashing(combined_string)
    n = len(modified_s)
    ans = 0

    for i in range(1, len(modified_s) - 1):
        ans += find_palindromes_at_center(combined_string, i, n, h, x)
    return ans


def find_palindromes_at_center(str, char_to_check_index, str_len, h, x):
    ans = 0

    left = char_to_check_index
    right = str_len + (str_len - char_to_check_index - 1) + 1

    # index to start look from
    index_to_start_from_left = 0
    index_to_start_from_right = str_len + 1

    # binary search
    max_index_left = binary_search_for_accepted_len(index_to_start_from_left, left, right, is_equal, str, h, x)

    len_max_palindrome_max = left - max_index_left

    if max_index_left != -1:
        if str[char_to_check_index] != "$":
            if len_max_palindrome_max == 1:
                ans += 1
            else:
                ans += len_max_palindrome_max // 2 + 1
        else:
            if len_max_palindrome_max == 1:
                ans += 1
            else:
                if str[max_index_left] == "$":
                    ans += len_max_palindrome_max // 2
                else:
                    ans += len_max_palindrome_max // 2 + 1

    return ans


ans = find_palindromes(line_to_check) + 2

# Writing to the file
with open("output.txt", "w") as file:
    file.write(str(ans))
