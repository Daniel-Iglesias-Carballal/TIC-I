

def factorial(n):

    fac=1
    for i in range(1,n+1):
        fac=fac*i
    return fac

def media(list,lon):
    
    suma=0
    for i in list:
        suma=suma+i
    return suma/lon

def mayor(list):

    max=list[0]
    for i in list:
        if(max < i ):
            max=i
    return max

lista=[]
print("")
print("Introduce 4 números.")
print("Introduce el primer número:")
num1= int(input())
lista.append(num1)

print("Introduce el segundo número:")
num2= int(input())
lista.append(num2)

print("Introduce el tercer número:")
num3= int(input())
lista.append(num3)

print("Introduce el cuarto número:")
num4= int(input())
lista.append(num4)
print("")

while True:
    print("------------------------------------------------------------------------")
    print(" ")
    print("Escriba el número de la opción que desea aplicar.")
    print("1.Calcular el factorial de los números.")
    print("2.Calcular la media aritmética.")
    print("3.Calcular el mayor de los números.")
    print("4.Salir del programa.\n")

    opcion= int(input())

    match opcion:
        case 1:
            print("")
            print("1.Calcular el factorial de los números")
            for i in lista:
                f=factorial(i)
                print("El factorial es:",f)
        case 2:
            print("")
            print("2.Calcular la media aritmética.")
            m=media(lista,4)
            print("La media aritmetica es:",m,"\n")
        case 3:
            print("")
            print("3.Calcular el mayor de los números.")
            y=mayor(lista)
            print("El mayor de los numeros es:",y,"\n")
        case 4:
            print("")
            print("4.Salir del programa.")
            break