__author__ = 'oscarmolina'
import wave
from rangodinamico import taller

def Cargar():
    print('Digite la direccion del archivo:')
    archivo=wave.open(prueba,"rb")
    tamano=archivo.getnframes()
