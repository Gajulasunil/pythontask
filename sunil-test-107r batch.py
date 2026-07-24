'''         diamond                    '''
# n = 5
# for i in range(1,n+1):
#     sp= ''
#     for j in range(i,n):
#         sp += ' '
#     st = ''
#     for j in range(1,i+1):
#         st += '*'
#     st1 = ''    
#     for j in range(1,i):
#         st1 +='*'
#     print(sp+st+st1) 
# for i in range(n-1,0,-1):
#     sp= ''
#     for j in range(i,n):
#         sp += ' '
#     st = ''
#     for j in range(1,i+1):
#         st += '*'
#     st1 = ''    
#     for j in range(1,i):
#         st1 +='*'
#     print(sp+st+st1)     
 
'''       centroid pyramid          ''' 
# n = 4
# for i in range(1,n+1):
#     sp = ''
#     for j in range(i,n):
#         sp += '  '
#     st = ''
#     for j in range(1,i+1):
#         if i==1 or i==n:
#             st += '* '
#         elif j==1 :
#             st += '* '
#         else:
#             st += '  '        
#     st1 = ''    
#     for j in range(1,i):
#         if i==1 or i==n:
#             st1 += '* '
#         elif  j==i-1:
#             st1 += '* '
#         else:
#             st1 += '  ' 
#     print(sp+st+st1)     
'''sand glass'''
# n = 4
# for i in range(1,n+1):
#     sp = ''
#     for j in range(1,i+1):
#         sp += '  '
#     st = ''
#     for j in range(i,n+1):
#         st += '* '
#     print(sp+st) 
# for i in range(n-1,0,-1):
#     sp = ''
#     for j in range(1,i+1):
#         sp += '  '
#     st = ''
#     for j in range(i,n+1):
#         st += '* '
#     print(sp+st)                
'''      butter fly      '''
# n = 4
# for i in range(1,n+1):
#     st = ''
#     for j in range(1,i+1):
#         st += '* '
#     sp1 = ''
#     for j in range(i,n):
#         sp1 +='  '
#     sp2 = ''
#     for j in range(i,n):
#         sp2 +='  '
#     st1 = ''
#     for j in range(1,i+1):
#         st1 += '* '
#     print(st+sp1+sp2+st1)
# for i in range(n,0,-1):
#     st = ''
#     for j in range(1,i+1):
#         st += '* '
#     sp1 = ''
#     for j in range(i,n):
#         sp1 +='  '
#     sp2 = ''
#     for j in range(i,n):
#         sp2 +='  '
#     st1 = ''
#     for j in range(1,i+1):
#         st1 += '* '
#     print(st+sp1+sp2+st1) 
'''     right alignment number triangle '''  
# n = 5 
# KeyboardInterrupt
# for i in range(1,n+1):
#     sp = ''
#     for j in range(i,n):
#         sp += '  '
#     st = ''
#     for j in range(1,i+1):
#         st += str(i-j+1)+' '  
#     print(sp+st)                    



n = 4
for i in range(1,n+1):
    star = ""
    for j in range(1,i+1):
        if(i == 1 ):
            star = star + "* "
        elif(j == 1 or j == i):
            star = star + "* "
        else:
            star = star + "  "
    space = ""
    for k in range(n,i,-1):
        space = space + "  "
    sp = ""
    for l in range(n,i,-1):
        sp = sp + "  "
    st = ""
    for m in range(1,i+1):
        if i == 1 :
            st = st + "* "
        elif m == 1 or m == i:
            st = st + "* "
        else:
            st = st + "  "
    print(star + space + sp + st)
    
for i in range(n-1,0,-1):
    star = ""
    for j in range(1,i+1):
        if(i == 1 ):
            star = star + "* "
        elif(j == 1 or j == i):
            star = star + "* "
        else:
            star = star + "  "
    space = ""
    for k in range(n,i,-1):
        space = space + "  "
    sp = ""
    for l in range(n,i,-1):
        sp = sp + "  "
    st = ""
    for m in range(1,i+1):
        if i == 1 :
            st = st + "* "
        elif m == 1 or m == i:
            st = st + "* "
        else:
            st = st + "  "
    print(star + space + sp + st)
   