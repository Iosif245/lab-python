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

    def on_choice_changed(self):
        """Called when the user toggles between "I do NOT want to provide a number" and "I want to provide a number"."""
        choice = self.choice_var.get()
        if choice == "YES":
            self.entry_number.config(state="normal")
            self.btn_send.config(state="normal")
            self.rb_yes.config(state="disabled")
            self.rb_no.config(state="disabled")
        elif choice == "NO":
            self.entry_number.config(state="disabled")
            self.btn_send.config(state="normal")
            self.rb_yes.config(state="disabled")
            self.rb_no.config(state="disabled")

        else:
            self.entry_number.config(state="disabled")
            self.btn_send.config(state="disabled")

    def send_option(self):
        """Send the chosen number or 'NO' to the server."""
        if not self.sock:
            self.log("No connection to the server.")
            return

        choice = self.choice_var.get()
        if choice == "YES":
            number_text = self.entry_number.get().strip()
            try:
                number = int(number_text)
                if 0 <= number <= 50:
                    self.sock.sendall(number_text.encode())
                    self.btn_send.config(state="disabled")
                else:
                    self.log("Number must be between 0 and 50.")
                    return
            except ValueError:
                self.log("Please enter a valid integer between 0 and 50.")
                return
        elif choice == "NO":
            try:
                self.sock.sendall("NO".encode())
            except Exception as e:
                self.log(f"Error sending message: {e}")
        else:
            self.log("Please make a valid selection before sending.")
            return

        self.disable_input_during_game()

    def disable_input_during_game(self):
        """User cannot change their decision or send a new number until the current game ends."""
        self.entry_number.config(state="disabled")
        self.btn_send.config(state="disabled")
        self.rb_yes.config(state="disabled")
        self.rb_no.config(state="disabled")

    def enable_input_for_new_game(self):
        """Called when the game ends, so user can choose again for the next game."""
        self.choice_var.set("DEFAULT") 
        self.entry_number.config(state="disabled")
        self.btn_send.config(state="disabled")
        self.rb_yes.config(state="normal")
        self.rb_no.config(state="normal")

    

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
