import socket
import re

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.4.4.11', 13337))
s.send('Hello'.encode())

# On reçoit la string Hello
data = s.recv(1024)

def is_calcul(value: str):
    return re.search(r'^(-?\d+)\s*[\+\-\*]\s*(-?\d+)$', value)

# Récupération d'une string utilisateur
msg = input("Calcul à envoyer: ")
if not is_calcul(msg):
    raise ValueError("Ceci n'est pas un calcul")

# Verif si les nombres sont compris entre -1048575 et +1048575
# print("ERROR: Veuillez entrer des nombres entre -1048575 et +1048575.")

# on encode le message explicitement en UTF-8 pour récup un tableau de bytes
encoded_msg = msg.encode('utf-8')

# on calcule sa taille, en nombre d'octets
msg_len = len(encoded_msg)

# on encode ce nombre d'octets sur une taille fixe de 4 octets
header = msg_len.to_bytes(4, byteorder='big')

# on peut concaténer ce header avec le message, avant d'envoyer sur le réseau
payload = header + encoded_msg

# on peut envoyer ça sur le réseau
print(payload)
s.send(payload)

# Réception et affichage du résultat
s_data = s.recv(1024)
print(s_data.decode())
s.close()
