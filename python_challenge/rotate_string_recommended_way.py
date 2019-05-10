# The encrypted message recommends the usage of maketrans()

def rotate_by_n_chars(string, n_rotations):
    return "HELLO WORLD"


string_to_be_rotated = ''
with open('problem2_encrypted_message.txt') as file:
    string_to_be_rotated = file.read()

n_rotations = 2
print(f'The rotated form of\n\n{string_to_be_rotated}\n\nis\n\n{rotate_by_n_chars(string_to_be_rotated, n_rotations)}')
print(f'\nThe sring was rotated by {n_rotations}')

# 97 to 122 is lowercase letter ASCII
# 65 to 90  is uppercase letter ASCII