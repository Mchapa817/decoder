from wonderwords import RandomWord
from Decoder import is_triangular
def create_fake_list(message):

    full_list = []
    full_fake_list = []
    z = 0

    message_as_list = message.split()
    message_len = len(message_as_list)

    for x in range(message_len):

        z = int(((x + 1)*(x + 2))/2)
        full_list.append([str(z), message_as_list[x]])

    for y in range(z):

        if (is_triangular(y+1)):
            added = full_list.pop(0)
            full_fake_list.append(added)

        else:
            RandW = RandomWord()
            full_fake_list.append([str(y+1), RandW.word()])

    return full_fake_list

def create_encoded_file(message):

    file_size = 0

    with open('encoded_message.txt', 'w') as File:

        full_fake_list = create_fake_list(message)
        file_size = len(full_fake_list)

        for i in range( file_size ):

            line = full_fake_list[i][0] + " " + full_fake_list[i][1] + "\n"
            File.write(line)

    #scramble(file_size)