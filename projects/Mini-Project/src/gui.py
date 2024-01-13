import tkinter as tk
from tkinter import ttk

import ttkbootstrap as boot

class Gui(ttk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.label = ttk.Label(self, text="Hello World!")
        self.label.pack(padx=10, pady=10)
    
        self.button = ttk.Button(self, text="Click me!", command=self.on_button_click)
        self.button.pack()

        # Frame to display clicked number
        self.frame = ttk.Frame(self)
        self.frame.pack(side=tk.LEFT, padx=10)

        self.clicked = 0
        self.clicked_label = ttk.Label(self.frame, text=f'Button clicked: {self.clicked} times')
        self.clicked_label.pack()

    def on_button_click(self):
        self.clicked += 1
        self.label.config(text=f'Button clicked: {self.clicked} times')

        # Update the label in the frame
        self.clicked_label.config(text=f'Button clicked: {self.clicked} times')

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Python Gui")
  
    boot.Style(theme='solar')
  
    user_gui = Gui(root)
    user_gui.pack(fill=tk.BOTH, expand=True)

    root.mainloop()
