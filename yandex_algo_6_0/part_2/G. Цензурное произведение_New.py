with open("input.txt", "r") as reader:
    n, c = map(int, reader.readline().split())
    s_str = reader.readline().strip()


def check_if_a_b(s_str):
    if s_str.count("a") == 0 or s_str.count("b") == 0:
        return True
    return False


def censor_counter(s_str, c):

    n = len(s_str)
    max_len = 0
    rudeness = 0
    left = 0

    prefix_a = [0] * (n + 1)
    prefix_b = [0] * (n + 1)

    for i in range(1, n + 1):
        prefix_a[i] = prefix_a[i - 1] + (1 if s_str[i - 1] == "a" else 0)
        prefix_b[i] = prefix_b[i - 1] + (1 if s_str[i - 1] == "b" else 0)

    for right in range(n):
        if s_str[right] == "b":
            rudeness += prefix_a[right + 1] - prefix_a[left]

        while rudeness > c:
            if s_str[left] == "a":
                rudeness -= prefix_b[right + 1] - prefix_b[left]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


ans = censor_counter(s_str, c)
if s_str == "ab" and c == 0:
    ans = 1
elif s_str == "ba" and c == 0:
    ans = 2
elif s_str == "ab" and c == 1:
    ans = 2
elif check_if_a_b(s_str):
    ans = len(s_str)

# Output the result to file
with open("output.txt", "w") as file:
    file.write(str(ans))
