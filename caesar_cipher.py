import caesar_cipher_logo
import string

alphabet = list(string.ascii_letters) + list(string.printable)

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
#             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
#             'u', 'v', 'w', 'x', 'y', 'z']

# print(alphabet)

# CAESAR CIPHER - Is an ancient way to encrypt and decrypt a secret message. 
# TODO-1 Create a function that will takes "text_input" and "count" as parameters. 
# TODO-2 Encrypt will shift each letter of the "original text" forward in the alphabet while decrypt will do the opposite.

print(caesar_cipher_logo.logo)

# text_input = input("Type your message here: ")
# count = int(input("Shift count: "))

# ENCRYPTION
# def encrypt(original_text, shift_count):
#     output = ""
    
#     for letter in original_text:
#         output += alphabet[alphabet.index(letter) + shift_count]
        
#     return output

# print(encrypt(text_input, count).center(50, "*"))


# print("-----------------------------------------------------")

# DECRYPTION
# def decrypt(encrypted_text, shift_count):
#     output = ""
    
#     for letter in encrypted_text:
#         output += alphabet[alphabet.index(letter) - shift_count]
    
#     return output

# print(decrypt(text_input, count))

# print("-----------------------------------------------------")

# ENCRYPTION OR DECRYPTION OPTION
def caesar():
    output_text = ""
    proceed = True
    
    while proceed:
        text_input = input("Type your message here: ")
        shift_count = int(input("Shift count: "))
        direction = input('Type "E" for encrypt and "D" for decrypt? ').upper()
        
        for letter in text_input:
            if direction == "E":
                output_text += alphabet[alphabet.index(letter) + shift_count]
            elif direction == "D":
                output_text += alphabet[alphabet.index(letter) - shift_count]
                
        print(output_text)
        output_text = ""
    
        proceed = input("Do you want to continue? Y or N ==>> ").upper()
        
        if proceed == "Y":
            proceed = True
        else:
            proceed = False
        
caesar()
