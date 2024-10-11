import socket

host = '0.0.0.0'
port = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host,port))
server_socket.listen(1)

print('Menunggu Koneksi...')

client_socket1, addr1 = server_socket.accept()
print(f"Terhubung dengan {addr1}")

while True:
    message1 = client_socket1.recv(1024).decode('utf-8')
    if not message1:
        print('terputus')
        
    print(f"Pesan dari client {addr1}: {message1}")
    client_socket1.send(f"Server menerima: {message1}".encode('utf-8'))

client_socket1.close()
server_socket.close()