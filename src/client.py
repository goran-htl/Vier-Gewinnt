import socket
import threading
import tkinter as tk

class ConnectFourClient:
    def __init__(self, host='localhost', port=65432):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))
        self.root = tk.Tk()
        self.root.title("Vier Gewinnt Client")
        self.create_widgets()
        self.listen_thread = threading.Thread(target=self.listen_server)
        self.listen_thread.start()
        self.root.mainloop()

    def create_widgets(self):
        self.board_buttons = []
        for col in range(7):
            button = tk.Button(self.root, text=str(col), command=lambda c=col: self.send_move(c))
            button.grid(row=0, column=col)
            self.board_buttons.append(button)
        self.board_labels = [[tk.Label(self.root, text=' ', width=4, height=2, relief='solid') for _ in range(7)] for _ in range(6)]
        for row in range(6):
            for col in range(7):
                self.board_labels[row][col].grid(row=row + 1, column=col)

    def update_board(self, board_str):
        rows = board_str.strip().split('\n')
        for row_idx, row in enumerate(rows):
            cells = row.split('|')
            for col_idx, cell in enumerate(cells):
                self.board_labels[row_idx][col_idx].config(text=cell)

    def send_move(self, col):
        self.client.sendall(str(col).encode('utf-8'))

    def listen_server(self):
        while True:
            data = self.client.recv(1024).decode('utf-8')
            if data.startswith("Du bist Spieler"):
                print(data)
            elif data == "GEWINNER":
                print("Gewonnen!")
                break
            elif data == "UNENTSCHIEDEN":
                print("Unentschieden!")
                break
            elif data == "UNGÜLTIGER ZUG":
                print("Ungültiger Zug. Bitte erneut versuchen.")
            else:
                self.update_board(data)

if __name__ == "__main__":
    client = ConnectFourClient()
