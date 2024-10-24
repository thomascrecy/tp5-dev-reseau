import socket
import datetime
import logging
import time

##### LOGS #######
LOG_DIR = "/var/log/bs_server"
LOG_FILE = "bs_server2.log"

def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt="%Y-%m-%d %H:%M")
        return formatter.format(record)

file_handler = logging.FileHandler(f"{LOG_DIR}/{LOG_FILE}", encoding="utf-8", mode="a")
file_handler.setLevel(logging.INFO)

file_formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s", datefmt="%Y-%m-%d %H:%M")
file_handler.setFormatter(file_formatter)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)
logger.addHandler(console_handler)
##### LOGS #######

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
            logging.info(f'Le client a téléchargé toto.html.')
        elif "GET /" in data:
            response = "HTTP/1.0 200 OK\n\n<h1>Hello je suis un serveur HTTP</h1>\n"
            client.send(response.encode())
            logging.info(f'Le client a téléchargé index.html.')
        break

    client.close()
s.close()