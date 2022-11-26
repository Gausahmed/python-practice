n = 5
'''
*****
*****
*****
*****
'''
print("1.")
for i in range(0,4):
    for j in range(0,5):
        print("* ",end="")
    print()

'''
*
**
***
****
*****
'''
print("2.")
for i in range(5):
    for j in range(i+1):
        print("* ",end="")
    print()

'''
    *
   **
  ***
 ****
*****
'''
k = 2*n-1
print("3. \r")
for i in range(n):
    for j in range(0,k):
        print(end=" ")
    k-=2
    for j in range(0,i+1):
        print("* ",end="")
    print()

'''
    *  
   * *
  * * * 
* * * * * 
'''
print("4. \r")
k = n-1
for i in range(n):
    for j in range(0,k):
        print(end=" ")
    k-=1
    for j in range(0,i+1):
        print("* ",end="")
    print()

'''
* * * * *
* * * * 
* * * 
* * 
*  
'''
print("5. \r")
for i in range(n,0,-1):
    for j in range(0,i):
        print("* ",end="")
    print()

'''
* * * * *
  * * * *
    * * *
      * *
        *
'''
# print("6. \r")
# k = 2*n-2
# for i in range(n,0,-1):
#     for j in range(k,0,-1):
#         print("/ ",end="")
#     k-=2
#     for j in range(0,i):
#         print("* ",end="")
#     print()
'''
*
* *
*   *
*     *
* * * * *
'''
print("7.")
for i in range(n):
    for j in range(0,i+1):
        if j==0 or j==i or i==n-1:
            print("* ",end="")
        else:
            print(" ",end=" ")
    print()

'''
* * * * *
* * * *
* * *
* * 
* 
* 
* * 
* * * 
* * * *
* * * * *
'''
print("8. \r")
for i in range(n,0,-1):
    for j in range(0,i):
        print("* ",end="")
    print()
for i in range(n):
    for j in range(0,i+1):
        print("* ",end="")
    print()

'''
  *  
 * * 
* * * 
 * * 
  * 
'''
print("9. \r")
k = n-1
for i in range(n):
    for j in range(0,k):
        print(end=" ")
    k-=1
    for j in range(0,i-1):
        print("* ",end="")
    print()
for i in range(n-2,1,-1):
    for l in range(1,n-i):
        print(end=" ")
    for l in range(0,i-1):
        print("* ",end="")
    print()

'''
    *
  * *
* * *
  * *
    *
'''
print('10. \r')
k = 2*n-1
for i in range(n-1):
    for j in range(k):
        print(end=" ")
    k = k -2
    for j in range(i):
        print("* ",end="")
    print()

for i in range(n-1,0,-1):
    for j in range(k):
        print(end=' ')
    k = k+2
    for j in range(0,i):
        print("* ",end="")
    print()