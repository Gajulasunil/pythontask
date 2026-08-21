'''1. Print Numbers (1 to N) '''
# def num (n):
#     if n == 6 :
#         return n
#     print(n)
#     num(n+1)
# n = 1
# num(n)
'''2. Print Numbers (N to 1)'''
# def num(n):
#     if n == 1:
#         return n
#     print(n)
#     return num(n-1)
# n = 5
# print(num(n))
'''3. Sum of First N Numbers'''
# def sum(n,s=0):
#     if n == 0:
#         return s
#     s = s + n
#     return sum(n-1,s)
# n = 5
# print(sum(n)) 
'''4. Factorial'''       
# def fact(n,f=1):
#     if n == 0:
#         return f
#     f = f*n
#     return fact(n-1,f)
# n = 5
# print(fact(n))    
'''5. Reverse a Number'''
# def rev(n,r= 0):
#     if n == 0:
#         return r
#     res = n%10
#     r = r*10 +res
#     return rev(n//10,r)
# n = 123
# print(rev(n))
'''6. Count Digits in a Number'''
# def count(n,c=0):
#     if n == 0:
#         return c
#     return count(n//10,c+1)
# n = 134
# print(count(n))
'''7. Sum of Digits'''
# def sum(n,s=0):
#     if n == 0:
#         return s
#     s = s + n
#     return sum(n-1,s)
# n = 3
# print(sum(n))
'''8. Check Palindrome (Number)'''
# def pali(n,res=0):
#     if n == 0:
#         return res
#     rem = n%10
#     res = res*10+rem 
#     return pali(n//10,res)
# n = 151
# if n == pali(n):
#     print('palindrome')
# else:
#     print('not a palindrome')
'''9. Find Factors'''
# def fact(n,i = 1,c=0):
#     if n == i:
#         print(i)
#         return c+1
#     if n%i == 0:
#         print(i,end=',')
#         return fact(n,i+1,c+1)
#     else:
#         return fact(n,i+1,c)
# n = 6
# if fact(n) == 2:
#     print('prime')
# else:
#     print('not prime')
'''11. Find Armstrong Number'''
# def count(n,c=0):
#     if n == 0:
#         return c
#     return count(n//10,c+1)
# def arm(n,r=0):
#     if n == 0:
#         return r
#     rem = n%10
#     r = r+rem**l
#     return arm(n//10,r)
# n = 153
# l = count(n)
# if n == arm(n):
#     print('armstrong')
# else:
#     print('not a armstrong')
'''12. String Palindrome Check'''
# def pali(n,s=''):
#     if n =='':
#         return s
#     return pali(n[1:],n[0]+s)
# n = 'madam'
# rev = pali(n)
# if rev == n:
#     print('palindrome')
# else:
#     print('not a palindrome')
'''13. Fibonacci Series'''
