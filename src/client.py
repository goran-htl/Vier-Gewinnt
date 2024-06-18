import socket
import tkinter as tk
from gui import Connect4GUI

def main():
    root = tk.Tk()

    # Connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    app = Connect4GUI(root, client_socket)
    root.mainloop()

if __name__ == "__main__":
    main()
