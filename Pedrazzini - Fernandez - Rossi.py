
def origen (preguntar_origen):    
    print ("""Queremos saber donde vive
    Si reside en Bariloche ingrese 1
    Si es turista nacional ingrese 2
    Si es turista internacional ingrese 3""")
preguntar_origen=input("Seleccione una opción:")
while True:
    if preguntar_origen==("1"):
            origen("Residente")
            break
    elif preguntar_origen==("2"):  
            origen("Argentino")
            break
    elif preguntar_origen==("3"):
            origen("Internacional")
            break
    else:
            print ("No ingreso una opción posible, pruebe nuevamente")
            
    



def pedir_numero(num):
    while True:
        num= input("Ingrese su número de teléfono:")
        if (len(num)<=7 and num.isnumeric()):
         print("Número guardado correctamante")
        break
    else: 
        print("Número inválido, ingréselo nuevamente")



def pedir_domicilio (domilicio):
  
    print("""Ingrese sus datos domicilarios como su país,
      su ciudad, su barrio, su calle y su numero de departamento""")
list_domicilio =[]
list_domicilio.append(input())
print(list_domicilio[0:4])




def consultar_tarifa(tarifa):
   
        tarifa=input("""¿Qué tarifa desea abonar?
Si desea la diaria, ingrese 1
Si desea la de fin de semana ingrese 2
Si desea la semanal ingrese 3
Si desea la de mes o superior ingrese 4""")
tarifa=[]
num=(input())
while True:
    if num==("1"):
            tarifa.insert(0,"AA1")
            tarifa.insert(1,"Diaria")
            tarifa.insert(2,"precio 1")
            break
    elif num==("2"):
            tarifa.insert(0,"AA2")
            tarifa.insert(1,"Fin de semana")
            tarifa.insert(2,"precio 2")
            break
    elif num==("3"):
           tarifa.insert(0,"AA3")
           tarifa.insert(1,"Semanal")
           tarifa.insert(2,"precio 3")
    elif num==("4"):
            tarifa.insert(0,"AA4")
            tarifa.insert(1,"Mes o superior")
            tarifa.insert(2,"precio 4")
            break
else:
            print("No ingresó una opción posible, pruebe nuevamente")
                   
print(tarifa)


def consultar_mes_de_alquiler(temporada):
    temporada=input("Ingrese el número de mes en el que rentará el automóvil:")
while True:
    mes=(input())
    if mes==("1" or "2" or "6" or "7" or "8" or "9" or "12"):
            temporada="alta"
            break
    elif    mes==("3" or "4" or "5" or "10" or "11"):
            temporada="baja"
            break

else:
        print("No ingresó una opción posible, pruebe nuevamente")