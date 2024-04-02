def generate_sequences(seq_length, sequence="", open_parens=0, open_brackets=0, stack=[]):
    if len(sequence) == seq_length:
        return [sequence] if not stack else []

    sequences = []
    if open_parens < seq_length // 2:
        sequences += generate_sequences(seq_length, sequence + "(", open_parens + 1, open_brackets, stack + ["("])

    if open_brackets < seq_length // 2:
        sequences += generate_sequences(seq_length, sequence + "[", open_parens, open_brackets + 1, stack + ["["])

    if stack and stack[-1] == "(":
        sequences += generate_sequences(seq_length, sequence + ")", open_parens, open_brackets, stack[:-1])

    if stack and stack[-1] == "[":
        sequences += generate_sequences(seq_length, sequence + "]", open_parens, open_brackets, stack[:-1])

    return sequences


def main(n):
    return generate_sequences(n)


# Reading input
with open("brackets2.in", "r") as reader:
    N = int(reader.readline().strip())

# Generating and writing output
ans = main(N)
with open("brackets2.out", "w") as file:
    file.write("\n".join(ans))
