import string
import random
import hashlib

ejemplo_de_reto = 'jwdoJ3d61ksq2n6l29dnZ3lA93dE2i'
def generar(reto=ejemplo_de_reto, tamaño=25):
    respuesta = ''.join(random.choice(string.ascii_lowercase +
                                      string.ascii_uppercase +
                                      string.digits) for x in range(tamaño))
    intento = reto+respuesta
    return intento, respuesta

shaHash = hashlib.sha256()

def intentoPrueba():
    enconytrado
    pass
    pass
