#!/usr/bin/env python3

import tkinter as tk
from tkinter import *
from turtle import title
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import ttkcreator as tc
from ttkcreator import *


class Ui(tk.Tk, ttk.Frame):
    def __init__(self):
        ut = tc(self, Menu())
        super().__init__(ttk.Window())

        self.style = ttk.Style(title=None, )
        ttk.Frame.__init__(self, self)


if __name__ == "__main__":
    u = Ui()
    u.mainloop()

"""
      (title: str = "ttkbootstrap", themename: str = "litera", iconphoto: str = '', size: Any | None = None, position: Any | None = None, minsize: Any | None = None, maxsize: Any | None = None, resizable: Any | None = None, hdpi: bool = True, scaling: Any | None = None, transient: Any | None = None, overrideredirect: bool = False, alpha: float = 1) -> None
      
      (master: Misc | None = None, cnf: dict[str, Any] | None = {}, *, activebackground: str = ..., activeborderwidth: _ScreenUnits = ..., activeforeground: str = ..., background: str = ..., bd: _ScreenUnits = ..., bg: str = ..., border: _ScreenUnits = ..., borderwidth: _ScreenUnits = ..., cursor: _Cursor = ..., disabledforeground: str = ..., fg: str = ..., font: _FontDescription = ..., foreground: str = ..., name: str = ..., postcommand: (() -> object) | str = ..., relief: _Relief = ..., selectcolor: str = ..., takefocus: _TakeFocusValue = ..., tearoff: int = ..., tearoffcommand: ((str, str) -> object) | str = ..., title: str = ..., type: Literal['menubar', 'tearoff', 'normal'] = ...) -> None
"""
