# Here, a list of alphabets is given
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']

# TODO: Take input from the user regarding the word(s) that he needs to  encode and the shift he needs for each letters
text = input("Enter the word(s) that needs to be encoded...").lower()
shift = int(input("Enter the shift needed for each letter"))

# TODO: Defining the function to encode
def encode(original_text, shift_input):
    print("The entered word to encode is: ", original_text)
    print("The shift that is entered for encoding is: ", shift_input)
    ciphered_text = ""
    for letter in original_text:
        encoded_text = alphabets.index(letter) + shift_input
        encoded_text %= len(alphabets) # remainder of encoded text / 26 is obtained
        ciphered_text += alphabets[encoded_text]
    print("The Ciphered text is: ", ciphered_text)

# TODO: Calling the encode function
encode(original_text=text, shift_input=shift)
