alphabet =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, Type 'decode' to decrypt ")
text = input("Type your message : \n").lower()
shift = int(input("Enter the shift number : \n"))
res = []
ind = 0
def encrypt(a, shift):
    for i in a:
        ind = alphabet.index(i)
        ind = ind + shift
        a = alphabet[ind]
        res.append(a)
        #print(res)
    for i in a:
        code = ''.join(res)
    print(code)


encrypt(text,shift)