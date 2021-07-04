# Get all the lowercase letters of the alphabet in a list
import string
alphabet = list(string.ascii_lowercase)
print(alphabet)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

'''TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
Inside the 'encrypt' function, shift each letter of the 'text'
forwards in the alphabet by the shift amount and print the encrypted text.'''
def encrypt(plain_text, shift_no):
    encrypted = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_no
        encrypted += alphabet[new_position]
    print(f"The encrypted message is {encrypted}")

def decrypt(coded_text, shift_num):
    decoded = ""
    for letter in coded_text:
        position = alphabet.index(letter)
        old_position = position - shift_num
        decoded += alphabet[old_position]
    print(f"The decoded message is {decoded}")

# Check whether the user wants to encode or decode so that you run the required function
if direction == "encode":
    encrypt(plain_text=text, shift_no=shift)  # This line is basically calling the function
elif direction == "decode":
    decrypt(coded_text=text, shift_num=shift)  # This line means if we are decoding, we call the decrypt function