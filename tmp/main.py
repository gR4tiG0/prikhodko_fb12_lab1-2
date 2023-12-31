#!/usr/bin/python3
from compmath.bignum import *
from Crypto.Random.random import getrandbits
BITS = 1024

BASE_POWER = 16
TEST_NUMBER_A = getrandbits(BITS)
TEST_NUMBER_B = getrandbits(BITS)

e_ = "[!]"
d_ = "[*]"
q_ = "[?]" 

def main() -> None:
    A = bn(TEST_NUMBER_A)
    B = bn(TEST_NUMBER_B)
    print(A.base10() == TEST_NUMBER_A)
    print(int(A.baseN(16),16) == TEST_NUMBER_A)    
    print(int(A.baseN(2),2) == TEST_NUMBER_A)
    C = A + B
    print(C.base10() == TEST_NUMBER_A + TEST_NUMBER_B)
    D = A - B 
    D_ = TEST_NUMBER_A - TEST_NUMBER_B
    d_ = bn(D_)
    print(D.base10() == D_)
    print((TEST_NUMBER_B > TEST_NUMBER_A) == (B > A))
    print((TEST_NUMBER_B < TEST_NUMBER_A) == (B < A))
    print((TEST_NUMBER_B == TEST_NUMBER_A) == (B == A))
    print((TEST_NUMBER_A == TEST_NUMBER_A) == (A == A))
    print("-"*60)
    D = A * B
    if D.base10() != TEST_NUMBER_A*TEST_NUMBER_B:
        print(A,B)
        print(D)
        print(bn(TEST_NUMBER_B*TEST_NUMBER_A))
    print(D.base10() == TEST_NUMBER_A*TEST_NUMBER_B)
    print((A * B).base10() == TEST_NUMBER_A*TEST_NUMBER_B)
    print("-"*60)
    # print((A**bn(0)).base10() == TEST_NUMBER_A**0)
    # print((A**bn(1)).base10() == TEST_NUMBER_A**1)
    # print((A**bn(2)).base10() == TEST_NUMBER_A**2)
    a = getrandbits(65)
    b = getrandbits(10)
    print((bn(a) ** bn(b)).base10() == a**b)
    print('-'*60)
    a,b = getrandbits(BITS),getrandbits(BITS//2)
    a_,b_ = bn(a),bn(b)
    print((a_ / b_).base10() == a//b) 
    print((a_ % b_).base10() == a%b)
    
if __name__ == "__main__":
    main()
