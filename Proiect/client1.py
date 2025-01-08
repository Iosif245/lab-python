import socket
import threading
import tkinter as tk

HOST = '127.0.0.1'
PORT = 5000

class Client1GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Client1")

        self.sock = None
        self.stop_event = threading.Event()

        frame = tk.Frame(self.master)
        frame.pack(padx=10, pady=10)

        self.choice_var = tk.StringVar(value="DEFAULT") 

        tk.Label(frame, text="Do you want to provide the secret number for the next game?", anchor="w").pack(fill="x", pady=5)

        self.prompt_rb = tk.Radiobutton(
            frame, text="Please select an option below",
            variable=self.choice_var, value="DEFAULT",
            state="disabled"
        )
        self.prompt_rb.pack(anchor="w")

        self.rb_yes = tk.Radiobutton(
            frame, text="I want to provide a number (0..50)",
            variable=self.choice_var, value="YES",
            command=self.on_choice_changed
        )
        self.rb_yes.pack(anchor="w")

        self.rb_no = tk.Radiobutton(
            frame, text="I do NOT want to provide a number",
            variable=self.choice_var, value="NO",
            command=self.on_choice_changed
        )
        self.rb_no.pack(anchor="w")

        self.entry_number = tk.Entry(frame, state="disabled")
        self.entry_number.pack(fill="x", pady=5)

        self.btn_send = tk.Button(frame, text="Send option", command=self.send_option, state="disabled")
        self.btn_send.pack(fill="x")

        self.txt_log = tk.Text(frame, height=10, state="disabled")
        self.txt_log.pack(fill="both", expand=True)

        self.connect_to_server()

    def connect_to_server(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((HOST, PORT))
            self.log(f"Connected to server {HOST}:{PORT}")

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
    app = Client1GUI(root)
    root.mainloop()
