UNIVERSIDAD ARGENTINA DE LA EMPRESA (UADE)

KIWILLET
Billetera virtual – Proyecto de Programación I


Carrera: Ingeniería en Informática

Materia: Programación I / Algoritmos y Estructura de Datos I

Profesor/a: Ing. María Eugenia Varando

Turno: Noche – 2° Cuatrimestre 2025





Integrantes
• Massun, Felipe / 
• Scala Merani, Damián / 1139436
• Arias Castroman, Santiago / 1224594


Descripción general del proyecto:

Kiwillet busca simular el funcionamiento básico de una billetera virtual, pero ejecutada de forma local, todos los datos y registros se manejan en archivos de texto. El programa permite a un único usuario crear su cuenta, iniciar sesión, administrar sus tarjetas, realizar pagos de servicios, efectuar transferencias, ingresar dinero y consultar su saldo.
Objetivos:
Kiwillet tiene como objetivo hacer una billetera virtual que permita al usuario gestionar sus finanzas de forma simple y rápida.
Los objetivos del programa son:
Que el usuario pueda visualizar su saldo, registrar ingresos y egresos, y realizar pagos de servicios.
Mostrar las tarjetas registradas por el usuario además de poder dar el alta y  baja de cada tarjeta.
Sistema de pagos de servicios.
Registrar la actividad del usuario en archivos locales.
Seguridad de los datos del usuario, mediante contraseñas, validaciones de ingreso y control de errores en tiempo de ejecución.
Mostrar informes que permitan al usuario conocer el saldo, pagos realizados y movimientos en la cuenta.
Alcance funcional del sistema:

Archivos de entrada: 
User DICCIONARIO: 
nombre de usuario
password
Saldo disponible

Tarjetas DICCIONARIO 
CódigoTarjeta/ID
Fecha caducidad
Nombre de titular
código de seguridad

Tipos de tarjetas (Diccionario)
nombre de usuario/ID
CódigoTarjeta/ID

Servicios (Diccionarios)
Código de servicio  
Nombre de servicio


Archivos de salida 

-Bitácora (Log) Almacena todos los inputs con fecha y hora

Pagos Diccionario
Gastos Diccionario
Estadística de saldo por dia (resumen al final del mes)
lista de saldo por dia


Menu
0 El Login
1 modificar usuario 
2 pago de servicios
3 ver tarjetas 
4 transferencias 
5 ingresar dinero 
6 salir


1-LOGIN
1.1-Crear usuario
1.3-Loguearse

2- MENU PRINCIPAL

2.1- Tarjetas
	2.1.1- ver tarjetas
2.1.1.1- muestra de tarjetas (muestra el tipo, “crédito       santander, debito MP”, etc)
		2.1.1.2- elige con 1…n la tarjeta para ver sus datos completos

		2.1.2- agregar tarjeta
			2.1.2.1- ingresar código
			2.1.2.2- ingresar fecha de caducidad
			2.1.2.3- ingresar codigo de seguridad
			2.1.2.4- ingresar nombre de titular
			2.1.2.5- ingresar tipo de tarjeta 
		2.1.3-eliminar tarjeta

	2.2 pago de servicios 
		2.2.1 Pagar Agua → ingrese monto
		2.2.2 Pagar Gas → ingrese monto 
		2.2.3 Pagar Luz → ingrese monto

	2.3 Modificar Cuenta 
		2.2.1 Cambiar contraseña → ingrese contraseña

	2.4 Ingresar Dinero 
2.4.1 Cuenta 
2.4.2 Monto		

	2.4 Salir 

Reportes esperados:
1. Informe estadístico con:
   - Promedios de saldo.
   - Total de gastos y pagos.
   - Servicios más pagados.
   - Evolución del saldo.
2. Archivo LOG con todos los movimientos realizados.
3. Resumen mensual de movimientos y balances.
