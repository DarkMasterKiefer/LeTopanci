def validarUsuario(usuario, password):
    if usuario=='admin' and password== 'admin':
        return True
    else:
        return False

def validarGrupo(grupo):
    if grupo=='clientes':
        return True
    else:
        return False