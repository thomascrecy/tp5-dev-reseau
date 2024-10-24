import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(("10.4.4.11", 13337))
sock.listen()

while True:
    client, client_addr = sock.accept()  
    while True:
        data = client.recv(1024).decode("utf-8")
        if not data:
            break

        response = ""
        if "GET /toto.html" in data:
            file = open('toto.html')
            html_content = file.read()
            file.close()
            response = http_response = 'HTTP/1.0 200 OK\n\n' + html_content + '\n'
            client.send(response.encode())
        elif "GET /" in data:
            response = "HTTP/1.0 200 OK\n\n<h1>Hello je suis un serveur HTTP</h1>\n"
            client.send(response.encode())
        break

    client.close()
s.close()