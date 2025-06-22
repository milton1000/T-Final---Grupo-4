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
        
        @Parametro: msj_inicio (str)
        
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
                        tarifa = ("AA1","Diaria", 20000)
                        return tarifa
                
                #El usuario abona la de fin de semana.
                elif num_menu == "2":
                        tarifa = ("AA2","Fin de Semana", 30000)
                        return tarifa
                
                #El usuario abona la semanal.
                elif num_menu == "3":
                        tarifa = ("AA3","Semanal", 100000)
                        return tarifa
                
                #El usuario abona la mensual o superior.
                elif num_menu == "4":
                        tarifa = ("AA4","Mes o Superior", 200000)
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
                if mes == "1" or mes == "2" or mes == "6" or mes == "7" or mes == "8" or mes == "9" or mes == "12":
                        temporada = "alta"
                        return temporada
                
                #Meses de temporada baja.
                elif mes == "3" or mes == "4" or mes == "5" or mes == "10" or mes == "11":
                        temporada = "baja"
                        return temporada
                
                #No se ingresó una opción válida.
                else:
                        print("No ingresó una opción posible, pruebe nuevamente")

def eleccion_auto(autos_disp):
        """
        @Objetivo: Obtener el auto que desea el usuario.
        @Descripción: Se le consulta al usuario el auto que desea. Se ve si esta disponible. Si está, se regresa la data del auto, si no esta se regresa False.
        
        @Parametro: autos_disp (list or tuple)
        
        @return: disonible (list or boolean)
        """
        #Ingreso del auto que se desea alquilar.
        modelo_deseado = input("Ingrese el modelo de auto deseado para alquilar: ")
        #Tomamos como valor default que el auto no esta disponible.
        disponible = False
        
        #Se recorre la lista de autos disponibles para ver si el ingresado esta presente.
        for i in autos_disp:
                #Se encuentra el modelo deseado.
                if modelo_deseado == i[0]:
                        disponible = i
        
        return disponible
        


#A partir de aquí, comienza el programa.

#Variables que pueden cambiar puesto que no se especifica de donde se obtienen:
vip_user = False
#("Auto", nro de chasis, motor, tipo de vehículo, multiplicador)
autos_disponibles = (("Ford Fiesta", 1234, "cuatro cilindros 1.6V", "cuatro puertas", 1),
                     ("Fiat Cronos", 2345, "1.3 fire.fly", "cuatro puertas", 1),
                     ("Renault Logan", 3456, "1.6L 8V 85HP", "cuatro puertas", 1),
                     ("Toyota Hilux", 4567, " 2.4L 150 CV ", "camioneta", 1.2))

#Se realiza una bienvenida al usuario.
print ("""Bienvenido al programa de alquiler de autos 2000 Automóviles - Bariloche.
       A continuación le pediremos algunos datos personales...""")

#Solicitud nombre y apellido
nombre_user = input("Nombre: ")
apellido_user = input("Apellido: ")
#Se solicita origen del usuario (Función preguntar_origen) 
origen_user = preguntar_origen()

#Se solicita nro de pasaporte si es internacional y nro de DNI si es argentino.
if origen_user == "Internacional":
        #Se le solicita al usuario el número de pasaporte (Función pedir_numero). Un MAX de 25 números y mensaje de solicitud de pasaporte y reporte de error.
        pasaporte_user = pedir_numero(25, "Número de pasaporte: ", "Parece que lo ingresado no sigue los lineamientos solicitados. \nPruebe nuevamente...")
        #Al ser extranjero, no tiene DNI, por tanto en la tarifa el campo DNI aparecerá vacío.
        dni_user = "-"
#El usuario es argentino
else:
        #Se le solicita al usuario el número de DNI (Función pedir_numero). Un MAX de 8 números y mensaje de solicitud de pasaporte y reporte de error.
        dni_user = pedir_numero(8, "Documento Nacional de Identidad: ", "Parece que lo ingresado no sigue los lineamientos solicitados. \nPruebe nuevamente...")
        #Al ser argentino, no tiene pasaporte, por tanto en la tarifa el campo pasaporte aparecerá vacío.
        pasaporte_user = "-"

#Se solicita el número de teléfono personal.
tel_user = pedir_numero(15, "Ingrese su número de teléfono personal: ", "Parece que lo ingresado no sigue los lineamientos solicitados. \nRecuerde incluir el código de zona y pais \nPruebe nuevamente...")
#Se solicita datos domiciliarios (Función pedir_domicilio).
domi_user = pedir_domicilio("A continuación ingrese los datos de su domicilio personal")
#Se solicita nombre de empresa laboral.
empresa_user = input("Ingrese el nombre de su empresa laboral: ")
#Se solicita el número de teléfono laboral (Función pedir_domicilio).
tel_trabajo = pedir_numero(15, "Ingrese su número de teléfono laboral: ", "Parece que lo ingresado no sigue los lineamientos solicitados. \nRecuerde incluir el código de zona y pais \nPruebe nuevamente...")
#Se solicita datos de domicilio laboral.
domi_trabajo = pedir_domicilio("A continuación ingrese los datos de su domicilio laboral")

#Se obtiene datos de hotel o agencia asoc si no vive en bariloche.
if origen_user == "Internacional" or origen_user == "Argentino":
        hotel_user = input("Ingrese el nombre de su hotel o agencia asociada: ")

