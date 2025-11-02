import random
from datetime import datetime

#---------------------------------------------------------------LOG-------------------------------------------------------------

def Log(texto):
    tiempo = datetime.now().isoformat()
    try:
        with open("ArchivoLog.txt", "at") as archivoLog:
            archivoLog.write(f"{tiempo};{texto}\n")
    except OSError:
        print("El archivo no se abrio correctamente")

#---------------------------------------------------------------USUARIO---------------------------------------------------------
def leerUsuario():
    try:
        with open("Usuario.txt", "rt") as archivoUsuario:
            linea = archivoUsuario.readline().strip()
    except OSError:
        Log("Error al leer Archivo Usuario")

    if not linea:
        Log("Archivo Usuario vacio")

    try:
        nombre, contraseña, saldo = linea.split(";")
        saldo = float(saldo)
    except ValueError:
        Log("Formato incorrecto en Archivo Usuario")

    return {"nombre": nombre, "contraseña": contraseña, "saldo": saldo}


def escribirUsuario(usuario):
    exito = False
    if not usuario:
        return exito
    try:
        with open("Usuario.txt", "wt") as archivoUsuario:
            archivoUsuario.write(f"{usuario['nombre']};{usuario['contraseña']};{usuario['saldo']:.2f}\n")
        Log("Datos de usuario guardados")
        exito = True
    except OSError:
        Log("Error al escribir Archivo Usuario")
        print("No se pudo guardar la información del usuario.")
    return exito
    

def ingresarNombre(texto, minimo, maximo):
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


def ingresarContraseña(texto, minimo, maximo):
    while True:
        try:
            contraseña = input(texto).strip()
            if len(contraseña) < minimo or len(contraseña) > maximo:
                Log("Error ingreso de contraseña no cumple con la longitud requerida")
                raise ValueError
            Log("Ingreso de contraseña exitoso")
            break
        except ValueError:
            print(f'Ingreso erroneo: la contraseña debe tener entre {minimo} y {maximo} caracteres.')
    return contraseña


def crearCuenta():
    creada = False
    nombre = ingresarNombre("Ingrese su nombre de usuario: ", 4, 12)
    contraseña = ingresarContraseña("Ingrese su contraseña: ", 4, 12)
    usuario = {"nombre": nombre, "contraseña": contraseña, "saldo": 0.0}

    if escribirUsuario(usuario):
        Log("Cuenta creada exitosamente")
        print("Cuenta creada exitosamente. Ya puede iniciar sesión.")
        creada = True
    else:
        Log("Error al crear cuenta")

    return creada


def verificarExistenciaUsuario():
    try:
        with open("Usuario.txt", "rt"):
            pass
    except IOError:
        Log("Fallo al abrir el archivo de usuario")
        return False
    return True


def login():
    logueado = False
    usuario_registrado = leerUsuario()
    if not usuario_registrado:
        print("No existen usuarios registrados. Cree una cuenta primero.")
        Log("Error credenciales usuario no existentes")
        return logueado

    nombreUsuario = ingresarNombre("Ingrese su nombre de usuario (4 a 12 caracteres): ", 4, 12)
    contraseñaUsuario = ingresarContraseña("Ingrese su contraseña (4 a 12 caracteres): ", 4, 12)

    if (usuario_registrado["nombre"] == nombreUsuario) and (usuario_registrado["contraseña"] == contraseñaUsuario):
        Log("Login exitoso")
        logueado = True
    else:
        Log("Login fallido - credenciales incorrectas")
        print("Usuario o contraseña incorrectos.")

    return logueado



def loopLogin():
    while True:
        if login():
            menuPrincipal()
            break


def mostrarSaldo(usuario):
    print(f"Saldo actual: ${usuario['saldo']:.2f}")
    Log("Consulta de saldo")


