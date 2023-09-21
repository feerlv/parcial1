def area_perimetro():
  print("Dime la base de tu rectángulo")
  base = input ()
  print("Ahora dime la altura")
  altura = input ()
  resultado = int (base) * int (altura)
  print("El área es", resultado)
  resultado = 2 * int (base) + int (altura)
  print("El perímetro es", resultado)

area_perimetro()
