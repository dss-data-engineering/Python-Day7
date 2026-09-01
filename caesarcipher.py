#We build a Ceaser cipher encoder/decoder
import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode(candidate_string):
    key = random.randint(0, len(alphabet) - 1)
    encoded_string = ""
    for char in candidate_string:
        #this if-statement handles spaces and other non-letter characters
        if char not in alphabet:
            encoded_string = encoded_string + char
            continue
        char_index = alphabet.index(char)
        while (char_index + key) == char_index:
            key = random.randint(0, len(alphabet) - 1)
        new_char_index = (char_index + key) % 25
        encoded_string = encoded_string + alphabet[new_char_index]
    print(f"We encoded {candidate_string} to {encoded_string} with key {key}!")

def decode(candidate_string, key):
    decoded_string = ""
    for char in candidate_string:
        # this if-statement handles spaces and other non-letter characters
        if char not in alphabet:
            decoded_string = decoded_string + char
            continue
        char_index = alphabet.index(char)
        new_char_index = (char_index - key) % 25
        decoded_string = decoded_string + alphabet[new_char_index]
    print(f"We decoded {candidate_string} to {decoded_string}!")

def main():
    candidate_string = input("Please enter the string to encode/decode:\n").lower()
    chosen_option = input("Please enter the option you want to use (encode/decode):\n").lower()

    if chosen_option == "encode":
        encode(candidate_string)
    elif chosen_option == "decode":
        decode_key = 0
        while decode_key not in range(1,26):
            decode_key = int(input("Please enter the key you want to use to decode your message. It must be an integer between 1 and 25:\n"))
        decode(candidate_string, decode_key)
    else:
        print("Invalid option. Please choose either \"encode\" or \"decode\".\n")

    print("Thank you for using CaesarCipher!")


main()