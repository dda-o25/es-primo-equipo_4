"""
ANGELICA ELIZABETH IBARRA DIAZ
DIAZARTURO ARJONA HERMOSILLOA
CHRISTIAN ALONSO FLORES BURGOS
MARCO FABRIZIO AZPEITIA CASTELLANOS

10 de octubre 2025

Determinar si un número dado es primo
"""

# Declaraciones

#Entradas
numero = int(input("Inserte numero:"))
es_primo = True
#Proceso 
if numero <= 1:
    es_primo = False
else:
    for i in range(2, numero):  
        if numero % i == 0:     
            es_primo = False

#Salidas
if es_primo:
    print(f"{numero} sí es primo.")
else:
    print(f"{numero} no es primo.")
