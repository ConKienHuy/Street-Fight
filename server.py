import socket, threading, gameplay, pygame

#HOST = socket.gethostbyname(socket.gethostname())
HOST = "192.168.1.225"
PORT = 5555
MAX_CLIENTS = 2

clients = []

def broadcast(key):
    for client in clients:
        client.send(key)

def handle_client(client_socket):
    while True:
        try:
            key = client_socket.recv(1024)
            if not key:
                break
            print("Received:", key.decode())
            broadcast(key)
        except Exception as e:
            print("Error:", e)
            clients.remove(client_socket)
            client_socket.close()
            break

    client_socket.close()

def start_server():
    global ready_count
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        server_socket.bind((HOST, PORT))
        server_socket.listen(MAX_CLIENTS)
        print(f"Server is listening on {HOST}:{PORT}")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address}")

            clients.append(client_socket)
            broadcast(f"__P{len(clients)}".encode())

            thread = threading.Thread(target=handle_client, args=(client_socket,))
            thread.start()

    except Exception as e:
        print("Error:", e)
        clients.remove(client_socket)
        client_socket.close()
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()