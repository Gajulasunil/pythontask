# square
# n = 4
# for i in range(1,n+1):
#     star = ''
#     for j in range(n):
#         star +=' * '
#     print(star)
# rectangle
# n = 4
# for i in range(1,n+1):
#     star =''
#     for j in range(1,n*2+1):
#         star += ' * '
#     print(star)    
# left alignment 
# n = 4
# for i in range(1,n+1):
#     star = ''
#     for j in range(i):
#         star += ' * '
#     print(star)    
#right alignment 
# n= 4
# for i in range(1,n+1):
#     spaces = ''    
#     for j in range(i,n):
#         spaces = spaces + '  '
#     star = ''    
#     for j in range(1,i+1):
#         star +='* '    
#     print(spaces + star)  
# inverted left alinement
# n = 5
# for i in range(1,n+1):
#     star = ''
#     for j in range(i,n+1):
#         star += '* '
#     print(star)                        
# inverted right alinement
# n = 5
# for i in range(1,n+1):
#     spaces = ''
#     for j in range(1,i):
#         spaces = spaces + '  '
#     star = ''
#     for j in range(n+1,i,-1):
#         star = star + '* '
#     print(spaces + star)  
#  centered pyramid
# n = 5
# for i in range(1,n+1):
#     spaces = ''
#     for j in range(i,n):
#         spaces = spaces + '  '
#     star1 = ''    
#     for j in range(1,i+1):
#         star1 += '* '
#     star2 = ''
#     for j in range(1,i):
#         star2 += '* '
#     print(spaces + star1 + star2)    
# centred diamond
# n = 5 
# for i in range(1,n+1):
#     spaces = ''
#     for j in range(i,n):
#         spaces +='  '
#     star1 = '' 
#     for j in range(1,i+1):
#         star1 +='* '
#     star2 = ''    
#     for j in range(1,i):
#         star2 +='* '
#     print(spaces + star1 + star2)   
# for i in range(n-1,0,-1):
#     spaces = ''
#     for j in range(i,n):
#         spaces +='  '
#     star1 = '' 
#     for j in range(1,i+1):
#         star1 +='* '
#     star2 = ''    
#     for j in range(1,i):
#         star2 +='* '
#     print(spaces + star1 + star2)     
# butterfly 
# n = 5
# for i in range(1,n+1):
#     star1 = ''
#     for j in range(1,i+1):
#         star1 +='* '
#     sp1 = ''    
#     for j in range(i,n):
#         sp1 +='  '
#     sp2 = ''    
#     for j in range(i,n):
#             sp2 +='  '
#     star2 = ''
#     for j in range(1,i+1):
#         star2 +='* '        
#     print(star1 + sp1 + sp2 +star2)
# for i in range(n-1,0,-1):
#     star1 = ''
#     for j in range(1,i+1):
#         star1 +='* '
#     sp1 = ''    
#     for j in range(i,n):
#         sp1 +='  '
#     sp2 = ''    
#     for j in range(i,n):
#             sp2 +='  '
#     star2 = ''
#     for j in range(1,i+1):
#         star2 +='* '        
#     print(star1 + sp1 + sp2 +star2)          
# 10.	Left-Aligned Half Diamond
# n = 5
# for i in range(1,n+1):
#     star1 = ''
#     for j in range(1,i+1):
#         star1 += '* '
#     print(star1)    
# for i in range(1,n+1):
#     star2 = ''    
#     for j in range(i,n):
#         star2 += '* '  
#     print(star2)                                      
# 11.	Right-Aligned Half Diamond
# n = 5
# for i in range(1,n+1):
#     sp1 = ''
#     for j in range(i,n):
#         sp1 += '  '
#     star = ''
#     for j in range(1,i+1):
#         star += '* ' 
#     print(sp1+star)  
# for i in range(n-1,0,-1):
#     sp1 = ''
#     for j in range(i,n):
#         sp1 += '  '
#     star = ''
#     for j in range(1,i+1):
#         star += '* ' 
#     print(sp1+star)        
#12.	Sandglass Pattern
# n = 5
# for i in range(1,n+1):
#     sp1 = ''
#     for j in range(1,i+1):
#         sp1 += '  '
#     star1 = ''    
#     for j in range(i,n+1):
#         star1 += '* '
#     print(sp1+star1) 
# for i in range(n-1,0,-1):
#     sp1 = ''
#     for j in range(1,i+1):
#         sp1 += '  '
#     star1 = ''    
#     for j in range(i,n+1):
#         star1 += '* '
#     print(sp1+star1) 
'''              hollow pattern                     '''  
# 16.	Hollow Square Pattern
# n = 4 
# for i in range(1,n+1):
#     star  = ''
#     for j in range(1,n+1):
#         if i==1 or i==n:
#             star += '* '
#         elif j==1 or j==n:
#             star += '* ' 
#         else:
#             star += '  '   
#     print(star)         
#17.	Hollow Rectangle Pattern
# m = 4
# n = 5
# for i in range(1,m+1):
#     star = ''
#     for j in range(1,n+1):
#         if i==1 or i==m:
#             star += '* ' 
#         elif j==1 or j==n:
#             star += '* '
#         else:
#             star += '  '
#     print(star)  
# 18.	Hollow Right-Angled Triangle (Left-Aligned)
# n = 5
# for i in range(1,n+1):
#     star = ''
#     for j in range(1,i+1):
#         if i==1 or i==n:
#             star += '* '
#         elif j==1 or j==i:
#             star += '* '
#         else:
#             star += '  '        
#     print(star)   
# 19.	Hollow Right-Angled Triangle (Right-Aligned)
# n = 5
# for i in range(1,n+1):
#     sp = ''
#     for j in range(i,n):
#         sp += '  '
#     star = ''    
#     for j in range(1,i+1):
#         if i==1 or i==n:
#             star += '* '
#         elif j==1 or j==i:
#             star += '* '
#         else:
#             star += '  '    
                     
