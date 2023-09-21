MULTIPLICACION 

def multiplicacion (a,b):
  x = a * b
  return x

def division (a,b):
  x = a / b
  return x

print ("Dame el primer número")
a = int (input())
print ("Dame el segundo número")
b = int(input())
print ("La multiplicacion da",multiplicacion (a,b), "Y la division da", division (a,b))

AREA
def area_triangulo ():
  print ("Dame la base")
  base = input ()
  print ("Dame la altura")
  altura = input()
  resultado = int (base) * int (altura) / 2
  print ("El area es", resultado)

area_triangulo ()


CONVERSIONES 
def convertir ():
  print("Dame un numero en km")
  km = input ()
  resultado = int (km) * 1000
  print ("la conversion es",resultado)

convertir ()

