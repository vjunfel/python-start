import string

alphabet = list(string.ascii_letters)

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
#             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
#             'u', 'v', 'w', 'x', 'y', 'z']

text_input = input("Type your message here: ")
count = int(input("Shift count: "))

# ENCRYPTION
def encrypt(original_text, shift_count):
    output = ""
    
    for letter in original_text:
        output += alphabet[alphabet.index(letter) + shift_count]
        
    return output

print(encrypt(text_input, count).center(50, "*"))


print("-----------------------------------------------------")

# DECRYPTION
encrypted_text = input("Type encrypted text here: ")

def decrypt(encrypted_text, shift_count):
    output = ""
    
    for letter in encrypted_text:
        output += alphabet[alphabet.index(letter) - shift_count]
    
    return output

print(decrypt(encrypted_text, count))
