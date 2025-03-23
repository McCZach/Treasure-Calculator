from tables.potions import Potion
from tables.rings import Ring
from tables.scrolls import Scroll

import tkinter as tk
from tkinter import scrolledtext

class Application():
    def __init__(self):
        self.__main_window = tk.Tk()
        self.__main_window.geometry('800x600')
        self.__main_window.title('Treasure Generator')

        # Setup Application
        self.__option_frame = tk.Frame(self.__main_window)
        self.__option_frame.pack()

        self.__display_frame = tk.Frame(self.__main_window, border=6, relief='sunken')
        self.__display_frame.pack()

        self.__display_text = scrolledtext.ScrolledText(self.__display_frame, height=400, width=400)
        self.__display_text.tag_configure("red_bg", background='tomato')
        self.__display_text.tag_configure("orange_bg", background='orange')
        self.__display_text.tag_configure("yellow_bg", background='burlywood1')
        self.__display_text.pack()

        # Create Buttons
        self.__generate_potion = tk.Button(self.__option_frame, text='Generate Potion', 
                                           command=lambda: self.display_potion(self.__display_text))
        self.__generate_potion.pack(side='left', padx=5)

        self.__generate_ring = tk.Button(self.__option_frame, text='Generate Ring',
                                        command=lambda: self.display_ring(self.__display_text))
        self.__generate_ring.pack(side='left', padx=5)

        self.__generate_scroll = tk.Button(self.__option_frame, text='Generate Scroll',
                                           command=lambda: self.display_scroll(self.__display_text))
        self.__generate_scroll.pack(side='left', padx=5)

        self.__clear_button = tk.Button(self.__option_frame, text='Clear', 
                                        command=lambda: self.clear_text(self.__display_text))
        self.__clear_button.pack(side='left', padx=5)

        tk.mainloop()

    def clear_text(self, text_box):
        text_box.delete("1.0", tk.END)

    def display_potion(self, text_box):
        text_box.insert(tk.END, Potion.generate_potion(), 'red_bg')

    def display_ring(self, text_box):
        text_box.insert(tk.END, Ring.generate_ring(), 'orange_bg')

    def display_scroll(self, text_box):
        text_box.insert(tk.END, Scroll.generate_scroll(), 'yellow_bg')