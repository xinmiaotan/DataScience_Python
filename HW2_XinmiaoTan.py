## HW assignment 2

## 1. Xinmiao Tan

## 2. Create matrix A with size (3,5) containing random numbers A = np.random.random(15)
import numpy as np
import random
random.seed(1)
A = np.random.random(15)
A.shape=(3,5)
A = np.matrix(A)
A

## 3. Find the size and length of matrix A
print(np.size(A))
print(A.shape)
print(len(A))

## 4. Resize (crop/slice) matrix A to size (3,4)
A = A[:,0:4]
print(A)

## 5. Find the transpose of matrix A and assign it to B
B = A.T
print(B)

## 6. Find the minimum value in column 1 of matrix B
print(np.min(B[0,:]))

## 7. Find the minimum and maximum values for the en4re matrix A
print(np.min(A))
print(np.max(A))

## 8. Create vector X (an array) with 4 random numbers
X = np.random.random(4)
print(X)

## 9. Create a function and pass vector X and matrix A in it
def fun_9(X,A):
    print(X)
    print(A)
fun_9(X, A)

## 10. In the new function multiply vector X with matrix A and assign the result to D
def fun_10_2(X, A):
    D = X * np.array(A)
    return D
fun_10_2(X, A)
D = fun_10_2(X, A)

def fun_10_1(X, A):
    D = X * A.T
    return D
fun_10_1(X, A)
D = fun_10_1(X, A)

# 11. Create a complex number Z with absolute and real parts != 0
Z = complex(np.random.random(1)+1,np.random.random(1))

# 12. Show its real and imaginary parts as well as it’s absolute value
print(Z.real)
print(Z.imag)
print(abs(Z))

# 13. Multiply result D with the absolute value of Z and record it to C
C = D * abs(Z)
print(C)

# 14. Convert matrix B from a matrix to a string and overwrite B
B = str(B)
print(B)

# 15. Display a text on the screen: ‘Your Name is done with HW2‘
print('Xinmiao Tan is down with HW2')