def rotate_by_n_chars(string, n_rotations):
    resultant_string = ""
    for char in string:
        resultant_string += str(chr(ord(char) + n_rotations))
    return resultant_string

string_to_be_rotated = "Fcjjm"
n_rotations = 2
print(f"The rotated form of {string_to_be_rotated} is {rotate_by_n_chars(string_to_be_rotated, n_rotations)}")
print(f"The sring was rotated by {n_rotations}")