  
def origen (preguntar_origen):  
    bucle = 1
    while bucle <=1: 
        print ("Queremos saber donde vive")
        print ("Si reside en Bariloche ingrese 1")
        print ("Si es turista nacional ingrese 2")
        print ("Si es turista internacional ingrese 3")

num=int(input("Seleccione una opción:"))

match num:
    case 1:
        origen("Residente")
        bucle=6
    case 2: 
        origen("Argentino")
        bucle = 6
    case 3:
        origen("Internacional")
        bucle = 6
    case _:
        print ("No ingreso una opción posible, pruebe nuevamente")

        