def modificarContraseña():
    modificada = False

    usuario = leerUsuario()
    if not usuario:
        print("No hay usuario registrado.")
        Log("Intento de modificación sin usuario registrado")
    else:
        contraseña_actual = ingresarContraseña("Ingrese su contraseña actual: ", 4, 12)
        if contraseña_actual != usuario["contraseña"]:
            print("La contraseña actual no es correcta.")
            Log("Intento fallido de cambio de contraseña")
        else:
            nueva_contraseña = ingresarContraseña("Ingrese su nueva contraseña: ", 4, 12)
            usuario["contraseña"] = nueva_contraseña

            if escribirUsuario(usuario):
                Log("Contraseña modificada exitosamente")
                print("Contraseña actualizada correctamente.")
                modificada = True
            else:
                Log("Error al intentar actualizar contraseña")
                print("No se pudo actualizar la contraseña.")

    return modificada


#---------------------------------------------------------------TARJETA---------------------------------------------------------

def leerTarjetas():
    tarjetas = {}
    try:
        with open("Tarjetas.txt", "rt") as archivoTarjetas:
            for linea in archivoTarjetas:
                linea = linea.strip()
                if not linea:
                    continue
                try:
                    codigo, tipo, numero, titular, vencimiento = linea.split(";")
                except ValueError:
                    Log("Formato incorrecto en Archivo Tarjetas")
                    continue
                tarjetas[codigo] = {
                    "tipo": tipo,
                    "numero": numero,
                    "titular": titular,
                    "vencimiento": vencimiento,
                }
    except FileNotFoundError:
        Log("Archivo Tarjetas inexistente, se creara al guardar")
    except OSError:
        Log("Error al leer Archivo Tarjetas")
    return tarjetas


def escribirTarjetas(tarjetas):
    guardadas = False
    try:
        with open("Tarjetas.txt", "wt") as archivoTarjetas:
            for codigo, datos in tarjetas.items():
                archivoTarjetas.write(
                    f"{codigo};{datos['tipo']};{datos['numero']};{datos['titular']};{datos['vencimiento']}\n")
        Log("Tarjetas guardadas correctamente")
        guardadas = True
    except OSError:
        Log("Error al escribir Archivo Tarjetas")
        print("No se pudieron guardar las tarjetas.")
    return guardadas



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
        except Exception:
            print("Error inesperado")
    return codigo


def agregarTarjeta():
    tarjetas = leerTarjetas()
    codigo = validarCodigo(4, 8, tarjetas)
    tipo = tipoTarjeta()
    while True:
        numero = input("Ingrese el número de tarjeta (16 dígitos): ").replace(" ", "")
        if numero.isdigit() and len(numero) == 16:
            break
        print("El número de tarjeta debe tener 16 dígitos.")
    titular = ingresarNombre("Ingrese el nombre del titular: ", 3, 30)
    while True:
        vencimiento = input("Ingrese la fecha de vencimiento (MM/AA): ").strip()
        if len(vencimiento) == 5 and vencimiento[2] == "/" and vencimiento.replace("/", "").isdigit():
            mes, año = vencimiento.split("/")
            if 1 <= int(mes) <= 12:
                break
            else:
                print("Mes inválido en la fecha de vencimiento.")
        else:
            print("Formato inválido. Use MM/AA.")
    tarjetas[codigo] = {
        "tipo": tipo,
        "numero": numero,
        "titular": titular,
        "vencimiento": vencimiento,
    }
    if escribirTarjetas(tarjetas):
        Log(f"Tarjeta {codigo} agregada")
        print("Tarjeta agregada correctamente.")



def verTarjetas():
    mostradas = False 
    tarjetas = leerTarjetas()
    if not tarjetas:
        print("No hay tarjetas registradas.")
        Log("Intento de visualizar tarjetas sin registros")
    else:
        tarjetas_ordenadas = sorted(
            tarjetas.items(),
            key=lambda item: item[1]["tipo"] )   # LAMBDA

        for codigo, datos in tarjetas_ordenadas:
            numero_visible = f"**** **** **** {datos['numero'][-4:]}"
            print(
                f"Código: {codigo} - Tipo: {datos['tipo']} - Número: {numero_visible} - "
                f"Titular: {datos['titular']} - Vencimiento: {datos['vencimiento']}")
        Log("Visualización de tarjetas")
        mostradas = True

    return mostradas


