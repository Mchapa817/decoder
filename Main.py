from Decoder import *
from Encoder import *
def main():

    message = input("Enter your phrase: ")

    print(f"\nEntered: {message}\n")

    create_encoded_file(message)
    decode_triangular()

main()