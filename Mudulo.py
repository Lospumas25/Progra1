import random
from datetime import datetime

""" FALTA LAMBDA / LISTA COMPRENSION / SLICING  DICCIONARIOS / RECURSIVIDAD """
#---------------------------------------------------------------LOG--------------------------------------------------------------------------

def Log(texto):
    
    time = datetime.now()
    
    try: 
        archivoLog = open("ArchivoLog.txt", "at")
        archivoLog.write(str(time) + ";" + texto + "\n")
        archivoLog.close()
    except OSError:
        print("El archivo no se abrio correctamente")

#---------------------------------------------------------------USUARIO----------------------------------------------------------------------
def leerUsuario():  #para leer usuario del archivo
    return

def escribirUsuario(): #para guardar el usuario en el archivo

    return

def ingresarNombre(texto,minimo,maximo):
    while True:
        try:
            nombre = input(texto).strip()
            if not nombre:
                Log("Error ingreso de nombre vacio")
                raise ValueError
            if len(nombre) < minimo or len(nombre) > maximo:
                Log("Error ingreso de nombre no cumple con la longitud requerida")
                raise ValueError
            Log("Ingreso de nombre exitoso")
            break
        except ValueError:
            print(f"Ingreso erroneo: Tu nombre debe tener entre {minimo} y {maximo} caracteres.")
    return nombre

def ingresarContraseña(texto,minimo,maximo):
    while True:
        try:
            contraseña = input(texto)
            if len(contraseña) < minimo or len(contraseña) > maximo:
                Log("Error ingreso de contraseña no cumple con la longitud requerida")
                raise ValueError
            Log("Ingreso de contraseña exitoso")
            break
        except ValueError:
            print(f'Ingreso erroneo: la contraseña debe tener entre {minimo} y {maximo} caracteres.')
    return contraseña

def crearCuenta():
    try:
        archivoUsuario = open("Usuario.txt", "wt")
    except OSError:
        print("Algo salio mal, no se pudo crear su cuenta.")
        Log("Error al crear Archivo Usuario")
        return False
    else:
        nombre = ingresarNombre("Ingrese su nombre de usuario: ", 4, 12)
        contraseña = ingresarContraseña("Ingrese su contraseña: ", 4, 12)
        saldo = "0"
        archivoUsuario.write(str(nombre) + ";" + str(contraseña) + ";", + saldo + "\n")
        archivoUsuario.close()
        Log("Cuenta creada exitosamente")
        return True


def verificarExistenciaUsuario (): #verifica la existencia del archivo Usuario
    try:
        arch = open ("Usuario.txt", "rt")
    except IOError:
        Log ("fallo al abrir el archivo")
        existe = False
    else: existe = True
    return existe



def login ():                    #DEVUELVE UN TRUE SI EL USUARIO Y CONTRASEÑA SON CORRECTOS, UN FALSE SI NO LO SON
    nombreUsuario = ingresarNombre ("ingrese su nombre de usuario, el usuario debe tener entre 4 y 12 caracteres", 4, 12)
    contraseñaUsuario = ingresarContraseña ("ingrese su contraseña, la contraseña debe tener entre 4 y 12 caracteres", 4, 12)
    try:
        archivo = open ("Usuario.txt", "rt")
    except IOError:
        print ("error, no existen usuarios registrados")
        Log("Error credenciales usuario no existentes")
    linea = archivo.readline ()
    linea = linea.strip("\n")
    nombreRegistrado, contraseñaRegistrada = linea.split(";")
    if (nombreRegistrado == nombreUsuario) and (contraseñaRegistrada == contraseñaUsuario):
        aux = True
    else:
        aux = False
    return aux 

def loopLogin ():  #LA MAIN EMPIEZA LLAMANDO ESTO DESPUES DE VERIFICAR QUE EXISTA USUARIO
    while True:
        correcto = login ()
        if correcto == True:
            break
            
def modificarContraseña():
    try:
        archivoUsuario = open("Usuario.txt", "rt")
    except OSError:
        print("Algo salio mal, no se pudo crear su cuenta.")
        Log("Error al abrir Archivo Usuario para modificar contraseña")
        return False
    else:
        linea = archivoUsuario.readline()
        linea = linea.strip("\n")
        nombre,contraseña,saldo = linea.split(";")
        contraseña = ingresarContraseña("Ingrese su contraseña: ", 4, 12)
        archivoUsuario.close()
        Log("Contraseña modificada exitosamente")

    try:
        archivoUsuario = open("Usuario.txt", "wt")
    except OSError:
        print("Algo salio mal, no se pudo crear su cuenta.")
        Log("Error al abrir Archivo Usuario para guardar nueva contraseña")
        return False
    else:
        archivoUsuario.write(str(nombre) + ";" + str(contraseña) + ";", + saldo + "\n")
        archivoUsuario.close()
        Log("Nueva contraseña guardada exitosamente")
        
        
