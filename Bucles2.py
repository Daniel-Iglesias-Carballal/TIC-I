
suma=0
while True:
    print("Introduzca un numeros que se sumaran, hasta que introduzca el numero 0.")

    num =int(input())
    
    suma=suma+num

    if num==0:
        break

print("La suma de los números es:",suma)