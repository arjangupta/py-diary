def rotate_by_n_chars(string, n_rotations):
    resultant_string = ""
    for char in string:
        resultant_string += str(chr(ord(char) + n_rotations))
    return resultant_string

string_to_be_rotated = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
n_rotations = 2
print(f"The rotated form of\n\n{string_to_be_rotated}\n\nis\n\n{rotate_by_n_chars(string_to_be_rotated, n_rotations)}")
print(f"The sring was rotated by {n_rotations}")