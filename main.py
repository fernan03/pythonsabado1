#hola mundo con python

#salida por consola
'''
print("hola mundo soy luis")
print('hola mundo soy luis')
'''

#Entredas
#Datos primitivos
dato = None
nombre = "luis"
edad = 19
estatura = 1.86
hinchaDelMejor = True

#salida por teclado
print("hola: ",nombre+ "tu edad es:",edad)
print(f'hola {nombre} tu edad es {edad} tu estatura es {estatura}')

#Recibir datos por teclado
ciudad = input("digita la ciudad donde vives: ")
print(f'la ciudad donde usted vives es: {ciudad} ')

#Recivir datos numericos por teclado
numero1=int(input("Digita un numero: "))
numero2=int(input("Digita otro numero:"))
print(f'el primer numero es {numero1} y el numero dos es {numero2}')

#Operadores aritmeticos
#(+ - * / %)
suma = numero1 + numero2
print(f'la suma de los numeros es {suma}')