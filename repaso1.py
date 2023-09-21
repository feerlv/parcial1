def descuento():
  print("Dame un precio x")
  precio = input ()
  print("Número que será el descuento")
  descuento = input ()
  resultado = int (precio) * int (descuento) / 100
  print("El resultado es", resultado)

descuento()
