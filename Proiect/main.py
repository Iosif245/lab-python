import socket
import threading
import random

HOST = '127.0.0.1'
PORT = 5000

class GuessNumberServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(2)
        self.stop_event = threading.Event()

        self.client1 = None
        self.client2 = None

        self.secret_number = None
        self.attempts = 0
        self.max_score = 0
        self.wait_response_from_client1 = True
        self.received_response_from_client1 = False

        print(f"Server started at {host}:{port}. Waiting for clients...")
        self.accept_connections()

    def accept_connections(self):
        """Wait for two connections: Client1 and Client2."""
        while len([c for c in [self.client1, self.client2] if c is not None]) < 2:
            try:
                conn, addr = self.server_socket.accept()

                print(f"Client connected: {addr}")

                if not self.client1:
                    self.client1 = (conn, addr)
                    threading.Thread(target=self.handle_client1, args=(conn, addr)).start()
                elif not self.client2:
                    self.client2 = (conn, addr)
                    threading.Thread(target=self.handle_client2, args=(conn, addr)).start()

            except Exception as e:
                print(f"Error accepting connections: {e}")

   

if __name__ == "__main__":
    server = GuessNumberServer(HOST, PORT)

    while not server.stop_event.is_set():
        threading.Event().wait(1)
