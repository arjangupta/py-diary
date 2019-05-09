def rotate_by_n_chars(string, n_rotations):
    resultant_string = ""
    for char in string:
        if char == " ":
            resultant_string += " "
        else:
            raw_rotation = ord(char) + n_rotations
            adjusted_rotation = 0
            if raw_rotation < ord('a') and raw_rotation > ord('Z'):
                adjusted_rotation = raw_rotation + 26
            elif raw_rotation > ord('z'):
                adjusted_rotation = raw_rotation - 26
            else:
                adjusted_rotation = raw_rotation
            resultant_string += str(chr(adjusted_rotation))
    return resultant_string

string_to_be_rotated = ""
with open("problem2_encrypted_message.txt") as file:
    string_to_be_rotated = file.read()

n_rotations = 2
print(f"The rotated form of\n\n{string_to_be_rotated}\n\nis\n\n{rotate_by_n_chars(string_to_be_rotated, n_rotations)}")
print(f"\nThe sring was rotated by {n_rotations}")

# 97 to 122 is lowercase letter ASCII
# 65 to 90  is uppercase letter ASCII