#Si el usuario es VIP.
if vip_user == True:
        #Entrega de tarjeta.
        print("Aqui tiene su tarjeta VIP con 10 por ciento de descuento!\nRecuerda que caduca el 20 de julio de 2026")
        #Registramos el descuento para luego incorporarlo a la suma total.
        dto_vip = 10
        forma_pago = "Tarjeta VIP"

#Si el usuario no es VIP
else:
        #Se registra forma de pago y como contactó la agencia.
        forma_pago = input("Ingrese su forma de pago: ")
        cntact_agencia = input("¿Cómo contactó a la agencia?: ")
        dto_vip = 0

#Elección de autos a partir de los que estan disponibles.
auto_user = eleccion_auto(autos_disponibles)

#El auto no está dentro de los autos disponibles.
if auto_user == False:
        print("El auto fue rechazado porque no está disponible ahora mismo")

#El auto si esta disponible.
else:
        print(f"""Modelo: {auto_user[0]}
              Número de chasis: {auto_user[1]}
              Motor: {auto_user[2]}
              Tipo de Vehículo: {auto_user[3]}""")
        #Consulta tarifa (Función consultar_tarifa).
        tarifa_user = consultar_tarifa()
        #Consulta mes de alquiler (Función consultar_mes_de_alquiler). Se obtiene si temporada alta o baja.
        temporada_user = consultar_mes_de_alquiler()
        #Consulta zona geográfica principal.
        zona_user = input("Ingrese la zona geográfica a circular con el auto: ")
        #Cobro del seguro brindado por la Comisión nacional de seguro.
        print(f"""Se le informa que deberá abonar el seguro proporcionado por la Comisión Nacional de Seguro
              Código: 56748
              Nómbre: {nombre_user}
              Importe: 30000$
              """)
        #Solicitud de edad (Función pedir_numero).
        edad_user = pedir_numero(3, "Le solicitamos que ingrese su edad: ", "Inserte su edad de forma numérica por favor. \nIntenteno nuevamente a continuación...")

        #Si la edad del usuario es mayor o igual a 25.
        if edad_user >=25:
                #Ahora se empieza a acumular el total a pagar. Tarifa a abonar por el multiplicador.
                total_a_pagar = tarifa_user[2] * auto_user[4]

                #Recargos por temporada y zona geográfica. Si la temporada es alta y está en una zona con valor extra.
                if temporada_user == "alta" and (zona_user == "Cerro Catedral" or zona_user == "Ruta 40" or zona_user == "Circuito Chico"):
                        #20% de aumento.
                        total_a_pagar *= 1.2
                        recargo_tz = "20%"

                #Si la temporada es alta o está en una zona con valor extra.
                elif temporada_user == "alta" or zona_user == "Cerro Catedral" or zona_user == "Ruta 40" or zona_user == "Circuito Chico":
                        #10% de aumento.
                        total_a_pagar *= 1.1
                        recargo_tz = "10%"
                        
                #Si la temporada es baja y no esta en una zona con valor extra.
                else:
                        #No hay aumento
                        recargo_tz = "0%"
                
                #Se agrega al monto total, una vez hechos todos los aumentos de la compañia, los aumentos externos: seguro de nieve y el de CNdS.
                total_a_pagar += 50000
                
                #Se imprime la factura al cliente
                print(f"""Factura:
                      {nombre_user} {apellido_user}
                      origen: {origen_user}
                      DNI: {dni_user}
                      Pasaporte: {pasaporte_user}
                      Teléfono Personal: {tel_user}
                      Domicilio Personal
                      Pais: {domi_user[0]}
                      Ciudad: {domi_user[1]}
                      Barrio: {domi_user[2]}
                      Calle: {domi_user[3]}
                      Número de edificación y/o departamento:
                      Teléfono de trabajo: {tel_trabajo}
                      Domicilio de trabajo
                      Pais: {domi_trabajo[0]}
                      Ciudad: {domi_trabajo[1]}
                      Barrio: {domi_trabajo[2]}
                      Calle: {domi_trabajo[3]}
                      Automovil: {auto_user[0]}
                      Número de Chasis: {auto_user[1]}
                       Motor: {auto_user[2]}
                      Tipo de Vehículo: {auto_user[3]}
                      Código de Tarifa: {tarifa_user[0]}
                      Nombre de Tarifa: {tarifa_user[1]}
                      Precio de Tarida: {tarifa_user[2] * auto_user[4]}$
                      Seguro de la Comisión Nacional de Seguridad: 30000$
                      Seguro contra nieve: 20000$
                      Temporada: {temporada_user}
                      Zona geográfica: {zona_user}
                      Recargo por temporada y zona geográfica: {recargo_tz}
                      Descuento VIP: {dto_vip}""")

                #Se expone el monto a pagar.
                print(f"Usted debe pagar: {total_a_pagar}$")
                
                #Se inicia proceso de pago. Bucle para asegurar un monto que sigue los lineamientos.
                while True:
                        #Se solicita el total a pagar.
                        pago_ingresado = pedir_numero(len(str(total_a_pagar)), "Ingrese el total a abonar, recuerde que no se puede pagar más del total ", "Parece que no siguió los lineamientos requeridos. \nIntente nuevamente porfavor...")
                        
                        #Si el pago es menor o igual al total.
                        if pago_ingresado <= total_a_pagar:
                                print(f"Usted adeuda: {total_a_pagar-pago_ingresado}")
                                break

                        #Si el pago es mayor al total.
                        else:
                                print("No se aceptan montos mayores al requerido")
        
        #La edad ingresada fue menor a 25.
        else:
                print("Los menores de 25 no pueden alquilar automóviles")                        
