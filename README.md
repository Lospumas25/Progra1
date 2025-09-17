1# TP_Progra_1_Grupo3 - "FLASHPAY"

//Trabajo Práctico de Programación I. Repositario dedicado a publicar las diferentes versiones y avances en el proyecto//

<p align="center">
<img src="https://github.com/raull127/TP_Progra_1_Grupo3__FLASHPAY/blob/main/media/LogoProvisionalLiveFP.PNG?raw=true" align="centre" width="700" height="700"/>
</p>

    📝 Proyecto

   Objetivo General:

En la actualidad, toda persona conectada a internet requiere de herramientas digitales que le permitan administrar su dinero de manera sencilla, sin necesidad de utilizar servicios bancarios complejos. Una billetera virtual ofrece una solución ágil y accesible para realizar pagos, transferencias y consultas de saldo. El entorno es propicio y la aceptación de las masas genera un contexto ideal para el ingreso de nuevos jugadores que puedan ofrecer soluciones alternativas a los problemas financieros que el consumidor enfrenta dia a dia.
Es por ello que decidimos desarrollar "FLASHPAY", una aplicación de billetera virtual básica que permita a los usuarios registrarse, consultar saldo, cargar dinero, realizar pagos, transferir fondos, convertir divisas y consultar historial de movimientos.

   Objetivos Específicos:
- Implementar un sistema de registro y autenticación de usuarios.
- Gestionar cargas, transferencias y pagos entre usuarios de la aplicación.
- Desarrollar un módulo de conversión de monedas (ej. ARS ↔ USD ↔ EUR).
- Incorporar la visualización del historial de operaciones.
- Aplicar conceptos de estructuras de datos (listas, matrices), programación modular, random, cadenas y slicing.
- Utilizar Git/GitHub para el versionado del código y trabajo colaborativo.


Diagrama de Flujo de la Aplicación:

<p align="center">
<img src="https://github.com/raull127/TP_Progra_1_Grupo3__FLASHPAY/blob/main/media/DiagramaAppWallet.png?raw=true" align="centre" width="800" height="800"/>
</p>

    👥 Equipo 

Integrantes:
- Cantero, Raul Ariel – Legajo: 1184085
- Mamani Argote, Alejandro Matias  – Legajo: 1151978
- Scala Merani, Damian Gabriel – Legajo: 1139436
- Arias Castroman, Santiago – Legajo: 1224594
- Massun, Felipe – Legajo: 1195389

Roles:
- Líder de Proyecto:  Cantero, Raul Ariel
- Diseñador UX/UI: Mamani Argote, Alejandro Matias
- Programador de Gestión de Usuarios: Scala Merani, Damian Gabriel
- Programador de Transacciones: Arias Castroman, Santiago
- Programador de Gestión Fondos/Datos: Massun, Felipe

.

    🎥 Presentación del Proyecto

Se adjunta un video introductorio como presentación del proyecto y del grupo de trabajo
.
[![Watch the video](https://github.com/raull127/TP_Progra_1_Grupo3__FLASHPAY/blob/main/media/222.PNG?raw=true)](https://youtu.be/BD-hEeCRqBA)
.

    📚  Desarrollo y Planes de Proyecto

Objetivos y entregables finales:
- Prototipo en Python publicado en un repositorio GitHub abierto.
- Documento de alcance.
- Presentación PPTX.
- Video grupal de presentación.
 
 Requisitos

- Funcionales:
1. Registro e inicio de sesión de usuarios.
2. Consulta de saldo.
3. Carga de dinero.
4. Transferencias entre cuentas.
5. Pagos a otros usuarios.
6. Conversión de divisas.
7. Historial de transacciones.

- No Funcionales:
1. Interfaz en Consola (Python).
2. Seguridad básica mediante validaciones de entrada.
3. Uso de módulos y funciones organizadas.
4. Control de versiones en GitHub.

Flujo de Ejecucion:

1) Iniciar Sesión
- Mostrar pantalla de inicio y opción “Iniciar Sesión”
- Ingresar ID y Contraseña (strings)

2) Validación (Protegido por Contraseña)
- Buscar ID en la matriz usuarios (todo string).
- Si credenciales inválidas → informar y volver a Iniciar Sesión.
- Si credenciales válidas → determinar rol:
-    Usuario → ir a Menú Principal del Usuario.
-    Administrador → ir a Menú Principal del Administrador (rama admin del diagrama).

