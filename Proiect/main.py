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

    def handle_client1(self, conn, addr):
        while not self.stop_event.is_set():
            if self.wait_response_from_client1:
                try:
                    self.send_to(conn, "Choose an option for current game")
                    data = conn.recv(1024)
                    if not data:
                        print(f"Client1 disconnected: {addr}")
                        self.client1 = None
                        conn.close()
                        break

                    message = data.decode().strip()
                    self.wait_response_from_client1 = False
                    self.received_response_from_client1 = True
                    if message == "NO":
                        self.broadcast("Client1 did not provide a number. A random number will be generated.")
                        self.secret_number = None
                    else:
                        try:
                            number = int(message)
                            if 0 <= number <= 50:
                                self.secret_number = number
                                self.send_to(conn, f"Number {number} has been set.")
                            else:
                                self.send_to(conn, "The number must be within the range [0..50].")
                        except ValueError:
                            self.send_to(conn, "Please send a valid number.")

                except ConnectionResetError:
                    print(f"Connection lost with Client1: {addr}")
                    self.client1 = None
                    break
                except Exception as e:
                    print(f"Error handling Client1 ({addr}): {e}")
                    self.client1 = None
                    break

    def handle_client2(self, conn, addr):
        self.start_new_game()
        while not self.stop_event.is_set():
            try:
                data = conn.recv(1024)
                if not data:
                    print(f"Client2 disconnected: {addr}")
                    self.client2 = None
                    conn.close()
                    break

                message = data.decode().strip()

                if message.upper() in ["NEW GAME"]:
                    self.broadcast("Client2 requested a NEW GAME. The maximum score remains.")
                    self.received_response_from_client1 = False
                    self.wait_response_from_client1 = True
                    self.start_new_game()
                    continue
                elif message.upper() in ["NEW SESSION"]:
                    self.broadcast("Client2 requested a NEW SESSION. The maximum score is reset.")
                    self.max_score = 0
                    self.received_response_from_client1 = False
                    self.wait_response_from_client1 = True
                    self.start_new_game()
                    continue
                elif message.upper() in ["STOP"]:
                    self.broadcast("Client2 requested to stop. Shutting down server...")
                    self.stop_server()
                    break

                try:
                    guess = int(message)
                except ValueError:
                    self.send_to(conn,
                                 "Please send a number (0..50) or a valid command (NEW GAME / NEW SESSION / STOP).")
                    continue

                self.attempts += 1

                if guess == self.secret_number:
                    score = self.calculate_score(self.attempts)
                    self.broadcast(
                        f"Client2 guessed the number {self.secret_number} in {self.attempts} attempts. Score: {score}")

                    self.max_score += score

                    self.broadcast(f"The current session's max score is: {self.max_score}")

                    self.send_to(conn, "Choose an option: NEW GAME / NEW SESSION / STOP")
                else:
                    if guess < self.secret_number:
                        response = "HIGHER"
                    else:
                        response = "LOWER"
                    self.broadcast(f"Guess: {guess}. Answer: {response}")

            except ConnectionResetError:
                print(f"Connection lost with Client2: {addr}")
                self.client2 = None
                break
            except Exception as e:
                print(f"Error handling Client2 ({addr}): {e}")
                self.client2 = None
                break

    def start_new_game(self):
        self.attempts = 0

        while not self.received_response_from_client1:
            threading.Event().wait(1)

        if self.secret_number is None:
            self.secret_number = random.randint(0, 50)
            self.broadcast("A random secret number (0..50) has been generated.")
        else:
            self.broadcast("The secret number provided by Client1 is set. The game starts now!")

    def calculate_score(self, tries):
        points = 100 - 5 * (tries - 1)
        return max(0, points)

    def broadcast(self, message):
        """Send a message to both Client1 and Client2."""
        for client in [self.client1, self.client2]:
            if client:
                conn, _ = client
                try:
                    conn.sendall((message + "\n").encode())
                except Exception as e:
                    print(f"Failed to send message to {client[1]}: {e}")
        print(message)

    def send_to(self, client_conn, message):
        """Send a message to a specific client."""
        try:
            client_conn.sendall((message + "\n").encode())
        except Exception as e:
            print(f"Failed to send message to a client: {e}")

    def stop_server(self):
        """Broadcast a shutdown message, close all connections, and exit."""
        self.broadcast("The server is shutting down. Goodbye!")
        for c in [self.client1, self.client2]:
            if c:
                conn, _ = c
                try:
                    conn.close()
                except Exception as e:
                    print(f"Error closing connection: {e}")
        self.stop_event.set()
        self.server_socket.close()
        exit(0)


if __name__ == "__main__":
    server = GuessNumberServer(HOST, PORT)

    while not server.stop_event.is_set():
        threading.Event().wait(1)
