import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.4.4.11', 13337))
s.send('Hello'.encode())

# On reçoit la string Hello
data = s.recv(1024)

# Récupération d'une string utilisateur
msg = input("Calcul à envoyer: ")

# Verif input de l'utilisateur
if msg < -1048575 or msg > +1048575 :
    print("Erreur, veuillez entrez des nombres compris entre -1048575 et +1048575")
    msg = input("Calcul à envoyer: ")



# On envoie
s.send(msg.encode())

# Réception et affichage du résultat
s_data = s.recv(1024)
print(s_data.decode())
s.close()
