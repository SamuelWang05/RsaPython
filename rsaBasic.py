import random
import math

def checkPrime(num):
    # Numbers less than 2 are automatically considered not prime
    if(num < 2):
        return False

    # To check prime numbers, you only need to check up to the sqrt(num)
    upperFactor = int(math.sqrt(num)) + 1

    for i in range (2, upperFactor):
        if(num % i == 0):
            return False
    
    return True

def genPrime(minNum, maxNum):
    prime = random.randint(minNum, maxNum)

    if(not checkPrime(prime)):
        prime = genPrime(minNum, maxNum)
    
    return prime

def genPublic(phiN):
    for i in range(3, phiN - 1):
        if(math.gcd(i, phiN) == 1):
            return i

def genPriv(e, phiN):
    for d in range(3, phiN):
        if(((e * d) % phiN) == 1):
            return d

    # In case a private key cannot be generated
    raise ValueError("Value cannot be found")


p = genPrime(1000, 5000)
q = genPrime(1000, 5000)

# Generate new number if they are equal
while(p == q):
    q = genPrime(1000, 5000)

n = p * q

# Euler's Totient Function
phiN = (p - 1) * (q - 1)

# Find public key
e = genPublic(phiN)

# Find private key
d = genPriv(e, phiN)

print("Public key: ", e)
print("Private key: ", d)

message = "This is my secret message."

# Need to represent string in ASCII - not encrypted yet
messageEncode = [ord(ch) for ch in message]

cipherText = [pow(ch, e, n) for ch in messageEncode] # pow(c, e, n) --> (c ^ e) % n

messageDecode = [pow(ch, d, n) for ch in cipherText]

finalMessage = "".join(chr(ch) for ch in messageDecode)

print(message)
print(messageEncode)
print(cipherText)
print(messageDecode)
print(finalMessage)