#     print(sp + star)               
# 20.	Hollow Inverted Triangle (Left-Aligned)
# n = 5
# for i in range(1,n+1):
#     star = ''
#     for j in range(i,n+1):
#         if i==1 or i==n:
#             star += '* '
#         elif j==i or j==n:
#             star += '* ' 
#         else:
#             star += '  '             
#     print(star)
# 21.	Hollow Inverted Triangle (Right-Aligned)
# n = 5
# for i in range(1,n+1):
#     sp = ''
#     for j in range(1,i+1):
#         sp += '  '
#     star = ''
#     for j in range(i,n+1):
#         if i==1 or i==n:
#             star += '* '
#         elif j==i or j==n:
#             star += '* '
#         else :
#             star += '  '        
#     print(sp + star)   
#  22.	Hollow Pyramid Pattern    
# n = 5
# for i in range(1,n+1):
#     sp =''
#     for j in range(i,n):
#         sp += '  '
#     star1 = ''    
#     for j in range(1,i+1):
#         if i == 1 or i ==n :
#             star1 += '* '
#         elif j == 1 :
#             star1 += '* '
#         else:
#             star1 += '  '          
#     star2 = ''
#     for j in range(1,i):
#         if i == 1 or i == n:
#             star2 += '* '
#         elif  j==i-1:
#             star2 += '* '
#         else:
#             star2 += '  '
#     print(sp + star1 + star2)           
#23.	Hollow Diamond Pattern                         
# n = 5
# for i in range(1,n+1):
#     sp =''
#     for j in range(i,n):
#         sp += '  '
#     star1 = ''    
#     for j in range(1,i+1):
#         if i == 1  :
#             star1 += '* '
#         elif j == 1 :
#             star1 += '* '
#         else:
#             star1 += '  '          
#     star2 = ''
#     for j in range(1,i):
#         if i == 1 :
#             star2 += '* '
#         elif  j==i-1:
#             star2 += '* '
#         else:
#             star2 += '  '
#     print(sp + star1 + star2)
# for i in range(n-1,0,-1):
#     sp =''
#     for j in range(i,n):
#         sp += '  '
#     star1 = ''    
#     for j in range(1,i+1):
#         if i == 1 or i ==n :
#             star1 += '* '
#         elif j == 1 :
#             star1 += '* '
#         else:
#             star1 += '  '          
#     star2 = ''
#     for j in range(1,i):
#         if i == 1 or i == n:
#             star2 += '* '
#         elif  j==i-1:
#             star2 += '* '
#         else:
#             star2 += '  '
#     print(sp + star1 + star2)  
# 24.	Hollow Butterfly Pattern
n = 5
for i in range(1,n+1):
    st1 = ''
    for j in range(1,i+1):
        if i==1 :
            st1 += '* '
        elif j==1 or j==i:
            st1 += '* '
        else:
            st1 += '  '        
    sp1 = ''
    for j in range(i,n):
        sp1 += '  ' 
    sp2 = ''
    for j in range(i,n):
        sp2 += '  '
    st2 = ''    
    for j in range(1,i+1):
        if i==1 :
            st2 += '* '
        elif j==1 or j==i:
            st2 += '* '
        else:
            st2 += '  ' 
    print(st1+sp1+sp2+st2)  
for i in range(n,0,-1):
    st1 = ''
    for j in range(1,i+1):
        if i==1 :
            st1 += '* '
        elif j==1 or j==i:
            st1 += '* '
        else:
            st1 += '  '        
    sp1 = ''
    for j in range(i,n):
        sp1 += '  ' 
    sp2 = ''
    for j in range(i,n):
        sp2 += '  '
    st2 = ''    
    for j in range(1,i+1):
        if i==1 :
            st2 += '* '
        elif j==1 or j==i:
            st2 += '* '
        else:
            st2 += '  ' 
    print(st1+sp1+sp2+st2)                                                
        