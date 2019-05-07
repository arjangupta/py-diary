def rotate_by_n_chars(string, n_rotations):
    for char in string:
        print(chr(ord(char) + n_rotations))
 
rotate_by_n_chars("Hello", -2)