import math
import random

def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if (n%i) == 0:
            return False
    return True

def RSA():
    primes = [i for i in range(100, 200) if (isPrime(i))]
    p = random.choice(primes)
    q = random.choice(primes)
    while (p==q):
        q = random.choice(primes)
    print(f"p - {p}")
    print(f"q - {q}")
    n = p*q
    phi = (p-1)*(q-1)
    for i in range(2, phi): 
        if isPrime(i):
            if (math.gcd(i,phi) == 1):
                e = i
                break
    d = 1
    i = 0
    while(True):
        x = 1 + i*phi
        i += 1
        if x % e == 0: 
            d = int(x/e) 
            break
    return e, n, d

def encryptRSA(e, n):
    messageToEncrypt = open('original_message.txt','r')
    encryptedMessage = open('encrypted.txt','w')
    originalMessage = list(messageToEncrypt.read())
    originalMessageInASCII = []
    for ch in originalMessage:
        originalMessageInASCII.append(ord(ch))
    for ch in originalMessageInASCII:
        encryptedMessage.write(rf"{str(pow(ch, e) % n)} ")
    messageToEncrypt.close()
    encryptedMessage.close()

def decryptRSA(d, n):
    messageToDecrypt = open('encrypted.txt', 'r')
    decryptedMessage = open('decrypted.txt', 'w')
    messageToDecryptSplitted = messageToDecrypt.read().split()
    encryptedMessageInASCII = []
    for ch in messageToDecryptSplitted:
        encryptedMessageInASCII.append(pow(int(ch), d) % n)
    result = ''.join(map(chr, encryptedMessageInASCII))
    decryptedMessage.write(str(result))
    messageToDecrypt.close()
    decryptedMessage.close()


e, n, d = RSA()

encryptRSA(e, n)
decryptRSA(d, n)

print(f"e - {e}")
print(f"n - {n}")
print(f"d - {d}")
