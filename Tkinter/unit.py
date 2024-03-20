from tkinter import *
import random
import new
import configure
import ctypes
import sys

class Cell:
    all = []
    def __init__(self, is_mine=False):
        self.is_mine = is_mine

    def create_btn_object(self, location):
        btn = Button(
            location,
        )   