
def preguntar_origen():
        num_menu = input("""Queremos saber donde vive
        Si reside en Bariloche ingrese 1
        Si es turista nacional ingrese 2
        Si es turista internacional ingrese 3
        """)
        
        while True:
                
                if num_menu == "1":
                        origen = "Residente"
                        return origen
                
                elif num_menu == "2":  
                        origen = "Argentino"
                        return origen
                
                elif num_menu == "3":
                        origen = "Internacional"
                        return origen
                
                else:
                        print("No ingreso una opción posible, pruebe nuevamente")
            

def pedir_numero(longitud_num, msj_pedido, msj_error):
    
        while True:
                num = input(msj_pedido)
        
                if len(num) <= longitud_num and num.isnumeric():
                        num = int(num)
                        return
                else: 
                        print(msj_error)



def pedir_domicilio (msj_inicio):
        print(msj_inicio)
        domicilio =[]
        domicilio.append(input("Pais: "))
        domicilio.append(input("Ciudad: "))
        domicilio.append(input("Barrio: "))
        domicilio.append(input("Calle: "))
        domicilio.append(input("Número de edificación y/o departamento: "))
        return domicilio



def consultar_tarifa():
        num_menu = input("""¿Qué tarifa desea abonar?
        Si desea la diaria, ingrese 1
        Si desea la de fin de semana ingrese 2
        Si desea la semanal ingrese 3
        Si desea la de mes o superior ingrese 4
        """)

        while True:     
                if num_menu == "1":
                        tarifa = ("AA1","Diaria","precio 1")
                        return tarifa
                elif num_menu == "2":
                        tarifa = ("AA2","Fin de Semana","precio 2")
                        return tarifa
                elif num_menu == "3":
                        tarifa = ("AA3","Semanal","precio 3")
                        return tarifa
                elif num_menu == "4":
                        tarifa = ("AA4","Mes o Superior","precio 4")
                        return tarifa
                else:
                        print("No ingresó una opción posible, pruebe nuevamente")

def consultar_mes_de_alquiler():
        
        while True:
                
                mes = input("Ingrese el número de mes en el que rentará el automóvil: ")
                
                if mes == ("1" or "2" or "6" or "7" or "8" or "9" or "12"):
                        temporada = "alta"
                        return temporada
                
                elif mes == ("3" or "4" or "5" or "10" or "11"):
                        temporada = "baja"
                        return temporada

                else:
                        print("No ingresó una opción posible, pruebe nuevamente")