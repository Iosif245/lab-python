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
