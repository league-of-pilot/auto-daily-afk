import tkinter as tk
import threading

class LogWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Bot Log")
        self.text = tk.Text(self.root, height=10, width=60)
        self.text.pack()
        threading.Thread(target=self.root.mainloop, daemon=True).start()

    def log(self, msg):
        self.text.insert(tk.END, msg + "\n")
        self.text.see(tk.END)
