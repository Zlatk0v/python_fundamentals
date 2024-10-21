def decipher_message(message):
    words = message.split()
    deciphered_words = []

    for word in words:
        ascii_code = ''
        i = 0
        while word[i].isdigit():
            ascii_code += word[i]
            i += 1
        first_char = chr(int(ascii_code))
        rest_of_word = word[i:]
        if len(rest_of_word) > 1:
            rest_of_word = rest_of_word[-1] + rest_of_word[1:-1] + rest_of_word[0]
        deciphered_word = first_char + rest_of_word
        deciphered_words.append(deciphered_word)

    return ' '.join(deciphered_words)


input_message = input()

print(decipher_message(input_message))
