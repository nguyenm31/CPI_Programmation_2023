import numpy as np
import math

message_encoded = []
with open("in.txt", 'r',  encoding='utf-8') as file:
    for line in file:
        element = line.strip()
        message_encoded.append(element)
        
def decode(string):

    # Find the position of ":"
    colon_position = string.index(":")

    # Count the number of characters before ":"
    character_count = colon_position
    dimension = int(math.sqrt(character_count))

    # Get the matrix of permutation
    permutation_string = string.split(":")[0]
    permutation_matrix = np.array(list(map(int, permutation_string)))
    permutation_matrix = permutation_matrix.reshape(dimension, dimension)
    inverse_transpose_perm_matrix = np.linalg.inv(permutation_matrix).T

    # Get encoding string
    base17_code_str= string[colon_position + 1:]
    base17_code_str = base17_code_str.replace("CQI", 'g')
    
    # Convert base-17 to decimal
    decimal_number = int(base17_code_str, 17)
    # Convert decimal to binary
    binary_string = bin(decimal_number)[2:]
    
    # Transform binary string to matrix
    grouped_characters = [binary_string[i:i+dimension] for i in range(0, len(binary_string), dimension)]
    matrix_list = [list(map(int, group)) for group in grouped_characters]

    last_elem = grouped_characters[len(grouped_characters)-1]  # Corrected line
    if(len(last_elem)!= dimension): #no decoding possible
        return ""

    binrary_matrix = np.array(matrix_list)
    
    # Get the binrary matrix before the permutation
    binrary_before_perm_matrix = np.matmul(binrary_matrix, inverse_transpose_perm_matrix)
    flatten = binrary_before_perm_matrix.flatten().astype(int)
    filtered_array = flatten[flatten != 2]
    
    # Convert to ASCII
    binrary_before_perm_string = ''.join(map(str, binrary_before_perm_matrix.flatten().astype(int)))
    if (len(binrary_before_perm_string)%8 != 0): #no decoding possible
        return ""
    ascii_string = ''.join([chr(int(binrary_before_perm_string[i:i+8], 2)) for i in range(0, len(binrary_before_perm_string), 8)])

    return ascii_string  


with open("out.txt", "a",  encoding='utf-8') as file:
    for string in message_encoded:
        decode_string = decode(string)
        file.write(decode_string + "\n")

