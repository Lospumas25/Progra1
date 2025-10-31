# Kiwillet – Billetera Virtual Local

Kiwillet es una aplicación de consola escrita en Python que simula el funcionamiento básico de una billetera virtual ejecutada de forma local. Permite crear una única cuenta de usuario y administrar tarjetas, movimientos, pagos de servicios y reportes financieros, almacenando toda la información en archivos de texto plano.

## Características principales

- **Gestión de usuario**: creación de la cuenta inicial, inicio de sesión, cambio de contraseña y consulta de saldo disponible.
- **Movimientos**: registro de ingresos de dinero, transferencias y pagos realizados, con detalle de fecha, descripción, monto y saldo resultante.
- **Pagos de servicios**: cálculo y pago parcial o total de servicios básicos (Agua, Gas y Luz) con validaciones de saldo disponible.
- **Tarjetas**: alta, baja y consulta de tarjetas, clasificadas por tipo y con visualización parcial del número para proteger la información sensible.
- **Reportes**: resumen de los últimos movimientos, totales de ingresos/egresos y saldo promedio. Toda actividad queda auditada en un archivo de log.
- **Simulación financiera**: cálculo recursivo de un plazo fijo con tasa fija mensual, útil para estimar ganancias futuras con el saldo actual.

## Requisitos

- Python 3.10 o superior.
- No se requieren dependencias externas; el proyecto utiliza únicamente módulos estándar (`datetime` y `random`).

## Estructura del proyecto

```
Progra1/
├── Main.py        # Punto de entrada: inicia la aplicación y delega en Mudulo.py
├── Mudulo.py      # Lógica principal de la billetera virtual
└── README.md      # Documentación del proyecto
```

### Archivos generados en tiempo de ejecución

La aplicación persiste la información en archivos de texto ubicados en el mismo directorio:

- `Usuario.txt`: almacena nombre de usuario, contraseña y saldo disponible en formato `nombre;contraseña;saldo`.
- `Tarjetas.txt`: guarda cada tarjeta registrada con su código, tipo, número, titular y fecha de vencimiento.
- `Movimientos.txt`: registra los movimientos financieros con fecha ISO, descripción, monto y saldo final.
- `ArchivoLog.txt`: bitácora que almacena cada acción relevante del sistema con sello de tiempo.

## Flujo de ejecución

1. **Inicio**: `Main.py` importa `Mudulo.py` y ejecuta `iniciarAplicacion()`.
2. **Creación de cuenta**: si no existe `Usuario.txt`, se solicita crear un usuario (nombre, contraseña y saldo inicial cero).
3. **Autenticación**: el usuario debe iniciar sesión con sus credenciales para acceder al menú principal.
4. **Menú principal**: desde aquí se pueden ejecutar las distintas operaciones disponibles (consultar saldo, ingresar dinero, transferir, pagar servicios, administrar tarjetas, cambiar contraseña, ver reportes y simular un plazo fijo).
5. **Persistencia**: cada operación válida actualiza los archivos correspondientes y deja registro en la bitácora.

## Organización del código (`Mudulo.py`)

`Mudulo.py` agrupa las funciones en bloques temáticos, separados por comentarios para facilitar su lectura:

- **Log** (`Log`): gestiona la escritura de eventos en `ArchivoLog.txt`.
- **Usuario** (`leerUsuario`, `escribirUsuario`, `crearCuenta`, `login`, `loopLogin`, `mostrarSaldo`, `modificarContraseña`): manejo de credenciales y saldo.
- **Tarjetas** (`leerTarjetas`, `escribirTarjetas`, `agregarTarjeta`, `verTarjetas`, `eliminarTarjeta`, `menuTarjetas`): operaciones CRUD sobre las tarjetas asociadas.
- **Servicios** (`pagarServicio`): selección y pago de servicios básicos con control de saldo.
- **Movimientos** (`registrarMovimientos`, `obtenerMovimientos`, `ingresarDinero`, `transferir`): registro y consulta de transacciones financieras.
- **Reportes** (`mostrarReportes`): generación de un resumen y listado de los últimos movimientos.
- **Simulación** (`calcularPlazoFijo`, `simularPlazoFijo`): proyección recursiva del crecimiento del saldo.
- **Menú y arranque** (`menuPrincipal`, `iniciarAplicacion`): orquestan la interacción con el usuario y el ciclo de vida de la aplicación.

## Cómo ejecutar la aplicación

Desde la raíz del proyecto:

```bash
python Main.py
```

Siga las instrucciones mostradas en consola para crear la cuenta inicial (si aún no existe) e iniciar sesión. Utilice el menú para realizar las distintas operaciones de la billetera virtual. Los archivos de datos se crearán automáticamente en el directorio cuando corresponda.

## Mantenimiento y futuras mejoras

- Permitir múltiples usuarios y manejo de sesiones independientes.
- Integrar validaciones más estrictas para formatos de tarjetas y servicios.
- Incorporar pruebas automatizadas y cobertura de errores para entradas inválidas.
- Migrar el almacenamiento a una base de datos ligera (por ejemplo, SQLite) para mejorar la integridad de los datos.

---

**Autores originales**

- Massun, Felipe
- Scala Merani, Damián (LU 1139436)
- Arias Castroman, Santiago (LU 1224594)
