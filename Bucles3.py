def primo(n):
    x=2
    
    for i in range(x,n): 
        if(n%i==0):
            return False
    return True

for i in range (1,101):
    if(primo(i)):
        print(i,"es primo")
    else:
        print(i,"no es primo")