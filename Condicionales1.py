print ("Introduce dos edades:")
print ("Introduce la primera edad:")
num =int(input())
print ("Introduce la segunda edad:")
num2 =int(input())

if num < num2:
    print ("La primera edad,",num,", es menor que la segunda,",num2,".")
elif num == num2:
    print ("La primera edad,",num,", es igual que la segunda,",num2,".")
else:
    print ("La primera edad,",num,", es mayor que la segunda,",num2,".")

print ("La media de las dos edades es:")
print ((num + num2)/2)