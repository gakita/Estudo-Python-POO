import customtkinter
from main import App
import sqlite3

class terms_screen(App):
    def __init__(self):
        self.root.title("Termos de Uso")
        self.root.geometry("1200x800")
        self.root.resizable(False,False)

    