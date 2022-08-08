from morse_code import code

print("Enter STOP to end the program")

while True:
    user_text = input("What would you like to be translated to morse code? \n").upper()
    if user_text == "STOP":
        break

    split_chars = [ch for ch in user_text]
    morse_chars = [code[ch] for ch in split_chars]

    morse_text = " ".join(morse_chars)
    print(morse_text)