#---------------------------------------------------------------TARJETA---------------------------------------------------------------------
def leerTarjetas():
    return
def escribirTarjetas():
    return
def tipoTarjeta():
    tipoTarjetas = ["VISA", "MASTERCARD", "AMEX"]
    while True:
        try:
            print("Elija el tipo de tarjeta")
            for i in range(len(tipoTarjetas)):
                print(i + 1, tipoTarjetas[i])
            tarjeta = int(input(f"Ingrese el número del 1 al {len(tipoTarjetas)}: "))

            if tarjeta < 1 or tarjeta > len(tipoTarjetas):
                Log("Error ingreso tipo de tarjeta fuera de rango")
                raise ValueError("Opción fuera de rango.")
            Log("Ingreso tipo de tarjeta exitoso")
            break
        
        except ValueError as e:
            print("Entrada inválida.", e)
    return tipoTarjetas[tarjeta - 1]

def agregarTarjeta():
    return

def verTarjetas():
    return

def eliminarTarjeta():
    return

def validarCodigo(minimo, maximo, diccTarjetas):
    while True:
        try:
            codigo = input("Ingrese codigo de tarjeta: ").strip()
            if not codigo.isdigit():
                Log("Error ingreso codigo de tarjeta con caracteres no numericos")
                raise ValueError("El codigo debe contener solo digitos")

            if not (minimo <= len(codigo) <= maximo):
                Log("Error ingreso codigo de tarjeta no cumple con la longitud requerida")
                raise ValueError(f"El codigo debe tener entre {minimo} y {maximo} digitos")
            
            if codigo in diccTarjetas:
                Log("Error ingreso codigo de tarjeta ya existente")
                raise ValueError("El código ya existe. Ingrese uno distinto")
            break
        except ValueError as mensaje:
            print(mensaje)
        except: #por que dos execept?ajasj
            print("Error inesperado")
    return codigo


#---------------------------------------------------------------SERVICIOS-----------------------------------------------------------------
def tipoServicio():
    servicios = ["Agua", "Gas", "Luz"]
    while True:
        try:
            for i in range(len(servicios)):
                print(i + 1, f"Pagar {servicios[i]}")
            opcion = int(input(f"Ingrese el número del 1 al {len(servicios)}: "))

            if opcion < 1 or opcion > len(servicios):
                Log("Error ingreso tipo de servicio fuera de rango")
                raise ValueError("Opción fuera de rango.")
            Log("Ingreso tipo de servicio exitoso")
            break
        except ValueError as e:
            print("Entrada inválida.", e)
    return servicios[opcion - 1]

#---------------------------------------------------------------MOVIMIENTOS---------------------------------------------------------------

def registrarMovimientos():
    return
def pagarServicio():
    Log("Ingreso a pagar servicio")
    servicios = ["Agua", "Gas", "Luz"]
    valores = [random.randint(1000,40000) for i in range(3)]
    while True: 
        try: 
            print("Seleccione el servicio a pagar:")
            for i in range(len(servicios)):
                print(i + 1, servicios[i])

            opcion = int(input(f"Ingrese el número del 1 al {len(servicios)}: "))

            if opcion < 1 or opcion > len(servicios):
                Log("Error ingreso tipo de servicio fuera de rango")
                raise ValueError("Opción fuera de rango.")

            print(f"Ha seleccionado pagar el servicio de {servicios[opcion - 1]}.")
            Log(f'ingreso a pagar servicio {servicios[opcion - 1]}')
            print("Debe pagar un monto de: ", valores[opcion - 1])

            monto = float(input("Ingrese el monto que desea pagar: "))
            if monto < 0 or monto > valores[opcion - 1]:
                Log("Error ingreso monto a pagar fuera de rango")
                raise ValueError("El monto ingresado es inválido.")
            
            restante = valores[opcion - 1] - monto
            print(f"Pago realizado. Monto restante a pagar: {restante}")
            Log(f'Monto: {monto} de servicio: {servicios[opcion - 1]} pagado exitosamente')
            
            break
        except ValueError as e:
            Log("Error en el proceso de pago de servicio")
            print("Entrada inválida.", e)


def ingresarDinero():
    return
def transferir():
    return

#---------------------------------------------------------------REPORTES------------------------------------------------------------------

def mostrarReportes():
    return


def calcularPlazoFijo (saldo, meses): #NECESITAMOS RECURSIVIDAD EN ESTA VIDA
    extra = saldo * 0.05
    if meses == 0:
        return extra
    return calcularPlazoFijo (saldo + extra, meses -1)





