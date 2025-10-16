

#USUARIO
def ingresarNombre (texto,nummin,nummax): 
    while True:
        try : 
            nombre = input(texto).strip
            
            if len(nombre) < nummin or len(nombre)>nummax : 
                raise ValueError

            break
        except ValueError: 
            print(f'Ingreso erroneo! Tu nombre debe tener mas de {nummin} y menos que {nummax} ')

    return nombre 

def ingresarContraseña (texto,min, max): 
    while True:
        try: 

            contraseña = input(texto) 
            if (len(contraseña) < max) or (len(contraseña > min)): 
                raise ValueError
            break
        
        except ValueError: 
            print(f'Ingreso erroneo!, la contraseña debe tener entre {min} y {max}   caracteres')
    return contraseña

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
















