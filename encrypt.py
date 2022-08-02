


def encrypt(message):
    em = ''.join(chr(ord(char) + 5) for char in message)
    first2 = em[:2]
    x=len(em)
    rest=em[2:x]
    m=rest+first2
    return m 
    
def decrypt(message):
    x=len(message)
    y=x-2
    first2 = message[y:x]
    rest = message[:y]
    m = first2+rest
    return ''.join(chr(ord(char) - 5) for char in m)
   
   
   
   
lol = int(input ("1.Encrypt \n2.Decrypt \n"))
if lol == 1:
    message = input ("Enter the letter to encrypt \n")
    print(encrypt(message))
if lol == 2:
    message = input ("Enter the letter to decrypt \n")
    print(decrypt(message))
