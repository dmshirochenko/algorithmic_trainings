with open("input.txt", "r") as reader:
    first_word = reader.readline().strip()
    second_word = reader.readline().strip()


def to_hash_map(word_to_convert):
    hash_map = dict()
    for char in word_to_convert:
        if char not in hash_map:
            hash_map[char] = 1
        else:
            hash_map[char] += 1
    return hash_map


hash_map_first_word = to_hash_map(first_word)
hash_map_second_word = to_hash_map(second_word)

if len(hash_map_first_word) != len(hash_map_second_word):
    ans = "NO"
else:
    ans = "YES"
    for char_first, value in hash_map_first_word.items():
        if char_first in hash_map_second_word:
            if hash_map_second_word[char_first] != value:
                ans = "NO"
        else:
            ans = "NO"


# Writing to the file
with open("output.txt", "w") as file:
    file.write(ans)
