print ("Queremos saber donde vive")
print ("Si reside en Bariloche ingrese 1")
print ("Si es turista nacional ingrese 2")
print ("Si es turista internacional ingrese 3")

def origen (preguntar_origen):    

    preguntar_origen=int(input("Seleccione una opción:"))

    match preguntar_origen:
        case 1:
            origen("Residente")
       
        case 2: 
            origen("Argentino")
      
        case 3:
            origen("Internacional")
      
        case _:
            print ("No ingreso una opción posible, pruebe nuevamente")
            




def pedir_numero(num):
        print("Ingrese su número de teléfono:")
num= input()

if (len(num)<=7 and num.isnumeric()):
    print("muy bien")

else: 
  print("Número inválido, ingréselo nuevamente:")

def pedir_domicilio (domilicio):
    list_domicilio =([])
print("Ingrese sus datos domicilarios:")
print("Ingrese su pais:")
list_domicilio.append(input())
print("Ingrese su ciudad:")
list_domicilio.append(input())
print("Ingrese su Barrio:")
list_domicilio.append(input())
print("Ingrese su Calle:")
list_domicilio.append(input())
print("Ingrese su número de departamento:")
list_domicilio.append(input())
print(list_domicilio)


def consultar_tarifa(tarifa):
    print("¿Qué tarifa desea abonar?")
print("Si desea la diaria, ingrese 1")
print("Si desea la de fin de semana ingrese 2")
print("Si desea la semanal ingrese 3")
print("Si desea la de mes o superior ingrese 4")
tarifa=([])
num=int(input())
match num:

        case 1:
            tarifa.insert(0,"AA1")
            tarifa.insert(1,"Diaria")
            tarifa.insert(2,"precio 1")

        case 2:
            tarifa.insert(0,"AA2")
            tarifa.insert(1,"Fin de semana")
            tarifa.insert(2,"precio 2")

        case 3:
           tarifa.insert(0,"AA3")
           tarifa.insert(1,"Semanal")
           tarifa.insert(2,"precio 3")

        case 4:
            tarifa.insert(0,"AA4")
            tarifa.insert(1,"Mes o superior")
            tarifa.insert(2,"precio 4")
        
        case __:
            print("No ingresó una opción posible, pruebe nuevamente")
            
            
print(tarifa)





    
    