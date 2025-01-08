import socket
import threading
import tkinter as tk

HOST = '127.0.0.1'
PORT = 5000


class Client2GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Client2 - Guess the Number")

        self.sock = None
        self.game_active = False 
        self.stop_event = threading.Event()

        frame = tk.Frame(self.master)
        frame.pack(padx=10, pady=10)

        tk.Label(frame, text="Enter your guess (0..50) or a command:\n(NEW GAME / NEW SESSION / STOP)",
                 anchor="w").pack(fill="x", pady=5)

        self.entry_input = tk.Entry(frame, state="disabled")
        self.entry_input.pack(fill="x", pady=5)

        self.btn_send = tk.Button(frame, text="Send", command=self.send_input, state="disabled")
        self.btn_send.pack(fill="x", pady=5)

        self.txt_log = tk.Text(frame, height=10, state="disabled")
        self.txt_log.pack(fill="both", expand=True)

        self.connect_to_server()

    def connect_to_server(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((HOST, PORT))
            self.log(f"Connected to server {HOST}:{PORT}")

            self.entry_input.config(state="normal")
            self.btn_send.config(state="normal")

            threading.Thread(target=self.receive_messages, daemon=True).start()

        except Exception as e:
            self.log(f"Connection error: {e}")
            self.sock = None

    def send_input(self):
        """
        Send the user's guess or command to the server.
        """
        if not self.sock:
            self.log("No connection to the server.")
            return

        user_input = self.entry_input.get().strip().upper()
        if user_input:
            try:
                self.sock.sendall(user_input.encode())
            except Exception as e:
                self.log(f"Error sending input: {e}")

        self.entry_input.delete(0, tk.END)

    def receive_messages(self):
        """
        Continuously receive messages from the server and display them.
        Handle enabling/disabling input based on game state.
        """
        while not self.stop_event.is_set():
            try:
                data = self.sock.recv(1024)
                if not data:
                    self.log("Connection closed by the server.")
                    self.sock.close()
                    self.sock = None
                    self.disable_input()
                    break
                message = data.decode().strip()
                self.log(message)

                if "The game starts now!" in message or "has been generated" in message:
                    self.game_active = True
                    self.enable_input()
                elif "goodbye" in message:
                    self.disable_input()
                    self.sock.close()
                    self.sock = None
                    self.stop_event.set()
                    break
                else:
                    self.game_active = False

            except ConnectionResetError:
                self.log("Connection lost.")
                self.sock = None
                self.disable_input()
                break

        self.master.destroy()

    def disable_input(self):
        """Disable the input and send button."""
        self.entry_input.config(state="disabled")
        self.btn_send.config(state="disabled")

    def enable_input(self):
        """Enable the input and send button."""
        self.entry_input.config(state="normal")
        self.btn_send.config(state="normal")

    def log(self, msg):
        """Append a message to the text area."""
        self.txt_log.config(state="normal")
        self.txt_log.insert(tk.END, msg + "\n")
        self.txt_log.config(state="disabled")
        self.txt_log.see(tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = Client2GUI(root)
    root.mainloop()