def eliminarTarjeta():
    tarjetas = leerTarjetas()
    if not tarjetas:
        print("No hay tarjetas para eliminar.")
        return

    codigo = input("Ingrese el código de la tarjeta a eliminar: ").strip()
    if codigo not in tarjetas:
        print("No existe una tarjeta con ese código.")
        Log("Intento fallido de eliminar tarjeta")
        return

    tarjetas.pop(codigo)
    if escribirTarjetas(tarjetas):
        Log(f"Tarjeta {codigo} eliminada")
        print("Tarjeta eliminada correctamente.")


def menuTarjetas():
    while True:
        print("\n--- Gestión de tarjetas ---")
        print("1. Ver tarjetas")
        print("2. Agregar tarjeta")
        print("3. Eliminar tarjeta")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            verTarjetas()
        elif opcion == "2":
            agregarTarjeta()
        elif opcion == "3":
            eliminarTarjeta()
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

#---------------------------------------------------------------SERVICIOS-------------------------------------------------------

def pagarServicio():
    pagado = False 
    usuario = leerUsuario()
    if not usuario:
        print("No hay usuario registrado.")
        Log("Intento de pagar servicio sin usuario")
    else:
        Log("Ingreso a pagar servicio")
        servicios = {nombre: random.randint(1000, 40000) for nombre in ("Agua", "Gas", "Luz")}
        nombres_servicio = list(servicios.keys())

        while True:
            try:
                print("Seleccione el servicio a pagar:")
                for indice, nombre in enumerate(nombres_servicio, start=1):
                    print(f"{indice}. {nombre} - Total adeudado: ${servicios[nombre]}")
                opcion = int(input(f"Ingrese el número del 1 al {len(nombres_servicio)}: "))
                if opcion < 1 or opcion > len(nombres_servicio):
                    Log("Error ingreso tipo de servicio fuera de rango")
                    raise ValueError("Opción fuera de rango.")
                servicio_elegido = nombres_servicio[opcion - 1]
                monto_pendiente = servicios[servicio_elegido]
                break
            except ValueError as e:
                print("Entrada inválida.", e)

        while True:
            try:
                monto = float(input("Ingrese el monto que desea pagar: "))
                if monto <= 0 or monto > monto_pendiente:
                    Log("Error ingreso monto a pagar fuera de rango")
                    raise ValueError("El monto ingresado es inválido.")
                if monto > usuario["saldo"]:
                    Log("Error saldo insuficiente para pagar servicio")
                    raise ValueError("Saldo insuficiente.")
                break
            except ValueError as e:
                print("Entrada inválida.", e)

        usuario["saldo"] -= monto
        escribirUsuario(usuario)
        registrarMovimientos(f"Pago de {servicio_elegido}", -monto, usuario["saldo"])
        restante = monto_pendiente - monto
        print(f"Pago realizado. Monto restante a pagar de {servicio_elegido}: {restante}")
        Log(f"Monto: {monto} de servicio: {servicio_elegido} pagado exitosamente")
        pagado = True

    return pagado


#---------------------------------------------------------------MOVIMIENTOS-----------------------------------------------------

def registrarMovimientos(descripcion, monto, saldo_final):
    registro = f"{datetime.now().isoformat()};{descripcion};{monto:.2f};{saldo_final:.2f}"
    try:
        with open("Movimientos.txt", "at") as archivoMovimientos:
            archivoMovimientos.write(registro + "\n")
    except OSError:
        Log("Error al escribir Archivo Movimientos")


def obtenerMovimientos():
    movimientos = []
    try:
        with open("Movimientos.txt", "rt") as archivoMovimientos:
            for linea in archivoMovimientos:
                linea = linea.strip()
                if not linea:
                    continue
                partes = linea.split(";")
                if len(partes) != 4:
                    continue
                fecha, descripcion, monto, saldo = partes
                try:
                    movimientos.append(
                        {
                            "fecha": fecha,
                            "descripcion": descripcion,
                            "monto": float(monto),
                            "saldo": float(saldo),
                        }
                    )
                except ValueError:
                    continue
    except FileNotFoundError:
        Log("Archivo Movimientos inexistente")
    except OSError:
        Log("Error al leer Archivo Movimientos")
    return movimientos


