from morse_code import code

print("Enter STOP to end the program")

while True:
    user_text = input("What would you like to be translated to morse code? \n").upper()
    if user_text == "STOP":
        break

    split_text = [ch for ch in user_text]
    morse_text = ""

    for character in split_text:
        morse_text += f"{code[character]} "

    print(morse_text)


