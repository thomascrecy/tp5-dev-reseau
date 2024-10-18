import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('10.4.4.11', 13337))  
s.listen(1)
conn, addr = s.accept()

END_MESSAGE = "<clafin>"

while True:
    # On lit les 4 premiers octets qui arrivent du client
    # Car dans le client, on a fixé la taille du header à 4 octets
    header = conn.recv(4)
    if not header:
        break

    # On lit la valeur
    msg_len = int.from_bytes(header[0:4], byteorder='big')

    print(f"Lecture des {msg_len} prochains octets")

    # Une liste qui va contenir les données reçues
    chunks = []

    bytes_received = 0
    while bytes_received < msg_len:
        # Si on reçoit + que la taille annoncée, on lit 1024 par 1024 octets
        chunk = conn.recv(min(msg_len - bytes_received, 1024))
        if not chunk:
            raise RuntimeError('Invalid chunk received bro')

        # on ajoute le morceau de 1024 ou moins à notre liste
        chunks.append(chunk)

        # on ajoute la quantité d'octets reçus au compteur
        bytes_received += len(chunk)

    # ptit one-liner pas combliqué à comprendre pour assembler la liste en un seul message
    message_received = b"".join(chunks).decode('utf-8')
    end_check = message_received[-(len(END_MESSAGE)):]
    message = message_received[:len(message_received)-len(END_MESSAGE)]

    if end_check == END_MESSAGE:
        print(f"Received from client {message}")
    else:
        print("Aucun séquence de fin trouvée")

conn.close()
s.close()