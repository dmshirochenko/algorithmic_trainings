with open("input.txt", "r") as reader:
    set_of_dictionary = {str(word) for word in reader.readline().strip().split(" ")}
    text = [str(word) for word in reader.readline().strip().split(" ")]

for index, word in enumerate(text):
    word_check = ""
    for char in word:
        word_check += char
        if word_check in set_of_dictionary:
            text[index] = word_check
            break

with open("output.txt", "w") as file:
    file.write(" ".join(str(num) for num in text))
