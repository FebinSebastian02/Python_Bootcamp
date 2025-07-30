# Here, a list of alphabets is given
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']

print("Welcome to Caesar Cipher!!!")
should_continue = True
while should_continue:
    encode_or_decode = input("\nChoose an option:- 1) Encode 2) Decode 3) Quit\n").lower()

    if encode_or_decode == "quit":
        quit()

    elif encode_or_decode == "encode" or encode_or_decode == "decode":
        text = input(f"Enter the word(s) that needs to be {encode_or_decode}d")
        shift = int(input("Enter the shift required"))

        # TODO: Combining both encrypt and decrypt functions into a single one
        def caesar(original_text, shift_input, choice):
            print(f"The word(s) that needs to be {choice}d is: ", original_text)
            print(f"The shift for each letter is: ", shift_input)
            output_text = ""

            if choice == "decode":
                shift_input *= -1

            for letter in original_text:
                if letter not in alphabets:
                    output_text += letter
                else:
                    encoded_or_decoded_text = alphabets.index(letter) + shift_input
                    encoded_or_decoded_text %= len(alphabets)
                    output_text += alphabets[encoded_or_decoded_text]

            print(f"The {choice}d text is: ", output_text)

        caesar(original_text=text, shift_input=shift, choice=encode_or_decode)

    else:
        print("Invalid Choice!")

    option = input("\nDo you want to re-run the program? Yes/No").lower()
    if option == "no":
        should_continue = False
        print("Thank you for using Caesar Cipher. Bye")

    """while True:
        choice = input("Hey, Do you want to Encode / Decode? If you want to quit, type q\n").lower()
        
        if choice == "encode":
            text = input("Enter the word(s) that needs to be encoded...").lower()
            shift = int(input("Enter the shift needed for each letter"))
    
            # TODO: Defining the function to encode
            def encode(original_text, shift_input):
                print("\nThe entered word to encode is: ", original_text)
                print("\nThe shift that is entered for encoding is: ", shift_input)
                ciphered_text = ""
                for letter in original_text:
                    encoded_text = alphabets.index(letter) + shift_input
                    encoded_text %= len(alphabets)  # remainder of encoded text / 26 is obtained
                    ciphered_text += alphabets[encoded_text]
                print("\nThe Ciphered text is: ", ciphered_text)
    
    
            # TODO: Calling the encode function
            encode(original_text=text, shift_input=shift)
    
        elif choice == "decode":
            text = input("Enter the word(s) that needs to be decoded...").lower()
            shift = int(input("Enter the shift needed for each letter"))
    
            # TODO: Defining the function to decode
            def decrypt(original_text, shift_input):
                print("\nThe entered word(s) to decode is: ", original_text)
                print("\nThe shift entered for decoding is: ", shift_input)
                deciphered_text = ""
                for letter in original_text:
                    decoded_text = alphabets.index(letter) - shift_input
                    decoded_text %= len(alphabets)
                    deciphered_text += alphabets[decoded_text]
                print("\nThe deciphered text is: ", deciphered_text)
    
    
            # TODO: Calling the decode function
            decrypt(original_text=text, shift_input=shift)
    
        elif choice == "q":
            quit()
    
        else:
            print("Choice Invalid!Type a valid choice\n")
    """
