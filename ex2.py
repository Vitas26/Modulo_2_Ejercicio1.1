#Ejercicio de arreglos desde el uno hasta n  identificar cuales son primos
#Usar por lo menos un for  y un if
#ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKGMSLpZLbUEwzjmx8i8oZ0rZ8J01GE7US7i8B3C3Vi/ vitas.scrapy@hotmail.com
def primos():                                       #Creamos una función
  print("Agregue el valor, debe de ser mayor a 1: ")#Imprimimos en la consola el str
  num=int(input())                                  #Hacemos una variable de int
  if num < 0:                                       #Hacemos el primer loop con un If
    print("Número no válido")                       #Si la variable es menor a 0 no se ejecuta
  else :
    lst = list(range(1, num+1))                     #Si es positivo el número se crea el arreglo
    print(lst)                                      #Se imprime el arreglo
    def f(n):                                       #Hacemos una nueva función para detectar los números primos
      return all([not n%x==0 for x in range (2,n)]) #Regresa todos los números que sean primos
    for i in range(1,num+1):                        #Los guarda en un nuevo arreglo
      i,f(i)
      num_primos = []
      for lNum in range(1, num+1):
          if (f(lNum)):
            num_primos.append(lNum)
    print(num_primos)
primos()                                            #Llamamos a la función