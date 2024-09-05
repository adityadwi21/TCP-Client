import socket
import tkinter as tk
from tkinter import scrolledtext, messagebox

class TCPClientApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TCP Client")

        # Variables
        self.client_socket = None

        # UI Setup
        self.setup_ui()

    def setup_ui(self):
        # IP Address Label and Entry
        tk.Label(self.root, text="IP Address:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.ip_entry = tk.Entry(self.root, width=20)
        self.ip_entry.grid(row=0, column=1, padx=10, pady=5)
        self.ip_entry.insert(0, "127.0.0.1")  # Default IP

        # Port Label and Entry
        tk.Label(self.root, text="Port:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.port_entry = tk.Entry(self.root, width=20)
        self.port_entry.grid(row=1, column=1, padx=10, pady=5)
        self.port_entry.insert(0, "8080")  # Default Port

        # Connect and Disconnect Buttons
        self.connect_button = tk.Button(self.root, text="Connect", command=self.connect_to_server)
        self.connect_button.grid(row=2, column=0, padx=10, pady=10)
        
        self.disconnect_button = tk.Button(self.root, text="Disconnect", command=self.disconnect_from_server, state=tk.DISABLED)
        self.disconnect_button.grid(row=2, column=1, padx=10, pady=10)

        # Message Entry
        tk.Label(self.root, text="Message:").grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        self.message_entry = tk.Entry(self.root, width=50)
        self.message_entry.grid(row=3, column=1, padx=10, pady=5)
        
        # Send Button
        self.send_button = tk.Button(self.root, text="Send", command=self.send_message, state=tk.DISABLED)
        self.send_button.grid(row=4, column=1, padx=10, pady=10)

        # Message Log (Scrolled Text)
        self.message_log = scrolledtext.ScrolledText(self.root, width=60, height=15, state=tk.DISABLED)
        self.message_log.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def connect_to_server(self):
        try:
            ip_address = self.ip_entry.get()
            port = int(self.port_entry.get())
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((ip_address, port))
            self.message_log.config(state=tk.NORMAL)
            self.message_log.insert(tk.END, f"Connected to {ip_address}:{port}\n")
            self.message_log.config(state=tk.DISABLED)

            # Enable/Disable buttons
            self.connect_button.config(state=tk.DISABLED)
            self.disconnect_button.config(state=tk.NORMAL)
            self.send_button.config(state=tk.NORMAL)

        except Exception as e:
            messagebox.showerror("Connection Error", f"Failed to connect: {e}")

    def disconnect_from_server(self):
        if self.client_socket:
            self.client_socket.close()
            self.client_socket = None
            self.message_log.config(state=tk.NORMAL)
            self.message_log.insert(tk.END, "Disconnected from server.\n")
            self.message_log.config(state=tk.DISABLED)

            # Enable/Disable buttons
            self.connect_button.config(state=tk.NORMAL)
            self.disconnect_button.config(state=tk.DISABLED)
            self.send_button.config(state=tk.DISABLED)

    def send_message(self):
        if self.client_socket:
            message = self.message_entry.get()
            if message:
                self.client_socket.sendall(message.encode())
                self.message_log.config(state=tk.NORMAL)
                self.message_log.insert(tk.END, f"Sent: {message}\n")
                self.message_log.config(state=tk.DISABLED)
                self.message_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TCPClientApp(root)
    root.mainloop()
