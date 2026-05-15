print("Introduzca un nunero de numeros pares:")
num =int(input())
for i in range(num+1):
    if (i%2 == 0): 
        print(i, "es par")
    else:
        print (i,"es impar")