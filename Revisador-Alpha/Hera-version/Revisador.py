import subprocess
import os

import difflib
import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import alignment

from openpyxl.styles import Font
import socket
import hashlib
import platform
from datetime import datetime

#Salida
nombre = "Resultados.xlsx"
time = 10 #timepo máximo de cada prueba(expresado en segundos)

dict_errores = {
'Semántica': "El código está correctamente escrito en Python, existen problemas de planteamiento de ejercicios 
'IndexError'
}