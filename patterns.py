n = 5 
for i in range(1,n+1):
    star = ''
    for j in range(1,i+1):
        star += '* '
    spaces = ''
    sp=''
    for j in range((n-i)**2,0,-1):
        sp+=' '
    st=''    
    for j in range(i+1):
        st+='*'
    print(star+sp+st)    

         