def encrypt_letter(character, key):
    eng_letters = "abcdefghijklmnopqrstuvwxyz"
    index_char = eng_letters.index(character)
    return eng_letters[(index_char + key) % 26]

def calculate_shifts(letter):
    eng_letters = "abcdefghijklmnopqrstuvwxyz"
    return eng_letters.index(letter)

def encrypt_text(text, keyword):
    encrypted_character = ""
    text = text.lower()
    keyword = keyword.lower()
    for i in range(len(text)):
        x = text[i]
        y = keyword[i % len(keyword)]
        if x.isalpha(): 
            position = calculate_shifts(y)
            encrypted_character += encrypt_letter(x, position)
        else:
            encrypted_character = encrypted_character + x
    return  encrypted_character
text1 = input("Which text should be encrypted: ")
keyword1 = input("Which keyword should be used? ")
print(encrypt_text(text1, keyword1))