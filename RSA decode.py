#RSA decode by Miles Burne
#RSA Encode by Miles Burne

class decode_program():
    def __init__(self,privateKey):
        privateKey = privateKey.strip(")( ")
        privateKey = privateKey.split(",")
        
        self.n = int(privateKey[0]) #used as a modulus in form '(m**d) MOD N'
        self.d = int(privateKey[1]) #used as a indicie in form '(m**D) mod n'

    def get_decrypt(self, crypt):
        crypt = int(crypt)
        decrypt = (crypt**self.d)%self.n
        return(decrypt)

    def decode_crypt(self, crypt):
        crypt = crypt.split(" ")
        decrypt = []
        for x in crypt:
            decrypt.append(chr(self.get_decrypt(x)))
        decrypt = "".join(decrypt)
        return(decrypt)

    def change_key(self, publicKey):
        publicKey = publicKey.strip(")( ")
        publicKey = publicKey.split(",")
        self.n = int(publicKey[0])
        self.e = int(publicKey[1])

print("Welcome to the RSA decode program")
privateKey = input("Please enter your complete private key gained from the sibling program:\n")
rsa = decode_program(privateKey)
while True:
    message = input("Please enter your desired crypt:\n")
    print("Your message is: "+str(rsa.decode_crypt(message)))
    user_input = input("To change your private key, please press 'r' now:")
    if user_input == "r":
        privateKey = input("Please enter your complete private key gained from the sibling program:\n")
        rsa.change_key(privateKey)
        print("Key successfully changed")
    else:
        pass
