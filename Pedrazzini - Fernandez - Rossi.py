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



#A partir de aquí, comienza el programa.
# Se realiza una bienvenida del programa al usuario y se le pide su nombre y apellido
print ("""Bienvenido al programa de alquiler de autos 2000 Automóviles - Bariloche.
Para comenzar, ingrese su nombre y apellido a continuación""")
Nombre= input("Nombre:")
Apellido= input("Apellido:")

##Se llama a la función 1 
preguntar_origen()

#Se pregunta si el usuario es Internacional. Si la respuesta es si, se pide el pasaporte. Caso contrario,
#se pide el DNI

if preguntar_origen =="Internacional":
        print(input("Ingrese nu número de pasaporte:"))

else:
        print("Ingrese su número de DNI:")
        DNI=pedir_numero(8)


#Se solicita el número de teléfono personal
print("Ingrese su número de teléfono personal:")
tel_personal=pedir_numero(15)

#Se pide al usuario sus datos domiciliarios
print("Ingrese sus datos domiciliarios:")
domicilio_personal=pedir_domicilio()

#Se pide al usuario el nombre de su empresa laboral
print(input("Ingrese el nombre de su empresa laboral:"))
empresa=input()

#Se pide al usuario el número de teléfono laboral
print("Ingrese su número de teléfono laboral:")
tel_laboral=pedir_numero(15)

#Se pide al usuario el domicilio laboral
print("Ahora ingrese los datos domiciliarios de su empresa:")
domicilio_laboral=pedir_domicilio()

#Se pregunta al usuario si es internacional o argentino
#Si la respuesta es internacional, se le pedirá el nombre del hotel o agencia asociada
#Caso contrario, si es Argentino, no se le pedirá nada.
if preguntar_origen=="Internacional":
        print(input("Ingrese el nombre de su hotel o agencia asociada:"))
        hotel_o_agencia=input()
        
#Se pregunta al usuario si es VIP
VIP=True

if VIP == True:
        print("Aqui tiene su tarjeta con 10 por ciento de descuento!")
else:
        print(input("Ingrese su forma de pago:"))
        print(input("¿Cómo contactó a la agencia?:"))

#Se solicita al usuario ingresar el auto a alquilar
autos_disponibles=["Ford Fiesta", "Fiat Chronos","Renault Logan"]
print(input("Ingrese el modelo de auto deseado para alquilar:"))
modelo_deseado=input()
if modelo_deseado=="Ford Fiesta":
        print("""Modelo: Ford Fiesta
                 N° Chasis: 11650)
                 Motor:1.6
                 Tipo de Vehiculo: Sedan""")

elif modelo_deseado=="Fiat Chronos":
        print("""Modelo: Fiat Chronos
                 N° Chasis: 54665)
                 Motor:1.6
                 Tipo de Vehiculo: Sedan""")
        
elif modelo_deseado=="Renault Logan":
        print("""Modelo: Renault Logan
                 N° Chasis: 34975)
                 Motor:1.6
                 Tipo de Vehiculo: Sedan""")

else: 
        print("Auto Rechazado por falta de disponibilidad")

#Se le pedirá al usuario la tarifa a elegir
consultar_tarifa()
#Se le preguntará al usuario sobre el mes de alquiler del rodado
consultar_mes_de_alquiler()

#Se le preguntará al usuario sobre la zona geográfica
print(input("Ingrese la zona geográfica a circular con el auto:"))
zona_geografica=input()

#Se cobra un seguro brindado por la Comision Nacional de Seguros y otro especial por tierra o nieve.
print("Se le cobrará un seguro para su vehículo brindado por la CNdS:")
CNds=30000
seguro_especial=20000

print("Nombre:",Nombre, 
      "Código Nro: 564",
      "Importe CNds:",CNds,
      "Importe seguro especial:",seguro_especial)


#Se le solicitará la edad al usuario, si tiene más de 25 puede alquilar. Si no, no está permitido.
print(input("Ingrese su edad:"))
edad=pedir_numero(3)

if edad >=25:
        total_a_pagar=CNds+seguro_especial+consultar_tarifa

else:
        print("Los menores de 25 no pueden alquilar automóviles")

#Según zona geográfica y temporada, se añadirán los siguientes recargos
if consultar_mes_de_alquiler()=="alta":
        recargo=((total_a_pagar*20)/100)
        print("Tiene un recargo del 20 por ciento, por lo tanto, el total a pagar es:",total_a_pagar)
elif consultar_mes_de_alquiler()=="baja":
        recargo=((total_a_pagar*10)/100)
        print("Tiene un recargo del 10 por ciento, por lo tanto, el total a pagar es:",total_a_pagar)

else:
   print("No hay recargos:",total_a_pagar)


# Se imprime la factura al cliente
print("""Factura:
      Nombre""",Nombre,
      """Apellido:""",Apellido,"""
      Vehiculo:""",modelo_deseado,"""
      tarifa:""",consultar_tarifa(),"""
      seguros: CNdS y seguro especial
      Período de alquiler:""",consultar_mes_de_alquiler()
      ,"""Recargos por temporada y zona
      Descuento VIP: Aplicado""")



#Se ingresa el monto a pagar
print("Usted debe pagar:",total_a_pagar)
pago=False
while pago ==False:
        print(input("Ingrese su pago:"))
        pago_ingresado=input()
        if pago_ingresado<total_a_pagar:
                deuda=total_a_pagar-pago_ingresado
                print("Usted adeuda:",deuda)
        elif pago_ingresado==total_a_pagar:
                print("Pago realizado exitosamente!")
                pago==True
        else:
                print("No se aceptan montos mayores al requerido")
                pago==True



