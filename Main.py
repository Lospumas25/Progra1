import modulo


def main ():
    existe = verificarExistenciaUsuario ()
    if existe == False:
        crearCuenta ()
    loopLogin ()
    



