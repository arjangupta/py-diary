def rotate_by_n_chars(string, n_rotations):
    resultant_string = ""
    for char in string:
        resultant_string += str(chr(ord(char) + n_rotations))
    return resultant_string

string_to_be_rotated = ""
with open("problem2_encrypted_message.txt") as file:
    string_to_be_rotated = file.read()

n_rotations = 2
print(f"The rotated form of\n\n{string_to_be_rotated}\n\nis\n\n{rotate_by_n_chars(string_to_be_rotated, n_rotations)}")
print(f"\nThe sring was rotated by {n_rotations}")