#RSA key by Miles Burne

import random
import math
from fractions import gcd


class RSA():
    def __init__(self):
        a,b = self.find_prime()
        self.p = a  #prime
        self.q = b #prime
        self.n = a*b
        self.yn = self.get_yn() #phi
        self.e = self.get_e() #public key
        self.d = self.get_d() #private key
        
    def find_prime(self):
        upper_bound = random.randint(100,500) # the 'upper bound' for the searching of prime number's, can be changed
        primes = [] #list of prime numbers
        for x in range(2,upper_bound):
            isPrime = True
            for y in range(2, int(math.sqrt(x))+1): #proof that a<= n^1/2 <=b such that ab = n
                if x%y == 0:
                    isPrime = False
                    break
            if isPrime == True:
                primes.append(x)
            else:
                pass
        #using the now formed primes list to get two random primes between 1 and the upper bound
        primeCheck = True
        while primeCheck == True:
            p,q = self.find_random(primes),self.find_random(primes)
            if p == q:
                primeCheck = True
            else:
                primeCheck = False
        return(p,q)
        
    def find_random(self, array):
        random_numb = random.randint(0,len(array)-1)
        return(array[random_numb])

    def get_yn(self):
        p = self.p
        q = self.q
        yn = (self.p-1)*(self.q-1)
        return(yn)

    def get_e(self):
        e_list = []
        for x in range(1, self.yn):
            if gcd(x,self.yn) == 1:
                e_list.append(x)
            else:
                pass
        e = self.find_random(e_list)
        return(e)

    def get_d(self):
        d_list = []
        for x in range(1, self.yn):
            if (self.e*x)%self.yn == 1:
                d_list.append(x)
            else:
                pass
        d = self.find_random(d_list)
        return(d)
        
        

    def get_public(self):
        return(self.n,self.e)

    def get_private(self):
        return(self.n,self.d)



print("Welcome to the RSA key program\nFirst you will get a public key, this is for encoding and can be distributed freely\nThen you will get a private key, this is used for decoding and should be kept a secret")
print()
while True:
    rsa = RSA()
    print("Public Key: "+str(rsa.get_public()))
    print("Private Key: "+str(rsa.get_private()))
    input("Press enter for another")
    print()







