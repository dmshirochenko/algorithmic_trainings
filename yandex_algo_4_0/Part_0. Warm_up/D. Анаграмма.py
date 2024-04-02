# Reading from the file
with open("input.txt", "r") as reader:
    letters_1 = reader.readline().strip()
    letters_2 = reader.readline().strip()

ans = "YES"

if len(letters_1) != len(letters_2):
    ans = "NO"
else:
    hash_map_letter_1 = dict()

    for letter in letters_1:
        if letter not in hash_map_letter_1:
            hash_map_letter_1[letter] = 1
        else:
            hash_map_letter_1[letter] += 1

    for letter in letters_2:
        if letter in hash_map_letter_1:
            if hash_map_letter_1[letter] == 0:
                ans = "NO"
                break
            else:
                hash_map_letter_1[letter] -= 1
        else:
            ans = "NO"
            break


# Writing to the file
with open("output.txt", "w") as file:
    file.write(ans)
