#USUARIO

import random

def ingresarNombre(texto, minimo, maximo):
    while True:
        try:
            nombre = input(texto).strip()
            if not nombre:
                raise ValueError
            if len(nombre) < minimo or len(nombre) > maximo:
                raise ValueError
            break
        except ValueError:
            print(f'Ingreso erróneo. Tu nombre debe tener entre {minimo} y {maximo} caracteres.')
    return nombre

def ingresarContraseña (texto,minimo,maximo): 
    while True:
        try: 

            contraseña = input(texto) 
            if (len(contraseña) < int(max)) or (len(contraseña > int(min))): 
                raise ValueError
            break
        
        except ValueError: 
            print(f'Ingreso erroneo!, la contraseña debe tener entre {min} y {max}   caracteres')
    return contraseña

def crearCuenta (): 
    try:
        archivoUsuario = open("Usuario, wt")
    except IOError:
        print("algo salio mal, no se pudo crear su cuenta")
    else:            
        nombre =ingresarNombre ("ingrese su nombre de usuario", "4", "12")
        contraseña =ingresarContraseña ("ingrese su contraseña", "4", "12")
        saldo = "0"
        archivoUsuario.write(str(nombre) + ";" + str(contraseña) + ";", + saldo + "\n")
    return

#TARJETA

def tipoTarjeta (): 
    
    tipoTarjetas = ["VISA","MASTERCARD","AMEX"]
    
    while True: 
        try: 
            print("Elija el tipo de tarjeta!")
            for i in range (3):
                print(i+1,tipoTarjetas[i])
            
            tarjeta = int(input("Ingrese el numero del 1 al 3: "))
            
            if tarjeta < 1 or tarjeta > 3 :
                raise ValueError
            
            break 
            
            
        except ValueError:
            print("El valor esta dentro de los parametros permitidos")
    
    return tipoTarjeta

def validarCodigo(minimo, maximo ,diccTarjetas):
    while true:
        try:
            codigo = input("Ingrese codigo de tarjeta: ")
            if codigo.isdigit() == False:
                raise ValueError
            if codigo in diccTarjeta:
                
            break

        except ValueError as mensaje:
            print(mensaje)
        
        except:
            print("Error")













