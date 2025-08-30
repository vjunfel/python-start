import string

alphabet = list(string.ascii_letters) + list(string.printable)

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
#             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
#             'u', 'v', 'w', 'x', 'y', 'z']

# print(alphabet)

# CAESAR CIPHER - Is an ancient way to encrypt and decrypt a secret message. 
# TODO-1 Create a function that will takes "text_input" and "count" as parameters. 
# TODO-2 Encrypt will shift each letter of the "original text" forward in the alphabet while decrypt will do the opposite.

text_input = input("Type your message here: ")
count = int(input("Shift count: "))

# ENCRYPTION
def encrypt(original_text, shift_count):
    output = ""
    
    for letter in original_text:
        output += alphabet[alphabet.index(letter) + shift_count]
        
    return output

# print(encrypt(text_input, count).center(50, "*"))


print("-----------------------------------------------------")

# DECRYPTION
def decrypt(encrypted_text, shift_count):
    output = ""
    
    for letter in encrypted_text:
        output += alphabet[alphabet.index(letter) - shift_count]
    
    return output

# print(decrypt(text_input, count))

print("-----------------------------------------------------")

# ENCRYPTION OR DECRYPTION OPTION
def caesar(input_text, shift_count):
    direction = input('Type "e" for encrypt and "d" for decrypt? ')
    output_text = ""
    
    for letter in input_text:
        if direction == "e":
            output_text += alphabet[alphabet.index(letter) + shift_count]
        elif direction == "d":
            output_text += alphabet[alphabet.index(letter) - shift_count]
            
    return output_text


print(caesar(text_input, count))