3) Menú Principal del Usuario
Opciones (cada acción vuelve al Menú Principal):
- Ingresar / Retirar Dinero
  Ingresar: leer monto, sumar al saldo, guardar como string
  Registrar en transacciones: [fecha, id, "-", "CARGA", monto, moneda, ""]
  Retirar: validar fondos, restar del saldo y registrar "RETIRO" si lo incluyen
  
- Saldo
  Mostrar saldo y moneda desde usuarios (solo lectura)

- Transferencias
  Pedir id_destino y monto
  Validar existencia y fondos
  Debitar origen, acreditar destino
  Registrar en historial

- Conversión a Moneda Extranjera
  Elegir moneda
  Calcular con valor de la moneda
  Actualizar saldo convertido y moneda
  Registrar CONVERSION

- Historial
  Filtrar en transacciones por id
  Slicing de la fecha para formato (AAAA-MM-DD / HH-MM-SS)
  Filtros por fecha o cantidad

- Cerrar Sesión
  Volver al menu principal

4) Menú Principal del Administrador (rama “Como Usuario o Administrador”)
- Opciones típicas (todas regresan al menú admin):
- Usuarios: alta/baja/listado (matriz usuarios, todo string).
- Reportes (ver siguiente punto).
- Cerrar Sesión.

5) Informes
- Total por usuario
- Total por categoría
- Promedio por usuario
- Usuarios sin pagos
- Total general
- Fechas de pagos

6) Salida
- Cerrar sesión (vuelve a Iniciar Sesión).
- Salir (termina el programa).

Matrices:
usuarios = [[id, nombre, pass, saldo, moneda]]
transacciones = [[fecha, id_origen, id_destino, tipo, monto, moneda, detalle]]
contactos = [[id_owner, id_contacto, alias]]


Recursos
- Equipo de trabajo: 5 integrantes.
- Tiempo estimado: alrededor de 4 semanas de desarrollo (Etapa 1).
- Software: Python, Git/GitHub, Google Docs/Word, PowerPoint.


Cronograma

- 27/08/2025: Entrega del documento de alcance con definición de funcionalidades, requisitos y plan de evolucion de la aplicacion.  

- 03/09/2025: Trabajo en clase grupal orientado a afrontar aspectos del desarrollo y discutir como encarar los pasos siguientes.   

- 10/09/2025: Presentación Etapa 1 + defensa grupal. Demo funcional de la aplicación como prototipo mínimo viable (MVP) de una billetera virtual.   

Limitaciones:
- No se desarrollará una interfaz gráfica compleja (será en consola).
- No se implementarán sistemas de pago reales (solo simulaciones).
- Buena parte de la gestión de datos y mecanismos de seguridad será simulado, sin encriptación robusta o manejo avanzado de datos.

Fuera del alcance:
- Integración con bancos o servicios financieros reales
- Aplicación móvil o web con frontend avanzado
- Mecanismos de seguridad bancaria (encriptación avanzada, validaciones biométricas).

Motivo de Eleccion del Proyecto:

- La digitalización de los pagos es una tendencia en crecimiento en Argentina y en el mundo. Este proyecto busca simular una billetera virtual que no solo sea un ejercicio académico, sino también una propuesta inicial de solución para la inclusión financiera y el manejo simple de dinero electrónico.

<p align="center">
<img src="https://raw.githubusercontent.com/raull127/TP_Progra_1_Grupo3__FLASHPAY/refs/heads/main/media/LogoProvisionalMinimal0.png" align="centre" width="100" height="100"/>
</p>
