import random

#USUARIO

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
        return True

#TARJETA

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















