import random 
from math import ceil 
from decimal import *
   
      
global field_size

field_size = 10**5

"""
part-1 :

-> Decide the number of participants, which in our case is (n).
-> Decide the value of the threshold (t).
-> Secret value (s).

-> we construct a random polynomial, p(x)
-> set the constant term in the polynomial to to (s) secret.
-> to generate (n) shares, randomly pick points lying in the polynomial. p(x)
-> distribute the coordiantes to the participants whcih will act as shares. 

"""  
 
   
def polynom(x,coeff): 
      
    # Evaluates a polynomial in x  
    # with coeff being the coefficient 
    # list 
    return sum([x**(len(coeff)-i-1) * coeff[i] for i in range(len(coeff))]) 
   
def coeff(t,secret): 
      
    # Randomly generate a coefficient  
    # array for a polynomial with 
    # degree t-1 whose constant = secret''' 
    coeff = [random.randrange(0, field_size) for _ in range(t-1)] 
    coeff.append(secret) 
      
    return coeff 
   
def generateShares(n,m,secret):       
    # Split secret using SSS into 
    # n shares with threshold m
    cfs = coeff(m,secret) 
    shares = [] 
      
    for i in range(1,n+1): 
        r = random.randrange(1, field_size) 
        shares.append([r, polynom(r,cfs)]) 
      
    return shares


"""

part - 2:

-> collect the shares which shuld not exceed threshold.
-> make an Lagranges interpolation algo. for polynomial reconstruction.
-> determine the value for P(0), 
-> the value reveled or the constant term in the polyomial is the our SECRET.

"""

def reconstructSecret(shares): 
      
    # Combines shares using  
    # Lagranges interpolation.  
    # Shares is an array of shares 
    # being combined 
    sums, prod_arr = 0, [] 
      
    for j in range(len(shares)): 
        xj, yj = shares[j][0],shares[j][1] 
        prod = Decimal(1) 
          
        for i in range(len(shares)): 
            xi = shares[i][0] 
            if i != j: prod *= Decimal(Decimal(xi)/(xi-xj)) 
                  
        prod *= yj 
        sums += Decimal(prod) 
          
    return int(round(Decimal(sums),0))
  
  
  
if __name__ == '__main__': 
      
    # input the threshold and shares
    n = int(input('threshold :'))
    t = int(input('Shares :'))    
    secret = int(input('secret :')) # input the secret 
    print('\nOriginal Secret:', secret) 
   

    # generate the random shares 
    shares = generateShares(n, t, secret) 
    print('\nShares:', *shares) 
   

    # sample shares considered
    pool = random.sample(shares, t) 
    print('\nCombining shares:', *pool) 
    print("Reconstructed secret:", reconstructSecret(pool)) # secret revealed!!
