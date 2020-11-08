from tkinter import *
from tkinter import ttk
from settings import *

class Interface:

    def __init__(self):
        self.window = Tk()
        self.window.title(APP_NAME)
        self.window.geometry("{}x{}".format(WINDOW_WIDTH, WINDOW_HEIGHT))
        self.frame1 = Frame(self.window, width=200, height=200, bg="blue")
        self.frame1.pack(side=LEFT, padx=10, pady=10)
        self.list_hostname = ["Hardware", "Sofware1", "Software2"]
        self.combobox1 = ttk.Combobox(self.window, value=self.list_hostname)
        self.combobox1.pack()

    #def create_interface(self):

    def start_copy(self):
        print("\nTest\n")






