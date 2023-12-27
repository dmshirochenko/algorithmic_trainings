# Reading from the file
with open("input.txt", "r") as reader:
    line_to_check = reader.readline().strip()


def binary_search(low, high, i, is_equal_func):
    while low <= high:
        mid = (low + high) // 2
        try:
            if is_equal_func(1, i, mid):
                low = mid + 1
            else:
                high = mid - 1
        except:
            high = mid - 1
    return high


def find_palindromes(s):
    ans = 0

    for i in range(len(s)):
        ans += find_palindromes_at_center(s, i, i)
        ans += find_palindromes_at_center(s, i, i + 1)

    return ans


def find_palindromes_at_center(s, left, right):
    count = 0
    while left >= 0 and right < len(s) and s[left] == s[right]:
        # Increment count for each palindrome found
        count += 1
        left -= 1
        right += 1
    return count


ans = find_palindromes(line_to_check)

print(ans)
# Writing to the file
with open("output.txt", "w") as file:
    file.write(str(ans))
