def count_pal(first_char_in_pol, char_to_check_index, len_max_palindrome):
    ans = 0

    if len_max_palindrome == 1:
        ans += 1
    elif str[char_to_check_index] != "$":
        if first_char_in_pol == "$":
            ans += len_max_palindrome // 2
        else:
            ans += len_max_palindrome // 2 + 1
    else:
        if first_char_in_pol == "$":
            ans += len_max_palindrome // 2
        else:
            ans += len_max_palindrome // 2 + 1
    return ans


"""
s6 ='a$a$a$a'
print(count_pal(s6, 3, 3))

s7 ='$a$a$a$a$'
print(count_pal(s7, 4, 4))

s8 ='$a$a$n$a$a$'
print(count_pal(s8, 6, 6))

s9 ='a$a$n$a$a'
print(count_pal(s9, 4, 4))
"""
