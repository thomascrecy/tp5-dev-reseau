import socket

file = open('index.html')
html_content = file.read()
file.close()

http_response = 'HTTP/1.0 200 OK\n\n' + html_content
s.send(response.encode())