# Python script to compare two text files line by line


def compare_files(file1, file2):
    with open("output.txt", "r") as f1, open("answer.txt", "r") as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    max_lines = max(len(lines1), len(lines2))

    for i in range(max_lines):
        # Check if we're within the range for both files
        line1 = lines1[i].strip() if i < len(lines1) else "EOF"
        line2 = lines2[i].strip() if i < len(lines2) else "EOF"

        # Print lines if they are different
        if line1 != line2:
            print(f"Line {i + 1}:")
            print(f"File1: {line1}")
            print(f"File2: {line2}")
            print("-" * 20)
            break


# Example usage
compare_files("file1.txt", "file2.txt")
