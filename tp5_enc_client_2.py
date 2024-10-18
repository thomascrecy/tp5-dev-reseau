import socket
import re

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.4.4.11', 13337))

# def
def is_calcul(value: str):
    return re.search(r'^(-?\d+)\s*[\+\-\*]\s*(-?\d+)$', value)

def check_under_4bytes(l:list):
    return 0==len([int(x) for x in l if int(x) >= 4294967295])

#########################################
msg = input("Calcul à envoyer: ")
if not is_calcul(msg):
    raise ValueError("Ceci n'est pas un calcul")

values = re.split(r"\s*[\+\-\*]\s*", msg)
if not check_under_4bytes(values):
    raise ValueError("Valeur trop grande")

numbers = re.findall(r'\d+', msg)

# Récuper les chiffres et les mettres en variables
i, j = map(int, numbers)

i_one_byte = i.to_bytes(1, byteorder='big')
j_one_byte = j.to_bytes(1, byteorder='big')

# on décale l'un des deux de 4
shifted_i = i << 4 # ça donne 0001 0000

# donc on a j avec 4 bits useless à gauche à 0
# et shifted_i avec 4 bits useless à droite
# tu le vois venir nan ? FUSION
final = shifted_i | j # le OU logique est parfait pour cette situation

# On envoie
print(final.encode())
s.send(final.encode())

# Réception et affichage du résultat
#s_data = s.recv(1024)
#print(s_data.decode())
s.close()
