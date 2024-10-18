import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('10.4.4.11', 13337))  

s.listen(1)
conn, addr = s.accept()

# Receive a byte from the client
data = conn.recv(1)  # We expect to receive 1 byte
if data:
    # Since data is received as bytes, convert to an integer
    received_value = data[0]  # Get the integer value of the byte

    # Extract i and j
    i = (received_value >> 4) & 0x0F  # Get the upper 4 bits
    j = received_value & 0x0F          # Get the lower 4 bits

    print(f"Received i: {i}, j: {j}")

# Evaluation et envoi du résultat
# res  = eval(data.decode())
# conn.send(str(res).encode())

conn.close()