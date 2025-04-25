import math
def line():
   a = float(input("Ingrese el coeficiente A: "))
   b = float(input("Ingrese el coeficiente B: "))
   X1 = float(input("Ingrese el coeficiente X1: "))
   X2 = float(input("Ingrese el coeficiente X2: "))

   print(f"El coeficiente A de su ecuación de la recta es: {a}")
   print(f"El coeficiente B de su ecuación de la recta es: {b}")
   print(f"El coeficiente X1 de su ecuación de la recta es: {X1}")
   print(f"El coeficiente X2 de su ecuación de la recta es: {X2}")
   print()
   print("Para la siguiente ecuación:")
   print(f"/tY = {a}X + {b}")
   print()
   print("Dados los siguientes puntos:")
   y1 = a * X1 + b
   y2 = a * X2 +b
   print(f"P1 (50,0, {y1})")
   print(f"P2 (-32,9, {y2})")
   print()
   distancia = math.sqrt((X2 - X1) ** 2 + (y2 - y1) ** 2)
   print("La distancia entre ellos es: {distancia}")
