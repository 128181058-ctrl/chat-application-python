import socket

HOST = '127.0.0.1'
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Server started. Waiting for connection...")
conn, addr = server.accept()
print("Connected to:", addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    print("Client:", data.decode())

    msg = input("You: ")
    conn.send(msg.encode())

conn.close()
server.close()
