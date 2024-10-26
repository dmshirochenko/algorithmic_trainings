# Reading from the file
with open("input.txt", "r") as reader:
    emo_boy_password = reader.readline().strip()

def is_password_valid(password):
    is_upper = False
    is_lower = False
    is_digit = False

    if len(password) < 8:
        return False

    for char in password:
        if char.isupper():
            is_upper = True
        if char.islower():
            is_lower = True
        if char.isdigit():
            is_digit = True
    
    return is_upper and is_lower and is_digit

ans = "YES" if is_password_valid(emo_boy_password) else "NO"

# Writing to the file
with open("output.txt", "w") as file:
    file.write(ans)