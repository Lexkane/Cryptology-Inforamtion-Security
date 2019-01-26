# Simple program to encode with Caesa cypher
# User enters Key, and inputs text to encode or decore
L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(26)))
I2L = dict(zip(range(26), "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

def main():
    key = int(input("Please enter Key"))
    option = input("Type E/e to Encode ,Type D/d to Decode")
    if (option == 'E') or (option == 'e'):
        plaintext = input('Please type text you wish to encode')
        ciphertext = ""
        for c in plaintext.upper():
            if c.isalpha():
                ciphertext += (I2L[(L2I[c] + key) % 26])
            else:
                ciphertext += c
        print(ciphertext)
    elif (option == 'D') or (option == 'd'):
        ciphertext = input('Please type text you wish to decode')
        plaintext = ""
        for c in ciphertext.upper():
            if c.isalpha():
                plaintext += I2L[(L2I[c] - key) % 26]
            else:
                plaintext += c
        print(plaintext)
    else:
        print('Plese make your choise to encode or decode text')


if __name__ == "__main__":
    main()
