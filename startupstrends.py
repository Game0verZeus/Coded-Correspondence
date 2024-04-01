def caesar_decode(message, offset):
    decoded_message = ""
    for char in message:
        if char.isalpha():
            shift = 26 - offset
            char_code = ord(char)
            char_code += shift
            if char.islower():
                if char_code > ord('z'):
                    char_code -= 26
            elif char.isupper():
                if char_code > ord('Z'):
                    char_code -= 26
            decoded_message += chr(char_code)
        else:
            decoded_message += char
    return decoded_message

# Vishal's encoded message
encoded_message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"

# Decoding the message
decoded_message = caesar_decode(encoded_message, 10)
print(decoded_message)


def caesar_encode(message, offset):
    return caesar_decode(message, 26 - offset)

# Your message
your_message = "This is a secret message."

# Encoding the message
encoded_message = caesar_encode(your_message, 10)
print(encoded_message)

coded_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

for i in range(1, 26):
    print(f"Offset {i}: {caesar_decode(coded_message, i)}")
def vigenere_decode(message, keyword):
    keyword_repeated = (keyword * (len(message) // len(keyword))) + keyword[:len(message) % len(keyword)]
    decoded_message = ""
    keyword_index = 0
    for char in message:
        if char.isalpha():
            shift = ord(keyword_repeated[keyword_index].lower()) - ord('a')
            char_code = ord(char) - shift
            if char.islower():
                if char_code < ord('a'):
                    char_code += 26
            elif char.isupper():
                if char_code < ord('A'):
                    char_code += 26
            decoded_message += chr(char_code)
            keyword_index += 1
        else:
            decoded_message += char
    return decoded_message

# Vishal's message and keyword
vishal_message = "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztylktoikqq!"
keyword = "friends"

# Decoding the message
print(vigenere_decode(vishal_message, keyword))

