import math
a = int(input("Entre com o valor de a: "))
b = int(input("Entre com o valor de b: "))
c = int(input("Entre com o valor de c: "))

delta = (b**2) - (4 * a * c)

if delta > 0:
   val_1 = math.sqrt(delta)
   val_2 = 2 * a
   x_1 = (-b - val_1) / val_2)
   x_2 = (-b + val_1) / val_2)  
   print("As raízes da equação são ", x_1, "e", x_2)     
elif  delta == 0:
      x = -b / (2 * a)  
      print("A raiz desta equação é ", x)
else:
      print("Esta equação não possui raízes reais.")