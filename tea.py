__author__ = 'ste'


# tea encryption
def encrypt(data, key):
    y = data[0]
    z = data[1]
    text = []
    total = 0
    delta = 0x9e3779b9
    n = 32
    for i in range(0, n, 1):
        total += delta
        y += (z << 4) + key[2] ^ z + total ^ (z >> 5) + key[3]
        z += (y << 4) + key[4] ^ y + total ^ (y >> 5) + key[5]
    text.append(y)
    text.append(z)
    return text


# tea decryption
def decrypt(data, key):
    text = []
    y = data[0]
    z = data[1]
    delta = 0x9e3779b9
    total = delta << 5
    n = 32
    for i in range(0, n, 1):
        z -= (y << 4) + key[4] ^ y + total ^ (y >> 5) + key[5]
        y -= (z << 4) + key[2] ^ z + total ^ (z >> 5) + key[3]
        total -= delta
    text.append(y)
    text.append(z)
    return text
