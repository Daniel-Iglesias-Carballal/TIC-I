print ("Introduzca a sua edad:")
edad =int(input())
print ("Introduzca os sus ingresos:")
ingresos =int(input())

if 18<=edad or 1000<=ingresos:
    print ("Usuario ten que tributar")
else:
    print ("Usuario non ten que tributar")