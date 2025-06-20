def preguntar_origen():
        """
        @Objetivo: Obtener origen del usuario
        @Descripción: La función imprime un catalogo de opciones con los origenes correspondientes. De ingresar una opción no válida se repite el bucle.
        
        @return: origen (str)
        """
        #Este bucle se ejecutará hasta que el usuario ingrese en el catalogo consiguiente una opción valida. Se corta con return origen.
        while True:
                
                #Impresión del catálogo y elección del usuario.
                num_menu = input("""Queremos saber donde vive
                Si reside en Bariloche ingrese 1
                Si es turista nacional ingrese 2
                Si es turista internacional ingrese 3
                """)
                
                #El usuario es residente.
                if num_menu == "1":
                        origen = "Residente"
                        return origen
                
                #El usuario es argentino no residente.
                elif num_menu == "2":  
                        origen = "Argentino"
                        return origen
                
                #El usuario es del extranjero.
                elif num_menu == "3":
                        origen = "Internacional"
                        return origen
                
                #El usuario ingresó una opción inválida, se repite el bucle anterior.
                else:
                        print("No ingreso una opción posible, pruebe nuevamente")
            
def pedir_numero(longitud_num, msj_pedido, msj_error):
        """
        @Objetivo: Solicitar un número al usuario con una cantidad limitada de dígitos.
        @Descripción: La función solicitará un número bajo un mensaje especificado en los argumentos. De ingresar un número que sigue los lineamientos: se lo convierte a Integer y se corta el bucle. De ingresar algo que no sigue los lineamientos se informa el error y se ejecuta nuevamente el bucle.
        
        @Parametro: longitud_num (int)
        @Parametro: msj_pedido (str)
        @Parametro: msj_error (str)
        
        @return: num (int)
        """
        #Este bucle se ejecutará hasta que el usuario ingrese un número que sigue los lineamientos solicitados. Secorta con return num.
        while True:
                
                #Impresión del mensaje de pedido y obtención del número.
                num = input(msj_pedido)

                #Si lo ingresado es numérico y su lonitud es menor o igual que la solicitada.
                if len(num) <= longitud_num and num.isnumeric():
                        num = int(num)
                        return num
                
                #Si lo ingresado no sigue alguno de los dos lineamientos mencionados previamente.
                else: 
                        print(msj_error)

def pedir_domicilio (msj_inicio):
        """
        @Objetivo: Obtener la dirección del usuario.
        @Descripción: Se le consulta al usuario diferentes datos de un domicilio y a medida que contesta se van agregando estos datos a una lista con los datos domiciliarios.
        
        @Parametro: msj_inicio (msj_inicio)
        
        @return: domicilio (list)
        """
        #Se da la posibilidad en la función a inicializarla con un mensaje para especificar algo que el programador vea necesario. 
        print(msj_inicio)
        #Se crea la lista.
        domicilio =[]
        #Se ingresan los datos a la lista a medida que el usuario completa los datos.
        domicilio.append(input("Pais: "))
        domicilio.append(input("Ciudad: "))
        domicilio.append(input("Barrio: "))
        domicilio.append(input("Calle: "))
        domicilio.append(input("Número de edificación y/o departamento: "))
        #Devolvemos el domicilio especificado por el usuario.
        return domicilio

def consultar_tarifa():
        """
        @Objetivo: Hacer que el usuario elija la tarifa que desea abonar.
        @Descripción: La función imprime un catalogo de opciones con las distintas tarifas. El usuario debe elegir una y de ingresar una opción inválida se repite el bucle.
	
        @return: tarifa (tuple)
        """
        num_menu = input("""¿Qué tarifa desea abonar?
        Si desea la diaria, ingrese 1
        Si desea la de fin de semana ingrese 2
        Si desea la semanal ingrese 3
        Si desea la de mes o superior ingrese 4
        """)
        #Este bucle se ejecutará hasta que el usuario ingrese un valor válido del catálogo. Se corta con return tarifa.
        while True:
                #Impresión del catálogo y respuesta del usuario.
                num_menu = input("""¿Qué tarifa desea abonar?
                Si desea la diaria, ingrese 1
                Si desea la de fin de semana ingrese 2
                Si desea la semanal ingrese 3
                Si desea la de mes o superior ingrese 4
                """)
                
                #El usuario abona la diaria.
                if num_menu == "1":
                        tarifa = ("AA1","Diaria","precio 1")
                        return tarifa
                
                #El usuario abona la de fin de semana.
                elif num_menu == "2":
                        tarifa = ("AA2","Fin de Semana","precio 2")
                        return tarifa
                
                #El usuario abona la semanal.
                elif num_menu == "3":
                        tarifa = ("AA3","Semanal","precio 3")
                        return tarifa
                
                #El usuario abona la mensual o superior.
                elif num_menu == "4":
                        tarifa = ("AA4","Mes o Superior","precio 4")
                        return tarifa
                
                #El usuario no ingresa una opción válida.
                else:
                        print("No ingresó una opción posible, pruebe nuevamente")

def consultar_mes_de_alquiler():
        """
        @Objetivo: Hacer que el usuario elija el mes en el que alquilará el auto.
        @Descripción: Se consulta el nro de mes en el que se alquilará el automovil. En caso de ser dic-feb o jun-sep será temporada alta, sino temporada baja. En caso de que la respuesta no siga los lineamientos, se volverá a ejecutar el bucle.
	
        @return: temporada (str)
        """
        #Este bucle se ejecutará hasta que el usuario ingrese un mes válido. Se corta con return temporada.
        while True:
                #Se solicita número de mes.
                mes = input("Ingrese el número de mes en el que rentará el automóvil: ")
                
                #Meses de temporada alta.
                if mes == ("1" or "2" or "6" or "7" or "8" or "9" or "12"):
                        temporada = "alta"
                        return temporada
                
                #Meses de temporada baja.
                elif mes == ("3" or "4" or "5" or "10" or "11"):
                        temporada = "baja"
                        return temporada
                
                #No se ingresó una opción válida.
                else:
                        print("No ingresó una opción posible, pruebe nuevamente")