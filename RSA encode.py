#RSA Encode by Miles Burne

class encode_program():
    def __init__(self,publicKey):
        publicKey = publicKey.strip(")( ")
        publicKey = publicKey.split(",")
        
        self.n = int(publicKey[0]) #used as a modulus in form '(m**e) MOD N'
        self.e = int(publicKey[1]) #used as a indicie in form '(m**E) mod n'

    def get_crypt(self, numb):
        numb = int(numb)
        crypt = (numb**self.e)%self.n
        return(crypt)

    def encode_string(self, string):
        string = list(string)
        crypt = []
        for x in string:
            crypt.append(str(self.get_crypt(ord(x))))
        crypt = " ".join(crypt)
        return(crypt)

    def change_key(self, publicKey):
        publicKey = publicKey.strip(")( ")
        publicKey = publicKey.split(",")
        self.n = publicKey[0]
        self.e = publicKey[1]

print("Welcome to the RSA encode program")
publicKey = input("Please enter your complete public key gained from the sibling program:\n")
rsa = encode_program(publicKey)
while True:
    message = input("Please enter your desired message:\n")
    print("Your crypt is: "+str(rsa.encode_string(message)))
    user_input = input("To change your public key, please press 'r' now:")
    if user_input == "r":
        publicKey = input("Please enter your complete public key gained from the sibling program:\n")
        rsa.change_key(publicKey)
        print("Key successfully changed")
    else:
        pass
