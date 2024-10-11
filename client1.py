import socket

host = '127.0.0.1'
port = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((host,port))
    print("terhubung ke server")
    while 1:
        message = input("Masukkan pesan:")

        client_socket.send(message.encode('utf-8'))
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Respon dari server: {response}")

except:
    print("gagal terhubung")

finally:
    client_socket.close()