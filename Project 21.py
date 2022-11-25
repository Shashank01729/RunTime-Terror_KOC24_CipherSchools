#Project 21
'''
Your task is to find if it is possible to cut the cake in the below mentioned ways for a given value of N.

Given an integer N and a cake which can be cut into pieces, each cut should be a straight line going from the center of the cake to its border. Also, the angle between any two cuts must be a positive integer. Two pieces are equal if their appropriate angles are equal. 
The given cake can be cut in following three ways: 
•	Cut the cake into N equal pieces.
•	Cut the cake into N pieces of any size.
•	Cut the cake into N pieces such that no two of them are equal.
(Student is free to decide the input and output layout for this mini project)
'''

cakeangle=eval(input("Enter the Angle of the Cake: ")) #NOTE: Take cakeangle 360 degree in normal case
N=eval(input("Enter N: "))
if(cakeangle%N==0):
    print("YES the cake will cut in equal pieces of size",N)
else:
    print("NO the cake will not cut in equal pieces of size",N)
if(N>cakeangle): #Only when N is greater than cake angle cake can't be cut into pieces
    print("NO the cake will not cut in any piece of size",N)
else:
    print("YES the cake will cut in any piece of size",N)
n=1 # start subtracting the cake
for i in range(N):
    cakeangle-=n
    n+=1
    if(cakeangle<0):
        print("NO the cake will not cut into",N,"pieces such that no two of them are equal",N)
        break
else:
        print("YES the cake will cut into",N,"pieces such that no two of them are equal",N)


####################################################################################################
####################################################################################################
########################### I have made many ways to solve this problem ############################
################################### Below are given the codes ######################################
####################################################################################################
####################################################################################################
#Considering the test cases:
'''
1) Cut the cake into N equal pieces.
2) Cut the cake into N pieces of any size.
3) Cut the cake into N pieces such that no two of them are equal.
'''
#OUTPUT FORMAT IS y y n LIKE THIS FOR THE TEST CASES RESPECTIVELY


#Way1:
'''
n=int(input())
while(n>0):
    res=""
    temp=int(input())
    if 360%temp==0:
        res=res+"y "
    else:
        res=res+"n "
    if temp<=360:
        res=res+"y "
    else:
        res=res+"n "
    if (temp*(temp+1)/2)<=360:
        res=res+"y "
    else:
        res=res+"n "
    print(res)
    n=n-1
'''

#Way2:
'''
t=int(input())
for k in range(t):
    n = int(input())
    options = ['n', 'n', 'n']
    if 360%n==0:
        options[0] = 'y'
    if n<=360:
        options[1] = 'y'
    if n <27:
        options[2] = 'y'
    print(*options)
'''

#Way3:
'''
for _ in range(int(input())):
    N = int(input())
    if N > 360:
        print('n n n')
    else:
        res = []
        if 360%N == 0:
            res.append('y')
        else:
            res.append('n')
        res.append('y')
        if N*(N+1)//2 <= 360:    
            res.append('y')
        else:
            res.append('n')
        print(*res)
'''

#Way4:
'''
for _ in range(int(input())):
    N = int(input())
    if N > 360:
        print('n n n')
    else:
        res = []
        res.append('y' if 360%N == 0 else 'n')
        res.append('y')
        res.append('y' if N*(N+1)//2 <= 360 else 'n' )
        print(*res)
'''

#Way5:

'''
t=int(input())
while t>0:
    t-=1 
    n=int(input())
    a,b,c="","",""
    if 360%n==0:
        a='y'
    else:
        a='n'
    if n<=360:
        b='y'
    else:
        b='n'
    if n<27:
        c='y'
    else:
        c='n'
    print(f"{a} {b} {c}")
    
'''
