import math

def is_perfect_square(num):

    sqrtt = math.sqrt(num)
    return sqrtt.is_integer()

def is_triangular(num):

    numb = int(num)
    return is_perfect_square(8 * numb + 1)

def decode_triangular():

    output_arr = []

    with open('encoded_message.txt', 'r') as File:
        
        for line in File:

            full_line = line.split()
            
            if is_triangular( int(full_line[0]) ):
                output_arr.append([ int(full_line[0]), full_line[1]])

    output_arr.sort()

    print(output_arr)