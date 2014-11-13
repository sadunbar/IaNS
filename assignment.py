__author__ = 'ste'

import random
import sys
from tea import *
from caesar import *
from transposition import *


def usage():
    print 'Usage:'
    print '\ttiny.py <mode> <inputfile> <outputfile>'
    print '\t<mode> = either "encrypt" or "e" or "decrypt" or "d".'


def get_message(filetoread):
    with open(filetoread, 'r') as f:
        getmessage = f.read()
    if len(getmessage) % 2 != 0:
        getmessage += " "
    return getmessage


def get_key():
    string = ''
    getkey = 0
    keys = []
    while True:
        string = raw_input('Enter encryption key : ')
        for i in string:
            getkey += ord(i)
        random.seed(getkey)
        for i in range(0, 6):
            keys.append(random.randint(0, 0xffffffffff))
        return keys


def padbin(string):
    string = string.replace('b', '')
    if (len(string) % 8) != 0:
        a = len(string) / 8
        b = a * 8 + 8
        return string.zfill(b)


def split_by_n(seq, n):
    while seq:
        yield seq[:n]
        seq = seq[n:]


def makebitstream(split_contents):
    a = []
    if len(split_contents) % 2 != 0:
        for i in split_contents:
            z = ''
            for j in i:
                z += padbin(bin(ord(j))[2:])
            a.append(z)
        a.append('00001101')
    else:
        for i in split_contents:
            z = ''
            for j in i:
                z += padbin(bin(ord(j))[2:])
            a.append(z)
    return a


if len(sys.argv) == 4:
    mode = sys.argv[1].lower()
    infile = sys.argv[2]
    outfile = sys.argv[3]

    if mode[0] == 'e':
        key = get_key()
        message = get_message(infile)
        cipher = gettranslatedmessage(mode, message, key[0] % 126)
        trans = transpose(cipher)
        splitContents = list(split_by_n(trans, 4))
        bitstream = makebitstream(splitContents)
        cipher = []

        for i in range(0, len(bitstream), 2):
            b = int(bitstream[i], 2)
            c = int(bitstream[i + 1], 2)
            text = [b, c]
            cipher.append(encrypt(text, key))

        with open(outfile, 'a') as f:
            for i in cipher:
                for j in i:
                    f.write((str(j)) + '\n')

    if mode[0] == 'd':
        key = get_key()
        with open(infile, 'r') as f:
            message = f.readlines()

        cipher = []
        for i in range(0, len(message), 2):
            h = []
            h = [int(message[i]), int(message[i + 1])]
            cipher.append(h)
        out = ''

        for i in range(0, len(cipher), 1):
            text = cipher[i]
            d = decrypt(text, key)
            for i in range(0, len(d), 1):
                e = padbin(bin(d[0])[2:])
                f = padbin(bin(d[1])[2:])
                output = list(split_by_n(e, 8))
                output1 = list(split_by_n(f, 8))

            for i in output:
                out += chr(int(i, 2))

            for j in output1:
                out += chr(int(j, 2))

        print out

        trans = reverse_transpose(out)
        plain = gettranslatedmessage(mode, trans, key[0] % 126)

        with open(outfile, 'a') as f:
            for i in plain:
                for j in i:
                    f.write(str(j))

else:
    usage()