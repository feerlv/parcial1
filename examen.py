def descuento():
  print("Dime el precio del aluminio")
  aluminio = input()
  print ("Ahora el precio de conectores")
  conectores = input ()
  print ("Ahora el precio de cajas")
  cajas = input ()
  resultado = int (aluminio) + int (conectores) + int (cajas) 
  print ("El costo final del proyecto es", resultado)
  resultado = 270 * 5 / 100
  print("El 5% es", resultado)
  resultado = 270 - 13.5
  print("El costo menos el descuento es", resultado)

descuento ()
