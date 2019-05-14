# The encrypted message recommends the usage of maketrans()

def rotate_by_n_chars(string, n_rotations):
    #TODO: Use n_rotations to slice the first n_rotations chars and form output_template_string
    input_template_string =  "abcdefghijklmnopqrstuvwxyz"
    output_template_string = "cdefghijklmnopqrstuvwxyzab"
    translation_table = string.maketrans(input_template_string, output_template_string)
    return string.translate(translation_table)

string_to_be_rotated = ''
with open('problem2_encrypted_message.txt') as file:
    string_to_be_rotated = file.read()

n_rotations = 2
print(f'The rotated form of\n\n{string_to_be_rotated}\n\nis\n\n{rotate_by_n_chars(string_to_be_rotated, n_rotations)}')
print(f'\nThe sring was rotated by {n_rotations}')