def ingresarDinero():
    ingresado = False

    usuario = leerUsuario()
    if not usuario:
        print("No hay usuario registrado.")
        Log("Intento de ingresar dinero sin usuario registrado")
    else:
        while True:
            try:
                monto = float(input("Ingrese el monto a acreditar: "))
                if monto <= 0:
                    raise ValueError("El monto debe ser mayor a cero.")
                break
            except ValueError as e:
                print("Entrada inválida.", e)
        usuario["saldo"] += monto
        if escribirUsuario(usuario):
            registrarMovimientos("Ingreso de dinero", monto, usuario["saldo"])
            print(f"Ingreso registrado. Nuevo saldo: ${usuario['saldo']:.2f}")
            Log(f"Ingreso de dinero por ${monto:.2f}")
            ingresado = True
        else:
            Log("Error al intentar registrar ingreso de dinero")
            print("No se pudo guardar el ingreso.")
    return ingresado



def transferir():
    transferida = False
    usuario = leerUsuario()
    if not usuario:
        print("No hay usuario registrado.")
        Log("Intento de transferencia sin usuario registrado")
    else:
        destinatario = ingresarNombre("Ingrese el alias del destinatario: ", 3, 20)

        while True:
            try:
                monto = float(input("Ingrese el monto a transferir: "))
                if monto <= 0:
                    raise ValueError("El monto debe ser mayor a cero.")
                if monto > usuario["saldo"]:
                    raise ValueError("Saldo insuficiente.")
                break
            except ValueError as e:
                print("Entrada inválida.", e)

        usuario["saldo"] -= monto
        if escribirUsuario(usuario):
            registrarMovimientos(f"Transferencia a {destinatario}", -monto, usuario["saldo"])
            print(f"Transferencia realizada. Nuevo saldo: ${usuario['saldo']:.2f}")
            Log(f"Transferencia realizada a {destinatario} por ${monto:.2f}")
            transferida = True
        else:
            Log("Error al intentar guardar transferencia")
            print("No se pudo completar la transferencia.")

    return transferida


#---------------------------------------------------------------REPORTES--------------------------------------------------------

def mostrarReportes():
    mostrado = False

    movimientos = obtenerMovimientos()
    if not movimientos:
        print("No hay movimientos registrados.")
        Log("Intento de visualizar reportes sin movimientos")
    else:
        movimientos_ordenados = sorted(movimientos, key=lambda mov: mov["fecha"])
        print("\n--- Últimos movimientos ---")
        for movimiento in movimientos_ordenados[-5:]:
            print(
                f"{movimiento['fecha']} - {movimiento['descripcion']} - "
                f"${movimiento['monto']:.2f} - Saldo: ${movimiento['saldo']:.2f}")
        saldo_promedio = sum(mov["saldo"] for mov in movimientos_ordenados) / len(movimientos_ordenados)
        ingresos = sum(mov["monto"] for mov in movimientos_ordenados if mov["monto"] > 0)
        egresos = sum(-mov["monto"] for mov in movimientos_ordenados if mov["monto"] < 0)

        print("\n--- Resumen ---")
        print(f"Saldo promedio: ${saldo_promedio:.2f}")
        print(f"Total de ingresos: ${ingresos:.2f}")
        print(f"Total de egresos: ${egresos:.2f}")

        ingresos_registrados = [mov["monto"] for mov in movimientos_ordenados if mov["monto"] > 0]
        egresos_registrados = [mov["monto"] for mov in movimientos_ordenados if mov["monto"] < 0]

        if ingresos_registrados:
            mayor_ingreso = max(ingresos_registrados)
            menor_ingreso = min(ingresos_registrados)
            promedio_ingresos = sum(ingresos_registrados) / len(ingresos_registrados)
            print("\n--- Detalle de ingresos ---")
            print(f"Ingreso más alto: ${mayor_ingreso:.2f}")
            print(f"Ingreso más bajo: ${menor_ingreso:.2f}")
            print(f"Promedio de ingresos: ${promedio_ingresos:.2f}")

        if egresos_registrados:
            egresos_absolutos = [abs(mov) for mov in egresos_registrados]
            mayor_egreso = max(egresos_absolutos)
            menor_egreso = min(egresos_absolutos)
            promedio_egresos = sum(egresos_absolutos) / len(egresos_absolutos)
            print("\n--- Detalle de egresos ---")
            print(f"Egreso más alto: ${mayor_egreso:.2f}")
            print(f"Egreso más bajo: ${menor_egreso:.2f}")
            print(f"Promedio de egresos: ${promedio_egresos:.2f}")

        total_movimientos = ingresos + egresos
        if total_movimientos > 0:
            porcentaje_ingresos = (ingresos / total_movimientos) * 100
            porcentaje_egresos = (egresos / total_movimientos) * 100
            print("\n--- Porcentajes ---")
            print(f"Ingresos: {porcentaje_ingresos:.2f}% del total de movimientos")
            print(f"Egresos: {porcentaje_egresos:.2f}% del total de movimientos")

        Log("Visualización de reportes")
        mostrado = True

    return mostrado

