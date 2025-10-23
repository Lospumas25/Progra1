import random
from datetime import datetime

""" FALTA LAMBDA / LISTA COMPRENSION / SLICING / RANDOM / DICCIONARIOS / RECURSIVIDAD """
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
def leerUsuario():


def escribirUsuario():

    
def ingresarNombre(texto,minimo,maximo):
    while True:
        try:
            nombre = input(texto).strip()
            if not nombre:
                raise ValueError
            if len(nombre) < minimo or len(nombre) > maximo:
                raise ValueError
            break
        except ValueError:
            print(f"Ingreso erroneo: Tu nombre debe tener entre {minimo} y {maximo} caracteres.")
    return nombre

def ingresarContraseña(texto,minimo,maximo):
    while True:
        try:
            contraseña = input(texto)
            if len(contraseña) < minimo or len(contraseña) > maximo:
                raise ValueError
            break
        except ValueError:
            print(f'Ingreso erroneo: la contraseña debe tener entre {minimo} y {maximo} caracteres.')
    return contraseña

def crearCuenta():
    try:
        archivoUsuario = open("Usuario.txt", "wt")
    except OSError:
        print("Algo salio mal, no se pudo crear su cuenta.")
        return False
    else:
        nombre = ingresarNombre("Ingrese su nombre de usuario: ", 4, 12)
        contraseña = ingresarContraseña("Ingrese su contraseña: ", 4, 12)
        saldo = "0"
        archivoUsuario.write(str(nombre) + ";" + str(contraseña) + ";", + saldo + "\n")
        archivoUsuario.close()
        Log("Crea Cuenta")
        return True

def login ():                    #DEVUELVE UN TRUE SI EL USUARIO Y CONTRASEÑA SON CORRECTOS, UN FALSE SI NO LO SON
    nombreUsuario = ingresarNombre ("ingrese su nombre de usuario, el usuario debe tener entre 4 y 12 caracteres", 4, 12)
    contraseñaUsuario = ingresarContraseña ("ingrese su contraseña, la contraseña debe tener entre 4 y 12 caracteres", 4, 12)
    try:
       archivo = open ("Usuario.txt", "rt")
    except IOError:
        print ("error, no existen usuarios registrados")
    linea = archivo.readline ()
    linea = linea.strip("\n")
    nombreRegistrado, contraseñaRegistrada = linea.split(";")
    if (nombreRegistrado == nombreUsuario) and (contraseñaRegistrada == contraseñaUsuario):
        aux = True
    else:
        aux = False
    return aux 


def modificarContraseña():
    try:
        archivoUsuario = open("Usuario.txt", "rt")
    except OSError:
        print("Algo salio mal, no se pudo crear su cuenta.")
        return False
    else:
        linea = archivoUsuario.readline()
        linea = linea.strip("\n")
        nombre,contraseña,saldo = linea.split(";")
        contraseña = ingresarContraseña("Ingrese su contraseña: ", 4, 12)
        archivoUsuario.close()

    try:
        archivoUsuario = open("Usuario.txt", "wt")
    except OSError:
        print("Algo salio mal, no se pudo crear su cuenta.")
        return False
    else:
        archivoUsuario.write(str(nombre) + ";" + str(contraseña) + ";", + saldo + "\n")
        archivoUsuario.close()
        
        
#---------------------------------------------------------------TARJETA---------------------------------------------------------------------
def leerTarjetas():

def escribirTarjetas():

def tipoTarjeta():
    tipoTarjetas = ["VISA", "MASTERCARD", "AMEX"]
    while True:
        try:
            print("Elija el tipo de tarjeta")
            for i in range(len(tipoTarjetas)):
                print(i + 1, tipoTarjetas[i])
            tarjeta = int(input(f"Ingrese el número del 1 al {len(tipoTarjetas)}: "))
            if tarjeta < 1 or tarjeta > len(tipoTarjetas):
                raise ValueError("Opción fuera de rango.")
            break
        except ValueError as e:
            print("Entrada inválida.", e)
    return tipoTarjetas[tarjeta - 1]

def agregarTarjeta():
    

def verTarjetas():


def eliminarTarjeta():


def validarCodigo(minimo, maximo, diccTarjetas):
    while True:
        try:
            codigo = input("Ingrese codigo de tarjeta: ").strip()
            if not codigo.isdigit():
                raise ValueError("El codigo debe contener solo digitos")
            if not (minimo <= len(codigo) <= maximo):
                raise ValueError(f"El codigo debe tener entre {minimo} y {maximo} digitos")
            if codigo in diccTarjetas:
                raise ValueError("El código ya existe. Ingrese uno distinto")
            break
        except ValueError as mensaje:
            print(mensaje)
        except:
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
                raise ValueError("Opción fuera de rango.")
            break
        except ValueError as e:
            print("Entrada inválida.", e)
    return servicios[opcion - 1]

#---------------------------------------------------------------MOVIMIENTOS---------------------------------------------------------------

def registrarMovimientos():

def pagarServicio():

def ingresarDinero():

def transferir():


#---------------------------------------------------------------REPORTES------------------------------------------------------------------

def mostrarReportes():






















