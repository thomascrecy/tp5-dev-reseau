import socket
import re

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.4.4.11', 13337))
s.send('Hello'.encode())

# On reçoit la string Hello
data = s.recv(1024)

def is_calcul(value: str):
    # Utilisation de re pour capturer les deux nombres et l'opérateur
    match = re.search(r'^(-?\d+)\s*([\+\-\*])\s*(-?\d+)$', value)
    if match:
        num1 = int(match.group(1))
        num2 = int(match.group(3))
        return num1, num2, match.group(2)  # On retourne les deux nombres et l'opérateur
    return None

# Récupération d'une string utilisateur
msg = input("Calcul à envoyer: ")
result = is_calcul(msg)

if not result:
    raise ValueError("Ceci n'est pas un calcul")

num1, num2, operator = result

# Vérif si les nombres sont compris entre -1048575 et +1048575
min_value, max_value = -1048575, 1048575
if not (min_value <= num1 <= max_value and min_value <= num2 <= max_value):
    raise ValueError("Les nombres doivent être compris entre -1048575 et +1048575")

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