def calcularPlazoFijo(saldo, meses): #RECURSIVA
    if meses == 0:
        return saldo
    return calcularPlazoFijo(saldo * 1.05, meses - 1)


def simularPlazoFijo():
    simulado = False
    usuario = leerUsuario()
    if not usuario:
        print("No hay usuario registrado.")
        Log("Intento de simulación de plazo fijo sin usuario registrado")
    else:
        while True:
            try:
                meses = int(input("Ingrese la cantidad de meses a simular: "))
                if meses < 0:
                    raise ValueError("La cantidad de meses debe ser mayor o igual a cero.")
                break
            except ValueError as e:
                print("Entrada inválida.", e)

        capital_final = calcularPlazoFijo(usuario["saldo"], meses)
        ganancia = capital_final - usuario["saldo"]

        print(f"\n--- Simulación de Plazo Fijo ---")
        print(f"Capital actual: ${usuario['saldo']:.2f}")
        print(f"Capital estimado luego de {meses} meses: ${capital_final:.2f}")
        print(f"Ganancia estimada: ${ganancia:.2f}")

        Log(f"Simulación de plazo fijo por {meses} meses realizada correctamente")
        simulado = True

    return simulado



def menuPrincipal():
    activo = True

    while activo:
        usuario = leerUsuario()
        if not usuario:
            print("No se pudo obtener la información del usuario.")
            Log("Error al obtener información del usuario en el menú principal")
            break

        print("\n--- Menú Principal ---")
        print("1. Consultar saldo")
        print("2. Ingresar dinero")
        print("3. Transferir")
        print("4. Pagar servicio")
        print("5. Gestionar tarjetas")
        print("6. Cambiar contraseña")
        print("7. Ver reportes")
        print("8. Simular plazo fijo")
        print("9. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            mostrarSaldo(usuario)
        elif opcion == "2":
            ingresarDinero()
        elif opcion == "3":
            transferir()
        elif opcion == "4":
            pagarServicio()
        elif opcion == "5":
            menuTarjetas()
        elif opcion == "6":
            modificarContraseña()
        elif opcion == "7":
            mostrarReportes()
        elif opcion == "8":
            simularPlazoFijo()
        elif opcion == "9":
            Log("Cierre de sesión")
            print("Hasta luego!")
            activo = False
        else:
            print("Opción inválida. Intente nuevamente.")
            Log(f"Opción inválida ingresada: {opcion}")
    return activo



def iniciarAplicacion():
    if not verificarExistenciaUsuario():
        crearCuenta()
    loopLogin()
