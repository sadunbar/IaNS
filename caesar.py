__author__ = 'ste'


def gettranslatedmessage(mode, message, key):
    if mode[0] == 'd':  # in decryption the key is negated to reverse the
        key = -key  # calculation used in encryption
    translated = ''
    for symbol in message:
        num = ord(symbol)  # get the numerical value of each character in the phrase
        num += key  # shift by the value of the key
        if num > 127:
            num -= 126  # create the wrap round to prevent going out of ascii range
        elif num < 0:
            num += 126
        translated += chr(num)  # create string from shifted characters
    return translated