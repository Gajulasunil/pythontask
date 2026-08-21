''' Write a Python program to check if a number is even or odd.'''
# def even_or_odd():
#     num = int(input('Enter your number:'))
#     if num%2 == 0:
#         print(num,'is even')
#     else:
#         print(num,'is odd')
# even_or_odd()
'''Write a Python program to find the largest of three numbers.'''
# def lar_num():
#     a = int(input('Enter your 1 number:'))
#     b = int(input('Enter your 2 number:'))
#     c = int(input('Enter your 3 number:'))
#     if a<b or a<c:
#         if b>c:
#             print(b,'largest of three number')
#         else:
#             print(c,'largest of three number')
#     else:
#         print(a,'largest of three number')
# lar_num()
'''Write a Python program to check if a string is a palindrome.'''
# def palindrome():
#     s = input('Enter You Are String :')
#     rem = ''
#     for i in s:
#         rem = i + rem    
#     print(rem)
# palindrome()
'''Write a Python program to calculate the factorial of a number.'''
# def fact():
#     num = int(input('Enter a number:'))
#     sum = 1
#     for i in range(1,num+1):
#         sum = sum*i
#     print(f'factorial of {num} is :',sum)   
# fact()
'''Write a Python program to generate the Fibonacci sequence up to n terms.'''
# def fibon_():
#     n = int(input('Enter a number:'))
#     a = 0
#     b = 1
#     for i in range(n):
#         print(a,end=' ')
#         c = a+b
#         a = b
#         b = c
# fibon_()
'''Write a Python program to count the number of vowels in a string.'''
# def str_count():
#     s = input('Enter a string :')
#     a = 'AEIOUaeiou'
#     c = 0
#     for i in s:
#         if i in a:
#             c = c+1
#             print(i)
#     print('The numbers of vowels in a string :',c)
# str_count()    
'''Write a Python program to find the sum of all elements in a list.'''
# s = [1,2,3,4,5]
# sum = 0
# for i in s:
#     sum +=i
# print('sum =',sum)
'''Write a Python program to reverse a given string. '''
# def rev_str():
#     s = input('Enter a string :')
#     rev = ''
#     for i in s :
#         rev = i + rev 
#     print(rev)
# rev_str()
'''Write a Python program to check if a number is prime.'''
# def check_prime():
#     n = int(input('enter a number:'))
#     if n > 1:
#         c = 0
#         for i in range(1,n+1):
#             if n%i==0:
#                 c += 1
#         if c == 2:
#             print('prime')   
#         else:
#             if c>2:
#                 print('composite')          
#     else:
#         print('Neither prime nor composite')
# check_prime()
'''Write a Python program to print the multiplication table of a given number. '''
# def fact():
#     num = int(input('enter a number:'))
#     pro = 0
#     n = 10
#     for i in range(1,n+1):
#         pro = num *i
#         print(f'{num}*{i}=',pro)
# fact()
'''Write a Python program to find the second largest number in a list'''
